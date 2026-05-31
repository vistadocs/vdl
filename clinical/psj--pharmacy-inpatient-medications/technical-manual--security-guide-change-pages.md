---
title: PSJ*5*181 Technical Manual/Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: null
app_code: PSJ
app_name: 'Pharmacy: Inpatient Medications'
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*181
group_key: PSJ:PSJ:5
file_numbers:
- '1'
- '2'
- '4'
- '7'
- '8'
- '50'
- '50.68'
- '50.7'
- '51.1'
- '51.2'
- '57.1'
- '57.5'
- '58.1'
- '59.5'
- '59.6'
- '59.7'
- '200'
security_keys:
- PROVIDER
- PSJ PHARM TECH
- PSJ RNURSE
- PSJ RPHARM
- PSJI MGR
menu_options: 0
description: '> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the exi'
audience: Technical staff, IRM, system administrators
keywords: []
page_count: 0
word_count: 7580
section_count: 9
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: December 1997
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p181_tm_cp.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p181_tm_cp.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=88
audit_applied: '2026-05-31'
master_source: PSJ*5*181 Technical Manual/Security Guide Change Pages
master_pub_date: December 1997
consolidated_from: 11 versions
prior_versions:
- PSJ*5*134 Technical Manual/Security Guide Change Pages
- PSJ*5*178 Technical Manual/Security Guide Change Pages
- PSJ*5*214 Technical Manual/Security Guide Change Pages
- PSJ*5*222 Technical Manual/Security Guide Change Pages
- PSJ*5*226 Technical Manual/Security Guide Change Pages
- PSJ*5*254 Technical Manual/Security Guide Change Pages
- PSJ*5*267 Technical Manual/Security Guide Change Pages
- PSJ*5*275 Technical Manual/Security Guide Change Pages
- PSJ*5*279 Technical Manual/Security Guide Change Pages
- PSJ*5*284 Technical Manual/Security Guide Change Pages
consolidated_title: technical manual/security guide change pages
---

> ![](psj-5-181-technical-manual-security-guide-change-pages/001.png)

INPATIENT MEDICATIONS

> TECHNICAL MANUAL/ SECURITY GUIDE

> Version 5.0

> December 1997

> (Revised April 2011)

> Department of Veterans Affairs Product Development

> Revision History

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
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
<td><blockquote>
<p>04/2011</p>
</blockquote></td>
<td><blockquote>
<p>i, v, vi, vii, viii, 5- 8b (changed flow), 22,</p>
<p>23, 24,</p>
<p>removed 25-26,</p>
<p>changed 53, 85, 86,</p>
<p>93-</p>
<p>94;94a-b,</p>
<p>121--130</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*181</p>
</blockquote></td>
<td><blockquote>
<p>Changes to <em>Revision History</em>, <em>Table of Contents</em>; added new field to PHARMACY SYSTEM File (#59.7), added new field to the INPATIENT WARD PARAMETERS File (#59.6). Added</p>
<p>information re: the Pharmacy Reengineering (PRE) API Manual under "<em>Callable Routines</em>"; removed entire section 5.3, Routine Mapping, and all its sub-sections; added Health Level Seven (HL7) data field under segment { RXC}. Added the following "<em>Inpatient Medications Custodial Integration Agreements</em>": 4074, 4264, 4580, 5001, 5057; 5058, 5306, 5385. Added two</p>
<p>packages, HWSC and VistALink, to <em>External Relationships</em>, under <em>Packages Needed to Run Inpatient Medications</em>. Added the following call routines and their entry points: OROCAPI, PSSDSAPD, PSSDSAPI, PSSFDBRT, PSODDPR4,</p>
<p>PSODRDU2. Added the items <strong>DATUP, MOCHA, PECS, and PEPS</strong> in Glossary, which shifted all subsequent glossary items. Added routines PSJMISC2 &amp;PSJOCVAR to the routines table and removed Section 5.3</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>02/11</p>
</blockquote></td>
<td><blockquote>
<p>i, 53, 62,</p>
<p>64, 65</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*226</p>
</blockquote></td>
<td><blockquote>
<p>Added to RXC section Field 5, "Additive Frequency" in HL7 Ordering Fields; updated Front Door – IV Fluids table with Field 5; updated Back Door – IV Fluids table with Field 5; updated example.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/10</p>
</blockquote></td>
<td><blockquote>
<p>i, 22-23</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*113</p>
</blockquote></td>
<td><blockquote>
<p>Added routine PSGSICH1.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>02/10</p>
</blockquote></td>
<td><blockquote>
<p>i, 23</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*214</p>
</blockquote></td>
<td><blockquote>
<p>Added PSJQUTIL to the routine list in Section 5.1 for Patients on Specific Drug(s) Multidivisional Enhancements Project.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12/09</p>
</blockquote></td>
<td><blockquote>
<p>22-23</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*222</p>
</blockquote></td>
<td><blockquote>
<p>Added routine PSGOEF2.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
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
<td><blockquote>
<p>08/08</p>
</blockquote></td>
<td><blockquote>
<p>vi, 23, 51-</p>
</blockquote>
<p>53, 57-58,</p>
<p>60-61, 63,</p>
<blockquote>
<p>65, 65a-</p>
<p>65b</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*134</p>
</blockquote></td>
<td><blockquote>
<p>Parameters for escaping special characters added. New HL7 messages added. New routines added. HL7 order fields table contains an asterisk for each field that has special escaping characters.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>02/07</p>
</blockquote></td>
<td><blockquote>
<p>74-76</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*178</p>
</blockquote></td>
<td><blockquote>
<p>MED ROUTE now appears in larger font on IV labels from the Zebra bar code printer. Med ROUTE now prints on the IV labels for bar-code enabled printers, and it prints in larger font than surrounding text.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>09/06</p>
</blockquote></td>
<td><blockquote>
<p>23, 94</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*172</p>
</blockquote></td>
<td><blockquote>
<p>Encapsulation Cycle II project: Added PSJ53P1 to the Routine List in Section 5.1. Added DBIA 4537 to DBIA list. Changed the date on the Title Page to December 1997.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>05/06</p>
</blockquote></td>
<td><blockquote>
<p>v-viii 8a-8b 66-68b</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*154</p>
</blockquote></td>
<td><blockquote>
<p>In Section 2.2.2 Added "PRIORITIES FOR NOTIFICATION"</p>
<p>field.</p>
<p>In Section 9.5, made correction to include the priority of ASAP in notifications. Added information regarding the three notifications parameters.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12/2005</p>
</blockquote></td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*146</p>
</blockquote></td>
<td><blockquote>
<p>Remote Data Interoperability (RDI) Project: Added PSJLMUT2 to the Routine List in Section 5.1.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11/2005</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*163</p>
</blockquote></td>
<td><blockquote>
<p>Encapsulation Cycle II project: Added PSJ59P5 to the Routine List in Section 5.1. Added DBIA 4819 to DBIA list. Deleted DBIAs 172, 634, and 1882 from the DBIA list.</p>
<p>Reissued entire document due to a page numbering issue. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Routines](#routines)
  - [Descriptions](#descriptions)
  - [Callable Routines](#callable-routines)
    - [Deleting Inpatient Routines](#deleting-inpatient-routines)
  - [Health Level Seven (HL7) Messaging](#health-level-seven-hl7-messaging)
    - [HL7 Ordering Fields](#hl7-ordering-fields)
    - [Order Event Messages](#order-event-messages)
    - [Front Door - Inpatient Medications](#front-door-inpatient-medications)
    - [Example: Digoxin .125 mg QAM](#example-digoxin-125-mg-qam)
- [External Relationships](#external-relationships)
  - [Packages Needed to Run Inpatient Medications](#packages-needed-to-run-inpatient-medications)
  - [Unit Dose Medications and Ward Stock](#unit-dose-medications-and-ward-stock)
  - [Unit Dose Medications and Drug Accountability](#unit-dose-medications-and-drug-accountability)
  - [Calls Made by Inpatient Medications](#calls-made-by-inpatient-medications)
  - [Introduction to Integration Agreements and Entry Points](#introduction-to-integration-agreements-and-entry-points)
- [Glossary](#glossary)
    - [ListMan Action Prompts](#listman-action-prompts)
    - [Patient/Order Action Prompts](#patientorder-action-prompts)
    - [Hidden Action Prompts](#hidden-action-prompts)
> This technical manual is written for the Information Resources Management Service (IRMS) Chief/Site Manager and the Automated Data Processing Application Coordinator (ADPAC) for implementation and installation of the Inpatient Medications package. The main text of the manual outlines routine descriptions, file list, site configuration issues, variables, resource requirements, and package security.
> (*This page included for two-sided copying*.)

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following routines are exported by the Inpatient Medications package. Routine names starting with the letters PSG designate routines used mainly by the Unit Dose Medications module. Routine names starting with the letters PSIV designate routines used mainly by the IV Medications module. Routine names starting with the letters PSJ designate Inpatient Medications routines - utilities used by IV, Unit Dose, and other packages.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PSGAL5</p>
</blockquote></th>
<th>PSGAMS</th>
<th>PSGAMS0</th>
<th><blockquote>
<p>PSGAMSA</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSGAP</p>
</blockquote></td>
<td>PSGAP0</td>
<td>PSGAPH</td>
<td><blockquote>
<p>PSGAPIV</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGAPP</p>
</blockquote></td>
<td>PSGAXR</td>
<td>PSGBRJ</td>
<td><blockquote>
<p>PSGCAP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGCAP0</p>
</blockquote></td>
<td>PSGCAPIV</td>
<td>PSGCAPP</td>
<td><blockquote>
<p>PSGCAPP0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGCT</p>
</blockquote></td>
<td>PSGDCC</td>
<td>PSGDCCM</td>
<td><blockquote>
<p>PSGDCR0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGDCT</p>
</blockquote></td>
<td>PSGDCT1</td>
<td>PSGDCTP</td>
<td><blockquote>
<p>PSGDL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGDS</p>
</blockquote></td>
<td>PSGDS0</td>
<td>PSGDSP</td>
<td><blockquote>
<p>PSGDSP0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGDSP1</p>
</blockquote></td>
<td>PSGDSPN</td>
<td>PSGEUD</td>
<td><blockquote>
<p>PSGEUDD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGEUDP</p>
</blockquote></td>
<td>PSGFILD0</td>
<td>PSGFILD1</td>
<td><blockquote>
<p>PSGFILD2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGFILD3</p>
</blockquote></td>
<td>PSGFILED</td>
<td>PSGGAO</td>
<td><blockquote>
<p>PSGIU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGL</p>
</blockquote></td>
<td>PSGL0</td>
<td>PSGLBA</td>
<td><blockquote>
<p>PSGLH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGLOI</p>
</blockquote></td>
<td>PSGLPI</td>
<td>PSGLW</td>
<td><blockquote>
<p>PSGMAR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGMAR0</p>
</blockquote></td>
<td>PSGMAR1</td>
<td>PSGMAR2</td>
<td><blockquote>
<p>PSGMAR3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGMI</p>
</blockquote></td>
<td>PSGMIV</td>
<td>PSGMMAR</td>
<td><blockquote>
<p>PSGMMAR0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGMMAR1</p>
</blockquote></td>
<td>PSGMMAR2</td>
<td>PSGMMAR3</td>
<td><blockquote>
<p>PSGMMAR4</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGMMAR5</p>
</blockquote></td>
<td>PSGMMARH</td>
<td>PSGMMIV</td>
<td><blockquote>
<p>PSGMMIVC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGMUTL</p>
</blockquote></td>
<td>PSGNE3</td>
<td>PSGO</td>
<td><blockquote>
<p>PSGOD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGOE</p>
</blockquote></td>
<td>PSGOE0</td>
<td>PSGOE1</td>
<td><blockquote>
<p>PSGOE2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGOE3</p>
</blockquote></td>
<td>PSGOE31</td>
<td>PSGOE4</td>
<td><blockquote>
<p>PSGOE41</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGOE42</p>
</blockquote></td>
<td>PSGOE5</td>
<td>PSGOE6</td>
<td><blockquote>
<p>PSGOE7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGOE8</p>
</blockquote></td>
<td>PSGOE81</td>
<td>PSGOE82</td>
<td><blockquote>
<p>PSGOE9</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PSGOE91</p>
</blockquote></th>
<th>PSGOE92</th>
<th><blockquote>
<p>PSGOEC</p>
</blockquote></th>
<th><blockquote>
<p>PSGOECA</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSGOECS</p>
</blockquote></td>
<td>PSGOEE</td>
<td><blockquote>
<p>PSGOEE0</p>
</blockquote></td>
<td><blockquote>
<p>PSGOEEW</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGOEF</p>
</blockquote></td>
<td>PSGOEF1</td>
<td><blockquote>
<p>PSGOEF2</p>
</blockquote></td>
<td><blockquote>
<p>PSGOEH0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGOEH1</p>
</blockquote></td>
<td>PSGOEHA</td>
<td><blockquote>
<p>PSGOEI</p>
</blockquote></td>
<td><blockquote>
<p>PSGOEL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGOEM</p>
</blockquote></td>
<td>PSGOEM1</td>
<td><blockquote>
<p>PSGOENG</p>
</blockquote></td>
<td><blockquote>
<p>PSGOEPO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGOER</p>
</blockquote></td>
<td>PSGOER0</td>
<td><blockquote>
<p>PSGOER1</p>
</blockquote></td>
<td><blockquote>
<p>PSGOERI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGOERS</p>
</blockquote></td>
<td>PSGOES</td>
<td><blockquote>
<p>PSGOESF</p>
</blockquote></td>
<td><blockquote>
<p>PSGOETO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGOETO1</p>
</blockquote></td>
<td>PSGOEV</td>
<td><blockquote>
<p>PSGOEVS</p>
</blockquote></td>
<td><blockquote>
<p>PSGON</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGORS0</p>
</blockquote></td>
<td>PSGORVW</td>
<td><blockquote>
<p>PSGOT</p>
</blockquote></td>
<td><blockquote>
<p>PSGOTR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGOU</p>
</blockquote></td>
<td>PSGP</td>
<td><blockquote>
<p>PSGPEN</p>
</blockquote></td>
<td><blockquote>
<p>PSGPER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGPER0</p>
</blockquote></td>
<td>PSGPER1</td>
<td><blockquote>
<p>PSGPER2</p>
</blockquote></td>
<td><blockquote>
<p>PSGPL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGPL0</p>
</blockquote></td>
<td>PSGPL1</td>
<td><blockquote>
<p>PSGPLD</p>
</blockquote></td>
<td><blockquote>
<p>PSGPLDP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGPLDP0</p>
</blockquote></td>
<td>PSGPLDPH</td>
<td><blockquote>
<p>PSGPLF</p>
</blockquote></td>
<td><blockquote>
<p>PSGPLFM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGPLG</p>
</blockquote></td>
<td>PSGPLPRG</td>
<td><blockquote>
<p>PSGPLR</p>
</blockquote></td>
<td><blockquote>
<p>PSGPLR0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGPLRP</p>
</blockquote></td>
<td>PSGPLUP</td>
<td><blockquote>
<p>PSGPLUP0</p>
</blockquote></td>
<td><blockquote>
<p>PSGPLUTL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGPLXR</p>
</blockquote></td>
<td>PSGPO</td>
<td><blockquote>
<p>PSGPOR</p>
</blockquote></td>
<td><blockquote>
<p>PSGPR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGPRVR</p>
</blockquote></td>
<td>PSGPRVR0</td>
<td><blockquote>
<p>PSGRET</p>
</blockquote></td>
<td><blockquote>
<p>PSGRPNT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGS0</p>
</blockquote></td>
<td>PSGSCT</td>
<td><blockquote>
<p>PSGSCT0</p>
</blockquote></td>
<td><blockquote>
<p>PSGSEL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGSET</p>
</blockquote></td>
<td>PSGSETU</td>
<td><blockquote>
<p>PSGSH</p>
</blockquote></td>
<td><blockquote>
<p>PSGSICH1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGSICHK</p>
</blockquote></td>
<td>PSGSSP</td>
<td><blockquote>
<p>PSGTAP</p>
</blockquote></td>
<td><blockquote>
<p>PSGTAP0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGTAP1</p>
</blockquote></td>
<td>PSGTCTD</td>
<td><blockquote>
<p>PSGTCTD0</p>
</blockquote></td>
<td><blockquote>
<p>PSGTI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGVBW</p>
</blockquote></td>
<td>PSGVBW0</td>
<td><blockquote>
<p>PSGVBW1</p>
</blockquote></td>
<td><blockquote>
<p>PSGVBWP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSGVBWU</p>
</blockquote></td>
<td>PSGVDS</td>
<td><blockquote>
<p>PSGVW</p>
</blockquote></td>
<td><blockquote>
<p>PSGVW0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSGVWP</p>
</blockquote></td>
<td>PSIV</td>
<td><blockquote>
<p>PSIVACT</p>
</blockquote></td>
<td><blockquote>
<p>PSIVAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVALN</p>
</blockquote></td>
<td>PSIVALNC</td>
<td><blockquote>
<p>PSIVAMIS</p>
</blockquote></td>
<td><blockquote>
<p>PSIVAOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVAOR1</p>
</blockquote></td>
<td>PSIVBCID</td>
<td><blockquote>
<p>PSIVCAL</p>
</blockquote></td>
<td><blockquote>
<p>PSIVCHK</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVCHK1</p>
</blockquote></td>
<td>PSIVCSED</td>
<td><blockquote>
<p>PSIVDCR</p>
</blockquote></td>
<td><blockquote>
<p>PSIVDCR1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVDCR2</p>
</blockquote></td>
<td>PSIVDRG</td>
<td><blockquote>
<p>PSIVEDRG</p>
</blockquote></td>
<td><blockquote>
<p>PSIVEDT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVEDT1</p>
</blockquote></td>
<td>PSIVHIS</td>
<td><blockquote>
<p>PSIVHLD</p>
</blockquote></td>
<td><blockquote>
<p>PSIVHLP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVHLP1</p>
</blockquote></td>
<td>PSIVHLP2</td>
<td><blockquote>
<p>PSIVHLP3</p>
</blockquote></td>
<td><blockquote>
<p>PSIVHYP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVHYPL</p>
</blockquote></td>
<td>PSIVHYPR</td>
<td><blockquote>
<p>PSIVLABL</p>
</blockquote></td>
<td><blockquote>
<p>PSIVLABR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVLB</p>
</blockquote></td>
<td>PSIVLBDL</td>
<td><blockquote>
<p>PSIVLBL1</p>
</blockquote></td>
<td><blockquote>
<p>PSIVLBRP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVLTR</p>
</blockquote></td>
<td>PSIVLTR1</td>
<td><blockquote>
<p>PSIVMAN</p>
</blockquote></td>
<td><blockquote>
<p>PSIVMAN1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVOC</p>
</blockquote></td>
<td>PSIVOCDS</td>
<td><blockquote>
<p>PSIVOE</p>
</blockquote></td>
<td><blockquote>
<p>PSIVOPT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVOPT1</p>
</blockquote></td>
<td>PSIVOPT2</td>
<td><blockquote>
<p>PSIVORA</p>
</blockquote></td>
<td><blockquote>
<p>PSIVORA1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVORAL</p>
</blockquote></td>
<td>PSIVORC</td>
<td><blockquote>
<p>PSIVORC1</p>
</blockquote></td>
<td><blockquote>
<p>PSIVORC2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVORE</p>
</blockquote></td>
<td>PSIVORE1</td>
<td><blockquote>
<p>PSIVORE2</p>
</blockquote></td>
<td><blockquote>
<p>PSIVOREN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVORFA</p>
</blockquote></td>
<td>PSIVORFB</td>
<td><blockquote>
<p>PSIVORFE</p>
</blockquote></td>
<td><blockquote>
<p>PSIVORH</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVORLB</p>
</blockquote></td>
<td>PSIVORV1</td>
<td><blockquote>
<p>PSIVORV2</p>
</blockquote></td>
<td><blockquote>
<p>PSIVPAT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVPCR</p>
</blockquote></td>
<td>PSIVPCR1</td>
<td><blockquote>
<p>PSIVPGE</p>
</blockquote></td>
<td><blockquote>
<p>PSIVPR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVPRO</p>
</blockquote></td>
<td>PSIVQUI</td>
<td><blockquote>
<p>PSIVRD</p>
</blockquote></td>
<td><blockquote>
<p>PSIVRDC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVREC</p>
</blockquote></td>
<td>PSIVRNL</td>
<td><blockquote>
<p>PSIVRP</p>
</blockquote></td>
<td><blockquote>
<p>PSIVRP1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVRQ</p>
</blockquote></td>
<td>PSIVRQ1</td>
<td><blockquote>
<p>PSIVSET</p>
</blockquote></td>
<td><blockquote>
<p>PSIVSP</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PSIVSPDC</p>
</blockquote></th>
<th>PSIVUDL</th>
<th><blockquote>
<p>PSIVUTL</p>
</blockquote></th>
<th><blockquote>
<p>PSIVUTL1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSIVUWL</p>
</blockquote></td>
<td>PSIVVW1</td>
<td><blockquote>
<p>PSIVWCR</p>
</blockquote></td>
<td><blockquote>
<p>PSIVWCR1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVWL</p>
</blockquote></td>
<td>PSIVWL1</td>
<td><blockquote>
<p>PSIVWRP</p>
</blockquote></td>
<td><blockquote>
<p>PSIVXREF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVXU</p>
</blockquote></td>
<td>PSJ53P1</td>
<td><blockquote>
<p>PSJ59P5</p>
</blockquote></td>
<td><blockquote>
<p>PSJAC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJADT</p>
</blockquote></td>
<td>PSJADT0</td>
<td><blockquote>
<p>PSJADT1</p>
</blockquote></td>
<td><blockquote>
<p>PSJADT2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJALG</p>
</blockquote></td>
<td>PSJAPIDS</td>
<td><blockquote>
<p>PSJBCMA</p>
</blockquote></td>
<td><blockquote>
<p>PSJBCMA1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJBCMA2</p>
</blockquote></td>
<td>PSJBCMA3</td>
<td><blockquote>
<p>PSJBCMA4</p>
</blockquote></td>
<td><blockquote>
<p>PSJBLDOC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJCOM</p>
</blockquote></td>
<td>PSJCOM1</td>
<td><blockquote>
<p>PSJCOMR</p>
</blockquote></td>
<td><blockquote>
<p>PSJCOMV</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJDCHK</p>
</blockquote></td>
<td>PSJDCU</td>
<td><blockquote>
<p>PSJDDUT</p>
</blockquote></td>
<td><blockquote>
<p>PSJDDUT2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJDDUT3</p>
</blockquote></td>
<td>PSJDEA</td>
<td><blockquote>
<p>PSJDGAL</p>
</blockquote></td>
<td><blockquote>
<p>PSJDIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJDOSE</p>
</blockquote></td>
<td>PSJDPT</td>
<td><blockquote>
<p>PSJEEU</p>
</blockquote></td>
<td><blockquote>
<p>PSJEEU0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJENV</p>
</blockquote></td>
<td>PSJEXP</td>
<td><blockquote>
<p>PSJEXP0</p>
</blockquote></td>
<td><blockquote>
<p>PSJFTR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJGMRA</p>
</blockquote></td>
<td>PSJH1</td>
<td><blockquote>
<p>PSJHEAD</p>
</blockquote></td>
<td><blockquote>
<p>PSJHEH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJHIS</p>
</blockquote></td>
<td>PSJHL10</td>
<td><blockquote>
<p>PSJHL11</p>
</blockquote></td>
<td><blockquote>
<p>PSJHL2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJHL3</p>
</blockquote></td>
<td>PSJHL4</td>
<td><blockquote>
<p>PSJHL5</p>
</blockquote></td>
<td><blockquote>
<p>PSJHL6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJHL7</p>
</blockquote></td>
<td>PSJHL9</td>
<td><blockquote>
<p>PSJHLERR</p>
</blockquote></td>
<td><blockquote>
<p>PSJHLU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJHLV</p>
</blockquote></td>
<td>PSJHVARS</td>
<td><blockquote>
<p>PSJLIACT</p>
</blockquote></td>
<td><blockquote>
<p>PSJLIFN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJLIFNI</p>
</blockquote></td>
<td>PSJLIORD</td>
<td><blockquote>
<p>PSJLIPRF</p>
</blockquote></td>
<td><blockquote>
<p>PSJLIUTL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJLIVFD</p>
</blockquote></td>
<td>PSJLIVMD</td>
<td><blockquote>
<p>PSJLMAL</p>
</blockquote></td>
<td><blockquote>
<p>PSJLMDA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJLMGUD</p>
</blockquote></td>
<td>PSJLMHED</td>
<td><blockquote>
<p>PSJLMPRI</p>
</blockquote></td>
<td><blockquote>
<p>PSJLMPRU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJLMUDE</p>
</blockquote></td>
<td>PSJLMUT1</td>
<td><blockquote>
<p>PSJLMUT2</p>
</blockquote></td>
<td><blockquote>
<p>PSJLMUTL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJLOAD</p>
</blockquote></td>
<td>PSJLOI</td>
<td><blockquote>
<p>PSJMAI</p>
</blockquote></td>
<td><blockquote>
<p>PSJMAI1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJMDIR</p>
</blockquote></td>
<td>PSJMDIR1</td>
<td><blockquote>
<p>PSJMDWS</p>
</blockquote></td>
<td><blockquote>
<p>PSJMEDS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJMISC</p>
</blockquote></td>
<td>PSJMISC2</td>
<td><blockquote>
<p>PSJMIV</p>
</blockquote></td>
<td><blockquote>
<p>PSJMON</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJMP</p>
</blockquote></td>
<td>PSJMPEND</td>
<td><blockquote>
<p>PSJMPRT</p>
</blockquote></td>
<td><blockquote>
<p>PSJMPRTU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJMUTL</p>
</blockquote></td>
<td>PSJNTEG</td>
<td><blockquote>
<p>PSJNTEG0</p>
</blockquote></td>
<td><blockquote>
<p>PSJNTEG1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJO</p>
</blockquote></td>
<td>PSJO1</td>
<td><blockquote>
<p>PSJO2</p>
</blockquote></td>
<td><blockquote>
<p>PSJO3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJOC</p>
</blockquote></td>
<td>PSJOCDC</td>
<td><blockquote>
<p>PSJOCDI</p>
</blockquote></td>
<td><blockquote>
<p>PSJOCDS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJOCDSD</p>
</blockquote></td>
<td>PSJOCDT</td>
<td><blockquote>
<p>PSJOCERR</p>
</blockquote></td>
<td><blockquote>
<p>PSJOCOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJOCVAR</p>
</blockquote></td>
<td>PSJOE</td>
<td><blockquote>
<p>PSJOE0</p>
</blockquote></td>
<td><blockquote>
<p>PSJOE1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJOEA</p>
</blockquote></td>
<td>PSJOEA1</td>
<td><blockquote>
<p>PSJOEEW</p>
</blockquote></td>
<td><blockquote>
<p>PSJOERI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJORAPI</p>
</blockquote></td>
<td>PSJORDA</td>
<td><blockquote>
<p>PSJOREN</p>
</blockquote></td>
<td><blockquote>
<p>PSJORMA1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJORMA2</p>
</blockquote></td>
<td>PSJORMAR</td>
<td><blockquote>
<p>PSJORP2</p>
</blockquote></td>
<td><blockquote>
<p>PSJORPOE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJORRE</p>
</blockquote></td>
<td>PSJORRE1</td>
<td><blockquote>
<p>PSJORREN</p>
</blockquote></td>
<td><blockquote>
<p>PSJORRO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJORRN</p>
</blockquote></td>
<td>PSJORRN1</td>
<td><blockquote>
<p>PSJORUT2</p>
</blockquote></td>
<td><blockquote>
<p>PSJORUTL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJP</p>
</blockquote></td>
<td>PSJPATMR</td>
<td><blockquote>
<p>PSJPDIR</p>
</blockquote></td>
<td><blockquote>
<p>PSJPDV</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJPDV0</p>
</blockquote></td>
<td>PSJPDV1</td>
<td><blockquote>
<p>PSJPL0</p>
</blockquote></td>
<td><blockquote>
<p>PSJPR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJPR0</p>
</blockquote></td>
<td>PSJPST50</td>
<td><blockquote>
<p>PSJPXRM1</p>
</blockquote></td>
<td><blockquote>
<p>PSJQPR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJQUTIL</p>
</blockquote></td>
<td>PSJRXI</td>
<td><blockquote>
<p>PSJSPU</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> The following routines are not used in this version of Inpatient Medications. They were exported in the initial Kernel Installation and Distribution System (KIDS) build as Delete at Site.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PSGDCR</p>
</blockquote></th>
<th>PSGDCT0</th>
<th>PSGEXP</th>
<th><blockquote>
<p>PSGEXP0</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSGMMPST</p>
</blockquote></td>
<td>PSGOROE0</td>
<td>PSGORU</td>
<td><blockquote>
<p>PSGQOS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSIVNVO</p>
</blockquote></td>
<td>PSIVOEDO</td>
<td>PSIVOENT</td>
<td><blockquote>
<p>PSIVOEPT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSIVRD0</p>
</blockquote></td>
<td>PSIVRD0</td>
<td>PSJMAN</td>
<td><blockquote>
<p>PSJOAC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJOAC0</p>
</blockquote></td>
<td>PSJOE8</td>
<td>PSJOE81</td>
<td><blockquote>
<p>PSJOEE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJOER</p>
</blockquote></td>
<td>PSJOER0</td>
<td>PSJORA</td>
<td><blockquote>
<p>PSJORIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJUTL</p>
</blockquote></td>
<td>PSJUTL1</td>
<td>PSJUTL2</td>
<td><blockquote>
<p>PSJUTL3</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Entry points provided by the Inpatient Medications package to other packages can be found in the External Relationships section of this manual. No other routines are designated as callable from outside of this package. Additional information on other external calls and their entry points can be found on the VA Software Document Library (VDL). Under the Clinical Section select the Pharm: Inpatient Medications page and then select the "API Manual - Pharmacy Reengineering (PRE)".

### Deleting Inpatient Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Since this initial version is distributed using KIDS, the transport global is automatically deleted after the install. If the plan is to delete existing Inpatient Medications routines before loading V. 5.0, be sure not to delete PSGW\* (Ward Stock) routines. These routines are not included as part of Inpatient Medications.
- The following Inpatient Medications routines were sent with a past version of the Kernel, and are no longer needed. They can be deleted.
  - PSGZ1TSK
  - PSGZ2TSK
  - ![](psj-5-181-technical-manual-security-guide-change-pages/005.png)PSIVZTSK

> Note: It is okay if any of these routines are missing, because they are no longer used.

> Pages 25 & 26 have been removed from the manual because mapping is no longer required now that all routines reside in ROU.

> *(This page included for two-sided copying.)*

> Example: How to Print the Exported Protocols Using VA FileMan

## Health Level Seven (HL7) Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HL7 Ordering Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of HL7 data fields that will be used in transactions between Order Entry/Results Reporting (OE/RR) V. 3.0 and the Pharmacy packages. Not every data field will be used in every message.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 6%" />
<col style="width: 26%" />
<col style="width: 23%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>SEG</strong></em></th>
<th><em><strong>SEQ</strong></em></th>
<th><em><strong>FIELD NAME</strong></em></th>
<th><em><strong>EXAMPLE</strong></em></th>
<th><blockquote>
<p><em><strong>HL7 TYPE</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MSH</strong></td>
<td>1</td>
<td>Field Separator</td>
<td>|</td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Encoding Characters*</td>
<td>^~\&amp;</td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Sending Application</td>
<td>ORDER ENTRY</td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>Sending Facility</td>
<td>660</td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>Receiving Application</td>
<td>PHARMACY</td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td>Receiving Facility</td>
<td>660</td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>D/T of Message</td>
<td>199409151010</td>
<td><blockquote>
<p>timestamp</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>Message Type</td>
<td>ORM</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td><strong>PID</strong></td>
<td>3</td>
<td>Patient ID</td>
<td>5340747</td>
<td><blockquote>
<p>composite ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>Patient Name</td>
<td>PSJPATIENT1,ONE</td>
<td><blockquote>
<p>patient name</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td><strong>PV1</strong></td>
<td>2</td>
<td>Patient Class</td>
<td>I</td>
<td><blockquote>
<p>table 4</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Patient Location*</td>
<td>32^234-4</td>
<td><blockquote>
<p>user table</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>45</td>
<td>Appointment Date/Time</td>
<td>200308040800-0600</td>
<td><blockquote>
<p>timestamp</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td><strong>{ ORC</strong></td>
<td>1</td>
<td>Order Control</td>
<td>NW</td>
<td><blockquote>
<p>table 119</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Placer Order Number*</td>
<td>234123;1^OR</td>
<td><blockquote>
<p>number^application</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 6%" />
<col style="width: 24%" />
<col style="width: 28%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>SEG</strong></em></th>
<th><em><strong>SEQ</strong></em></th>
<th><em><strong>FIELD NAME</strong></em></th>
<th><blockquote>
<p><em><strong>EXAMPLE</strong></em></p>
</blockquote></th>
<th><em><strong>HL7 TYPE</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>3</td>
<td>Filler Order Number*</td>
<td><blockquote>
<p>870745^PS</p>
</blockquote></td>
<td>number^application</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>Order Status</td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td>table 38</td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>Quantity/Timing*</td>
<td><blockquote>
<p>325&amp;MG&amp;1&amp;TABLET&amp;</p>
<p>325MG&amp;638^Q1D^D14^1</p>
<p>99409151010^^R^^325M</p>
<p>G^</p>
</blockquote></td>
<td>dose^schedule^duration^star t^^priority^^text^ conjunction</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>D/T of Transaction</td>
<td><blockquote>
<p>199409151010</p>
</blockquote></td>
<td>timestamp</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>Entered by</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>composite ID</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>Verified by</td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td>composite ID</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>Ordering Provider</td>
<td><blockquote>
<p>97378</p>
</blockquote></td>
<td>composite ID</td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td>Order Effective D/T</td>
<td><blockquote>
<p>199409151010</p>
</blockquote></td>
<td>timestamp</td>
</tr>
<tr class="odd">
<td></td>
<td>16</td>
<td>Order Control Reason*</td>
<td><blockquote>
<p>E^ELECTRONICALLY ENTERED^99ORN^12^</p>
<p>Requesting Physician</p>
<p>Cancelled^99ORR</p>
</blockquote></td>
<td><p>coded element:</p>
<p>NoO Code^NoO Name^99ORN ^#^Reason</p>
<p>for Action^ 99ORR</p></td>
</tr>
<tr class="even">
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>RXO</strong></p>
</blockquote></td>
<td>1</td>
<td>Requested Give Code*</td>
<td><blockquote>
<p>^^^8^DIGOXIN</p>
<p>TAB^99PSP</p>
</blockquote></td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Requested Give Amt</td>
<td><blockquote>
<p>125</p>
</blockquote></td>
<td>numeric</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>Requested Dispense Code*</td>
<td><blockquote>
<p>576.4^DIGOXIN 0.5MG</p>
<p>TAB^99NDF^4213^DIGO XIN 0.5MG TAB^99PSD</p>
</blockquote></td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>Requested Disp Amt</td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td>numeric</td>
</tr>
<tr class="odd">
<td></td>
<td>13</td>
<td>Number of Refills</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td>numeric</td>
</tr>
<tr class="even">
<td></td>
<td>17</td>
<td>Requested Give Per</td>
<td><blockquote>
<p>D30</p>
</blockquote></td>
<td>string</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>RXE</strong></p>
</blockquote></td>
<td>1</td>
<td>Quantity/Timing*</td>
<td><blockquote>
<p>325&amp;MG&amp;1&amp;TABLET^Q</p>
<p>D^^ 199409150600^19940925</p>
<p>0600^^^325MG^</p>
</blockquote></td>
<td>dose^schedule^duration^ start^stop^priority^^ text^conjunction</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Give Code*</td>
<td><blockquote>
<p>576.4^^99NDF^21^^99PS</p>
<p>D</p>
</blockquote></td>
<td>coded element</td>
</tr>
<tr class="even">
<td></td>
<td>10</td>
<td>Dispense Amount</td>
<td><blockquote>
<p>100</p>
</blockquote></td>
<td>numeric</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>Number of Refills</td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>numeric</td>
</tr>
<tr class="even">
<td></td>
<td>22</td>
<td>Give Per Time</td>
<td><blockquote>
<p>D30</p>
</blockquote></td>
<td>string</td>
</tr>
<tr class="odd">
<td></td>
<td>23</td>
<td>Give Rate Amount</td>
<td><blockquote>
<p>125</p>
</blockquote></td>
<td>string</td>
</tr>
<tr class="even">
<td></td>
<td>24</td>
<td>Give Rate Units*</td>
<td><blockquote>
<p>^^^^ml/hr99PSU</p>
</blockquote></td>
<td>coded element</td>
</tr>
<tr class="odd">
<td></td>
<td>25</td>
<td>Give Strength</td>
<td><blockquote>
<p>325</p>
</blockquote></td>
<td>numeric</td>
</tr>
<tr class="even">
<td></td>
<td>26</td>
<td>Give Strength Units*</td>
<td><blockquote>
<p>^^^20^MG^99PSU</p>
</blockquote></td>
<td>coded element</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>{ NTE }</strong></p>
</blockquote></td>
<td>1</td>
<td>Set ID</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td>set ID</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Source of Comment</td>
<td><blockquote>
<p>P</p>
</blockquote></td>
<td>table 105</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Comment</td>
<td><blockquote>
<p>take with food</p>
</blockquote></td>
<td>formatted text</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="4"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 6%" />
<col style="width: 25%" />
<col style="width: 26%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>SEG</strong></em></th>
<th><em><strong>SEQ</strong></em></th>
<th><em><strong>FIELD NAME</strong></em></th>
<th><em><strong>EXAMPLE</strong></em></th>
<th><blockquote>
<p><em><strong>HL7 TYPE</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>{ RXR }</strong></td>
<td>1</td>
<td>Route*</td>
<td>^^^23^ORAL^99PSR</td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td><strong>{ RXC }</strong></td>
<td>1</td>
<td>RX Component Type</td>
<td>B</td>
<td><blockquote>
<p>table 166</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Component Code*</td>
<td><p>^^^4132^D5 W</p>
<p>NS^99PSD</p></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Component Amount</td>
<td>1</td>
<td><blockquote>
<p>numeric</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>Component Units*</td>
<td>^^^PSIV-1^ML^99OTH</td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>Additive Frequency</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>{ OBX }</strong></td>
<td>1</td>
<td>Set ID</td>
<td>1</td>
<td><blockquote>
<p>set ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Value Type</td>
<td>TX</td>
<td><blockquote>
<p>table 125</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Observation ID</td>
<td><p>^^^38^Critical Drug-Drug</p>
<p>interaction^99OCX</p></td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>Observation Value</td>
<td><p>Critical drug-drug</p>
<p>interaction Aspirin- Warfarin</p></td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>14</td>
<td>Date/time of Observation</td>
<td>199606130813</td>
<td><blockquote>
<p>timestamp</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>16</td>
<td>Observer</td>
<td>10</td>
<td><blockquote>
<p>composite ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>NTE</strong></p>
</blockquote></td>
<td>1</td>
<td>Set ID</td>
<td>1</td>
<td><blockquote>
<p>set ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Source of Comment</td>
<td>P</td>
<td><blockquote>
<p>table 105</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Comment</td>
<td>Worth the risk</td>
<td><blockquote>
<p>formatted text</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>ZRX</strong></p>
</blockquote></td>
<td>1</td>
<td>Previous Order #</td>
<td>2355</td>
<td><blockquote>
<p>numeric</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Nature of Order</td>
<td>W</td>
<td><blockquote>
<p>set of codes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Reason Order Created</td>
<td>N</td>
<td><blockquote>
<p>set of codes</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>Routing</td>
<td>W</td>
<td><blockquote>
<p>set of codes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>Current User*</td>
<td>DUZ^NAME^99NP</td>
<td><blockquote>
<p>composite ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td>IV Identifier</td>
<td>IV</td>
<td><blockquote>
<p>string</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>ZSC</strong></p>
</blockquote></td>
<td>1</td>
<td>Service Connected</td>
<td>SC</td>
<td><blockquote>
<p>coded element</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>}</strong></td>
<td colspan="4"></td>
</tr>
</tbody>
</table>

> \*- Fields marked with an asterisk require special escaping characters in order to send and receive the correct data contained in an HL7 message. See Special Escaping Characters for details.

> ![](psj-5-181-technical-manual-security-guide-change-pages/006.png)\*\*-RXC Segment Field 5 "Additive Frequency" applies only to additives used to specify IV bag information.

> Note: The following are definitions of some of the data fields under the FIELD NAME column.

> SENDING APPLICATION is the name of the VistA package generating the message; RECEIVING APPLICATION is the name of the VistA package that is the intended recipient of the message. SENDING FACILITY and RECEIVING FACILITY are the station numbers.

> PATIENT ID is the patient IEN in the PATIENT file (#2).

> PATIENT LOCATION, for an inpatient, is Hospital Location IEN^Room^Bed. For an

> outpatient, it is the Hospital Location IEN. In both cases, this is the location from which the order is being placed.

> APPOINTMENT DATE/TIME is for Inpatient Medication orders for Outpatients. This is the appointment date/time that this order is associated with.

> PLACER ORDER NUMBER is the OE/RR order number. FILLER ORDER NUMBER is the Pharmacy order number.

> ORDERING PROVIDER is the IEN in the NEW PERSON file (#200).

> ORDER STATUS identifies the current status of the order. Codes from table 38, located in HL7

> V. 2.3, that will be used, and those added, include:

> IP = pending

> CM = finished/verified by pharmacist (active) DC = discontinued

> RP = replaced HD = on hold ZE = expired

> ZS = suspended (active) ZU = un-suspended (active) ZX = unreleased

> ZZ = renewed

> QUANTITY/TIMING contains the give amount, schedule, duration, start and stop times, and priority for the order, as well as the actual text of the dose ordered. The quantity field is delimited with '&' as:

> Total Dose & Unit & Give Amount & Unit & Text & Dispense Drug

> By using the quantity and conjunction fields, orders with multiple schedules may be sent. For outpatient orders, multiple schedules will be sent delimited by '~' and combined into a single signature (SIG); an inpatient order with multiple schedules will be sent as separate orders for each schedule. The conjunction will be S (then), A (and), or X (except).

> REQUESTED GIVE CODE identifies a combination of the drug and dosage form in the format of a universal service ID. The last three pieces (alternate components) are used to identify an entry in the PHARMACY ORDERABLE ITEM file (#50.7).

> PROVIDER'S PHARMACY INSTRUCTIONS are text instructions from the provider to the pharmacist; these are passed in an NTE segment following a RXO segment with an ID of 6.

> PROVIDER'S ADMINISTRATION INSTRUCTIONS are Outpatient Pharmacy's "Patient Instructions" if the provider wishes to include them with the order; these are passed in an NTE segment following a RXO or RXE segment with an ID of 7.

> REQUESTED DISPENSE CODE identifies the drug ordered as it maps to the National Drug File (NDF) and to the local drug file. The first three pieces identify a VA Product Name entry in the NDF, the last three pieces (alternate components) are used to identify an entry in the DRUG file (#50). The 'code' field (piece 1) of the NDF portion uses two numbers, separated by a period, to identify VA Generic Name and VA Product Name. The fourth piece uses the IEN of the DRUG file (#50) to identify a dispensed drug. This field will be blank if a pharmacy orderable item, but no dispensed drug, was selected.

> REQUESTED DISPENSE AMOUNT is used to pass the amount that was entered in the QUANTITY field (#7) for an outpatient order.

> REQUESTED GIVE PER is used to pass the amount that was entered in the DAYS SUPPLY field (#8) for an outpatient order.

> ROUTE uses the IEN of the MEDICATION ROUTES file (#51.1) to identify a route. To truly be HL7 compatible, the MEDICATION ROUTES file (#51.1) should be mapped to the four route fields identified in HL7 V. 2.3 Section 4.8.3.

> In the case of an order for IV Fluids, the REQUESTED GIVE CODE will be PS-1^IV^99OTH. This will indicate that the order is for IV fluids and the solutions and additives will be found in the RXC segment.

> The RXC segment may repeat, once for each solution and additive in an IV order. The RX COMPONENT TYPE is B for a solution and A for an additive.

> The COMPONENT CODE identifies additives and solutions by their IEN in the PHARMACY ORDERABLE ITEM file (#50.7).

> COMPONENT UNITS uses 99OTH codes to map the IV Additive units.

> The OBX segment is used if there was a positive order check that the physician chose to override.

> The special code, 38^Critical Drug-drug interaction^99OCX, is used to identify this OBX segment in the OBSERVATION ID data field, and the OBSERVATION VALUE data field contains the actual order check message displayed to the provider; the OBX segment will be followed by a NTE segment, if an override reason was entered.

> A Z-segment (ZRX) is used to pass additional data on new orders:

> PREVIOUS ORDER NUMBER identifies the order being edited or renewed by the current order; for front-door orders this will be the Pharmacy order number, and for back-door orders it will be the Order Entry order number.

> NATURE OF ORDER may be (W)ritten, (V)erbal, (P)honed, (S)ervice Correction, (X) Rejected, (D)uplicate, Pol(I)cy, (A)uto, or (E)lectronically entered.

> REASON the order was created may be (N)ew, (E)dit, or (R)enew. ROUTING may be (W)indow, (M)ail, or (C)linic.

> CURRENT USER identifies the user currently on the system performing the actions on the order.

> IV IDENTIFIER will indicate a fluid (IV), Total Parenteral Nutrition (TPN), or IV med ("").

> A Z-segment (ZSC) is used for service connection, as this must be at the individual order level; values may be either SC or NSC.

### Order Event Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following tables identify the HL7 data fields that are passed in each kind of event associated with OE/RR. For each event there is an order control code and a set of data fields listed. For any given event; however, some of the data fields may be empty (provider instructions, for example). Pharmacy may wish to send additional data fields in a RXE segment.

> The protocols identified in the tables use OE/RR name spacing conventions. The messages sent by OE/RR will use the OR name spaced protocols indicated. Individual packages may use whatever protocol names they wish.

### Front Door - Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 28%" />
<col style="width: 23%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em><strong>Action</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Request from OE/RR</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Pharmacy accepts</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Pharmacy rejects</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Protocol</strong></p>
</blockquote></td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
<td><blockquote>
<p>PS EVSEND OR</p>
</blockquote></td>
<td><blockquote>
<p>PS EVSEND OR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Order Control</strong></p>
</blockquote></td>
<td><blockquote>
<p>NW (new order)</p>
<p>XO (change)</p>
</blockquote></td>
<td><blockquote>
<p>OK (accepted)</p>
<p>XR (new order)</p>
</blockquote></td>
<td><blockquote>
<p>UA (unable to accept)</p>
<p>UX (unable to change)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HL7 Fields</strong></p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,7,9,10,12,15,16</p>
<p>RXO: 1,10</p>
<p>NTE: 1,2,3</p>
<p>RXR: 1</p>
<p>OBX: 1,2,3,5,14,16</p>
<p>ZRX: 1,2,3</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,12,15,16</p>
<p>RXE: 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Protocol</strong></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Order Control</strong></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ZV (verified)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 27%" />
<col style="width: 24%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em><strong>Action</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Request from OE/RR</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Pharmacy accepts</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Pharmacy rejects</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>HL7 Fields</strong></p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3,19</p>
<p>ORC: 1,2,3,11,15</p>
</blockquote></td>
<td><blockquote>
<p>There is no return event.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Protocol</strong></p>
</blockquote></td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
<td><blockquote>
<p>PS EVSEND OR</p>
</blockquote></td>
<td><blockquote>
<p>PS EVSEND OR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Order Control</strong></p>
</blockquote></td>
<td><blockquote>
<p>CA (cancel)</p>
<p>DC (discontinue) HD (hold)</p>
<p>RL (release)</p>
<p>SS (send status)</p>
</blockquote></td>
<td><blockquote>
<p>CR (cancelled) DR (discontinued) HR (held)</p>
<p>OR (released)</p>
<p>SC (status update)</p>
</blockquote></td>
<td><blockquote>
<p>UC (unable to cancel) UD (unable to dc) UH (unable to hold)</p>
<p>UR (unable to release)</p>
<p>DE (data errors)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HL7 Fields</strong></p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3,19</p>
<p>ORC: 1,2,3,10,12,15,16</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5</p>
<p>RXE: 1</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,16</p>
</blockquote></td>
</tr>
</tbody>
</table>

> OE/RR will use CA to cancel orders, which have not been finished by Pharmacy; DC will be used for orders that have been finished.

### Example: Digoxin .125 mg QAM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Order

> MSH\|^~\\\|ORDER ENTRY\|13000\|PHARMACY\|13000\|20080304165 101-0600\|\|ORM

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE

> PV1\|\|I\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| ORC\|NW\|12613;1^OR\|\|\|\|\|2&MG&1&TABLET&2 MG&58^BID&01-13

> ^^200803050100-0600^^R^C^2 MG^~\|\|200803041650- 0600\|11884\|\|11884\|\|\|20080304165101

> -0600\|I^POLICY^99ORN^^^

> RXO\|^^^81^BIPERIDEN TAB ^99PSP\|\|\|\|\|\|\|\|\|785.4409^^99ND F^58^^99PSD

> RXR\|^^^1^ORAL (BY MOUTH)^99PSR

> ZRX\|\|I\|N

#### Verified by Nursing staff

> MSH\|^~\\\|ORDER ENTRY\|13000\|PHARMACY\|13000\|20080304165 253-0600\|\|ORM

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE

> PV1\|\|I\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| ORC\|ZV\|12613^OR\|2929P^PS\|\|\|\|\|\|\|\|11884\|\|\|\|200803041652 53-0600

#### Discontinue Order

> MSH\|^~\\\|ORDER ENTRY\|13000\|PHARMACY\|13000\|20080304165 754-0600\|\|ORM

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE

> PV1\|\|I\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| ORC\|DC\|12614;2^OR\|54U^PS\|\|\|\|\|\|\|11884\|\|11884\|\|\|2008030 4165754-0600\|I^POLICY^99ORN^14^Requesting Physician Cancelled^99ORR

# External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Packages Needed to Run Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Inpatient Medications package requires the minimum version, stated on the following external packages, to run effectively:

> <u>PACKAGE</u> <u>MINIMUM VERSION NEEDED</u>

<table>
<colgroup>
<col style="width: 87%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>Kernel</th>
<th><blockquote>
<p>8.0</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA FileMan</td>
<td><blockquote>
<p>22.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MailMan</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PIMS</td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CPRS</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Outpatient Pharmacy</td>
<td><blockquote>
<p>7.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PDM</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Dietetics</td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Bar Code Medication Administration</td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HealtheVet Web Services Client (HWSC)</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VistALink</td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Unit Dose Medications and Ward Stock

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Inpatient Medications package also has a tie to the Automatic Replenishment/Ward Stock package so that if the site is running the Automatic Replenishment/Ward Stock package, the Inpatient Medications package will know which items in the DRUG file (#50) are ward stock items for each ward. The tie is a cross-reference under the PHARMACY AOU STOCK file (#58.1).

## Unit Dose Medications and Drug Accountability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Inpatient Medications package also has a tie to the Drug Accountability package so that if the site is running the Drug Accountability package, the Inpatient Medications package will know which items in the DRUG file (#50) are ward stock items for each ward. This cross- reference is the link between the Controlled Substances package and the Unit Dose package for determining ward-stocked drugs.

## Calls Made by Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following external calls are supported via inter-package agreements:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ROUTINE</strong></p>
</blockquote></th>
<th><strong>ENTRY POINTS USED</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ECXUD1</p>
</blockquote></td>
<td>^ECXUD1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ECXPIV1</p>
</blockquote></td>
<td>^ECXPIV1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMRVUTL</p>
</blockquote></td>
<td>EN6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMRADPT</p>
</blockquote></td>
<td>EN1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMRAOR</p>
</blockquote></td>
<td>$$ORCHK</td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMRAOR2</p>
</blockquote></td>
<td>EN1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMRAPEM0</p>
</blockquote></td>
<td>EN2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>OR3CONV</p>
</blockquote></td>
<td>OTF</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORCONV3</p>
</blockquote></td>
<td>PSJQOS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORERR</p>
</blockquote></td>
<td>EN</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OROCAPI</p>
</blockquote></td>
<td>$$AOC, $$DOC, $$GOC</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORUTL</p>
</blockquote></td>
<td>READ</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ORX1</p>
</blockquote></td>
<td>NA</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORX2</p>
</blockquote></td>
<td>LK,ULK</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSAPSI5</p>
</blockquote></td>
<td>EN</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSBIPM</p>
</blockquote></td>
<td>EN, MOB, MOBR</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSDSAPD</p>
</blockquote></td>
<td>$$DOSE, $$DRT</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSDSAPI</p>
</blockquote></td>
<td><p>$$BSA, $$DS, $$EXMT, $$FRQ, $$MRT,</p>
<p>$$UNIT, $$SUP</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSFDBRT</p>
</blockquote></td>
<td>GROUTE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSHLSCH</p>
</blockquote></td>
<td>EN</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSODDPR4</p>
</blockquote></td>
<td>BLD</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSODRDU2</p>
</blockquote></td>
<td>EN</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDROUT2</p>
</blockquote></td>
<td>DIS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDAMA203</p>
</blockquote></td>
<td>SDIMO</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VADPT</p>
</blockquote></td>
<td>IN5, INP, PID, SDA</td>
</tr>
</tbody>
</table>

## Introduction to Integration Agreements and Entry Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following integration agreements and entry points are provided for the associated packages; only those packages listed can use these integration agreements and entry points. If there are any questions, please contact the Birmingham Health System Design & Development (HSD&D) Field Office.

> 2945 NAME: Use of calls in PSIVSP

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSIVSP

> 3143 NAME: DBIA3143

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: CLINICAL REMINDERS Salt Lake City

> ROUTINE: PSJORAPI

> 3167 NAME: 3167

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSJORPOE

> 3243 NAME: Active Flag

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSJORREN

> 3320 NAME: UPDATE BCMA STATUS INFORMATION

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

> ROUTINE: PSJBCMA3

> 3416 NAME: DBIA3416

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

> ROUTINE: PSJBCMA4

> 3598 NAME: DBIA3598

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSJOERI

> 3836 NAME: PSJPXRM1

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: CLINICAL REMINDERS Salt Lake City

> ROUTINE: PSJPXRM1

> 3876 NAME: PSJBCBU

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

> ROUTINE: PSJBCBU

> 4074 NAME: OR Call to PSJORUT2

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSJORUT2

> 4264 NAME: PDM ACCESS TO PSJXRFS

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

> ROUTINE: PSJXRFS

> 4265 NAME: PDM ACCESS TO PSJXRFK

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

> ROUTINE: PSJXRFK

> 4537 NAME: PSJ53P1

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE:

> ROUTINE: PSJ53P1

> 4580 NAME: VALIDATE DOW SCHEDULES

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

> ROUTINE: PSIVUTL

> 4819 NAME: PSJ59P5

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE:

> ROUTINE: PSJ59P5

> 5001 NAME: Pointing to the PHARMACY QUICK ORDER (#57.1) File

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE:

> USUAGE: Supported

> 5057 NAME: BCMA LAST ACTION

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

> DRUG ACCOUNTABILITY ROUTINE: PSJUTL2

> 5058 NAME: ALLERIES ARRAY

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

> ROUTINE: PSJMUTL

> 5306 NAME: PSJBLDOC

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

> ROUTINE: PSJBLDOC

> 5385 NAME: Dosing Checks for IVs

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSJAPIDS

> Example: How to Print DBIA Information from FORUM

> Select FORUM Primary Menu Option: DBA

> Select DBA Option: INTEGRATIon Agreements Menu

> Select Integration Agreements Menu Option: INQUIRe

> Select INTEGRATION REFERENCES: DBIA296 296 INPATIENT MEDICATIONS DBIA296

> DEVICE: *\[Select Print Device\]*

> PS(50.8,

> INTEGRATION REFERENCE INQUIRY \#296 OCT 1,1996 10:24 PAGE 1

> 296 NAME: DBIA296

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 50.8 ROOT: PS(50.8, DESCRIPTION: TYPE: File

> Outpatient Pharmacy 6.0v will be printing a management report. In order to complete the report, we need to read ^PS(50.8 (IV STATS FILE). We are reporting the outpatient ward's number of dispensed units, average cost of the dispensed units, and the total costs of the dispensed units.

> To obtain this data, we need to read the 0 node in subfile 50.804, the Average Drug Cost Per Unit field (#4) on the 0 node piece 5 in subfile 50.805, the Dispensed Units (Ward) field (#2) on the 0 node piece 2 in the subfile 50.808, and the B cross-reference in subfile 50.808.

> GLOBAL MAP DATA DICTIONARY \#50.8 -- IV STATS FILE STORED IN ^PS(50.8, SITE: BIRMINGHAM ISC

> ^PS(50.8 D0,2,D1,1,0)=^50.804P^^ (#1) WARD ^PS(50.8,D0,2,D1,2,D2,0)=^^^^ (#4) AVERAGE DRUG COST PER UNIT \[5N\] ^PS(50.8,D0,2,D1,2,D2,3,D3,0)=^ (#2) DISPENSED UNITS (WARD) \[2N\] ^

> *\<This page left blank for two-sided copying\>*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Action Prompts There are three types of Inpatient Medications "Action" prompts that occur during order entry: ListMan, Patient/Order, and Hidden action prompts.

### ListMan Action Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient/Order Action Prompts
> \+ Next Screen
> \- Previous Screen
> UP Up a Line
> DN Down a Line
> \> Shift View to Right
> \< Shift View to Left
> FS First screen
> LS Last Screen
> GO Go to Page
> RD Re Display Screen
> PS Print Screen
> PT Print List
> SL Search List
> Q Quit
> ADPL Auto Display (on/off)
> PU Patient Record Updates
> DA Detailed Allergy/ADR List
> VP View Profile
> NO New Orders Entry
> IN Intervention Menu
> PI Patient Information
> SO Select Order
> DC Discontinue
> ED Edit
> FL Flag
> VF Verify
> HD Hold

### Patient/Order Action Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> (continued) RN Renew
> AL Activity Logs
> OC On Call
> NL Print New IV Labels
> RL Reprint IV Labels
> RC Recycled IV
> DT Destroyed IV
> CA Cancelled IV

### Hidden Action Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> LBL Label Patient/Report
> JP Jump to a Patient
> OTH Other Pharmacy Options MAR MAR Menu
> DC Speed Discontinue
> RN Speed Renew
> SF Speed Finish
> SV Speed Verify
> CO Copy
> N Mark Not to be Given
> I Mark Incomplete
> DIN Drug Restr/Guide
> Active Order Any order which has not expired or been discontinued. Active orders also include any orders that are on hold or on call.
> Activity Reason Log The complete list of all activity related to a patient order. The log contains the action taken, the date of the action, and the user who took the action.
> Activity Ruler The activity ruler provides a visual representation of the relationship between manufacturing times, doses due and order start times. The intent is to provide the on- the-floor user with a means of tracking activity in the IV room and determining when to call for doses before the normal delivery. The activity ruler can be enabled or disabled under the *SIte Parameters (IV)* \[PSJI SITE PARAMETERS\] option.
> Additive A drug that is added to an IV solution for the purpose of parenteral administration. An additive can be an electrolyte, a vitamin or other nutrient, or an antibiotic. Only electrolyte or multivitamin type additives can be entered as IV fluid additives in CPRS.
> ADMINISTRATION SCHEDULE File \#51.1. This file contains administration
> File schedule names and standard dosage administration times. The name is a common abbreviation for an administration schedule type (e.g., QID, Q4H, PRN). The administration time entered is in military time, with each time separated from the next by a dash, and times listed in ascending order.
> Administering Teams Nursing teams used in the administration of medication
> to the patients. There can be a number of teams assigned to take care of one ward, with specific rooms and beds assigned to each team.
> Admixture An admixture is a type of intravenously administered medication comprised of any number of additives (including zero) in one solution. It is given at a specified flow rate; when one bottle or bag is empty, another is hung.
> APSP INTERVENTION File File \#9009032.4. This file is used to enter pharmacy
> interventions. Interventions in this file are records of occurrences where the pharmacist had to take some sort of action involving a particular prescription or order. A record would record the provider involved, why an intervention was necessary, what action was taken by the pharmacists, etc.
> Average Unit Drug Cost The total drug cost divided by the total number of units
> of measurement.
> BCMA A VistA computer software package named Bar Code Medication Administration. This package validates medications against active orders prior to being administered to the patient.
> Chemotherapy Chemotherapy is the treatment or prevention of cancer with chemical agents. The chemotherapy IV type administration can be a syringe, admixture, or a piggyback. Once the subtype (syringe, piggyback, etc.) is selected, the order entry follows the same procedure as the type that corresponds to the selected subtype (e.g., piggyback type of chemotherapy follows the same entry procedure as regular piggyback IV).
> Chemotherapy "Admixture" The Chemotherapy "Admixture" IV type follows the
> same order entry procedure as the regular admixture IV type. This type is in use when the level of toxicity of the chemotherapy drug is high and is to be administered continuously over an extended period of time (e.g., seven days).
> Chemotherapy "Piggyback" The Chemotherapy "Piggyback" IV type follows the
> same order entry procedure as the regular piggyback IV type. This type of chemotherapy is in use when the chemotherapy drug does not have time constraints on how fast it must be infused into the patient. These types are normally administered over a 30 - 60 minute interval.
> Chemotherapy "Syringe" The Chemotherapy "Syringe" IV type follows the same
> order entry procedure as the regular syringe IV type. Its administration may be continuous or intermittent. The pharmacist selects the type when the level of toxicity of the chemotherapy drug is low and needs to be infused directly into the patient within a short time interval (usually 1-2 minutes).
> Clinic Group A clinic group is a combination of outpatient clinics that have been defined as a group within Inpatient Medications to facilitate processing of orders.
> CLINIC DEFINITION File File \#53.46. This file is used in conjunction with
> Inpatient Medications for Outpatients (IMO) to give the user the ability to define, by clinic, default stop dates, whether to auto-dc IMO orders, and whether to send IMO orders to BCMA.
> CLINIC GROUP File File \#57.8. This file is used to provide grouping of
> clinics for the Non-Verified Pending option and miscellaneous reports.
> Continuous Syringe A syringe type of IV that is administered continuously to the patient, similar to a hyperal IV type. This type of syringe is commonly used on outpatients and administered automatically by an infusion pump.
> Coverage Times The start and end of coverage period designates administration times covered by a manufacturing run. There must be a coverage period for all IV types: admixtures and primaries, piggybacks, hyperals, syringes, and chemotherapy. For one type, admixtures for example, the user might define two coverage periods; one from 1200 to 0259 and another from 0300 to 1159 (this would mean that the user has two manufacturing times for admixtures).
> CPRS A VistA computer software package called Computerized Patient Record Systems. CPRS is an application in VistA that allows the user to enter all necessary orders for a patient in different packages from a single application. All pending orders that appear in the Unit Dose and IV Medications modules are initially entered through the CPRS package.
> Cumulative Doses The number of IV doses actually administered, which equals the total number of bags dispensed less any recycled, destroyed, or canceled bags.
> DATUP Functionality that allows the Pharmacy Enterprise Customization System (PECS) to send out custom and standard commercial-off-the-shelf (COTS) vendor database changes to update the two centralized databases at Austin and Martinsburg.
> Default Answer The most common answer, predefined by the system to save time and keystrokes for the user. The default
> answer appears before the two slash marks (//) and can be selected by the user by pressing \<Enter\>.
> Delivery Times The time(s) when IV orders are delivered to the wards.
> Dispense Drug The Dispense Drug name has the strength attached to it (e.g., Acetaminophen 325 mg). The name alone without strength attached is the Orderable Item name.
> Dosage Ordered After the user has selected the drug during order entry, the dosage ordered prompt is displayed.
> DRUG ELECTROLYTES File File \#50.4. This file contains the names of
> anions/cations, and their concentration units.
> DRUG File File \#50. This file holds the information related to each drug that can be used to fill a prescription.
> Electrolyte An additive that disassociates into ions (charged particles) when placed in solution.
> Entry By The name of the user who entered the Unit Dose or IV order into the computer.
> Hospital Supplied Self Med Self med which is to be supplied by the Medical
> Center's pharmacy. Hospital supplied self med is only prompted for if the user answers Yes to the SELF MED prompt during order entry.
> Hyperalimentation (Hyperal) Long term feeding of a protein-carbohydrate solution.
> Electrolytes, fats, trace elements, and vitamins can be added. Since this solution generally provides all necessary nutrients, it is commonly referred to as Total Parenteral Nutrition (TPN). A hyperal is composed of many additives in two or more solutions. When the labels print, they show the individual electrolytes in the hyperal order.
> Infusion Rate The designated rate of flow of IV fluids into the patient.
> INPATIENT USER File \#53.45. This file is used to tailor various aspects
> PARAMETERS File of the Inpatient Medications package with regards to specific users. This file also contains fields that are used as temporary storage of data during order entry/edit.
> INPATIENT WARD File \#59.6. This file is used to tailor various aspects
> PARAMETERS File of the Inpatient Medications package with regards to specific wards.
> Intermittent Syringe A syringe type of IV that is administered periodically to
> the patient according to an administration schedule.
> Internal Order Number The number on the top left corner of the label of an IV
> bag in brackets (\[ \]). This number can be used to speed up the entry of returns and destroyed IV bags.
> IV ADDITIVES File File \#52.6. This file contains drugs that are used as additives in the IV room. Data entered includes drug generic name, print name, drug information, synonym(s), dispensing units, cost per unit, days for IV order, usual IV schedule, administration times, electrolytes, and quick code information.
> IV CATEGORY File File \#50.2. This file allows the user to create categories
> of drugs in order to run "tailor-made" IV cost reports for specific user-defined categories of drugs. The user can group drugs into categories.
> IV Duration The duration of an order may be entered in CPRS at the IV DURATION OR TOTAL VOLUME field in the IV
> Fluids order dialog. The duration may be specified in terms of volume (liters or milliliters), or time (hours or days). Inpatient Medications uses this value to calculate a default stop date/time for the order at the time the order is finished.
> IV Label Action A prompt, requesting action on an IV label, in the form of "Action ( )", where the valid codes are shown in the parentheses. The following codes are valid:
> P – Print a specified number of labels now. B – Bypass any more actions.
> S – Suspend a specified number of labels for the IV room to print on demand.
> IV Room Name The name identifying an IV distribution area.
> IV SOLUTIONS File File \#52.7. This file contains drugs that are used as primary solutions in the IV room. The solution must already exist in the DRUG file (#50) to be selected. Data in this file includes: drug generic name, print name, status, drug information, synonym(s), volume, and electrolytes.
> IV STATS File File \#50.8. This file contains information concerning the IV workload of the pharmacy. This file is updated each time the *COmpile IV Statistics* option is run and the data stored is used as the basis for the AMIS (IV) report.
> Label Device The device, identified by the user, on which computer- generated labels will be printed.
> Local Possible Dosages Free-text dosages that are associated with drugs that do
> not meet all of the criteria for Possible Dosages.
> LVP Large Volume Parenteral — Admixture. A solution intended for continuous parenteral infusion, administered as a vehicle for additive(s) or for the pharmacological effect of the solution itself. It is comprised of any number of additives, including zero, in one solution. An LVP runs continuously, with another bag hung when one bottle or bag is empty.
> Manufacturing Times The time(s) that designate(s) the general time when the
> manufacturing list will be run and IV orders prepared. This field in the *SIte Parameters (IV)* \[PSJI SITE PARAMETERS\] option (IV ROOM file (#59.5)) is for documentation only and does not affect IV processing.
> MEDICATION ADMINISTERING File \#57.7. This file contains wards, the teams used in
> TEAM File the administration of medication to that ward and the rooms/beds assigned to that team.
> MEDICATION INSTRUCTION File File \#51.2. This file is used by Unit Dose and
> Outpatient Pharmacy. It contains the medication instruction name, expansion, and intended use.
> MEDICATION ROUTES File File \#51.2. This file contains medication route names.
> The user can enter an abbreviation for each route to be used at their site. The abbreviation will most likely be the Latin abbreviation for the term.
> Medication Routes/ Route by which medication is administered
> Abbreviations (e.g., oral). The MEDICATION ROUTES file (#51.2) contains the routes and abbreviations, which are selected by each VAMC. The abbreviation cannot be longer than five characters to fit on labels and the MAR. The user can add new routes and abbreviations as appropriate.
> MOCHA Medication Order Check Healthcare Application.
> Non-Formulary Drugs The medications that are defined as commercially
> available drug products not included in the VA National Formulary.
> Non-Verified Orders Any order that has been entered in the Unit Dose or IV
> Medications module that has not been verified (made active) by a nurse and/or pharmacist. Ward staff may not verify a non-verified order.
> Orderable Item An Orderable Item name has no strength attached to it (e.g., Acetaminophen). The name with a strength attached to it is the Dispense Drug name (e.g., Acetaminophen 325mg).
> Order Sets An Order Set is a set of N pre-written orders. (N indicates the number of orders in an Order Set is variable.) Order Sets are used to expedite order entry for drugs that are dispensed to all patients in certain medical practices and procedures.
> Order View Computer option that allows the user to view detailed information related to one specific order of a patient. The order view provides basic patient information and identification of the order variables.
> Parenteral Introduced by means other than by way of the digestive track.
> Patient Profile A listing of a patient's active and non-active Unit Dose and IV orders. The patient profile also includes basic patient information, including the patient's name, social security number, date of birth, diagnosis, ward location, date of admission, reactions, and any pertinent remarks.
> PECS Pharmacy Enterprise Customization System. A Graphical User Interface (GUI) web-based application used to research, update via DATUP, maintain, and report VA customizations of the commercial-off-the- shelf (COTS) vendor database used to perform Pharmacy order checks such as drug-drug interactions, duplicate therapy, and dosing.
> Pending Order A pending order is one that has been entered by a provider through CPRS without Pharmacy or Nursing finishing the order. Once Pharmacy or Nursing has finished and verified the order, it will become active.
> PEPS Pharmacy Enterprise Product Services. A suite of services that includes Outpatient and Inpatient services.
> PHARMACY SYSTEM File File \#59.7. This file contains data that pertains to the
> entire Pharmacy system of a medical center, and not to any one site or division.
> Piggyback Small volume parenteral solution for intermittent infusion. A piggyback is comprised of any number of additives, including zero, and one solution; the mixture is made in a small bag. The piggyback is given on a schedule (e.g., Q6H). Once the medication flows in, the piggyback is removed; another is not hung until the administration schedule calls for it.
> Possible Dosages Dosages that have a numeric dosage and numeric dispense units per dose appropriate for administration. For a drug to have possible dosages, it must be a single ingredient product that is matched to the VA PRODUCT file (#50.68). The VA PRODUCT file
> (#50.68) entry must have a numeric strength and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.
> Pre-Exchange Units The number of actual units required for this order until the next cart exchange.
> Primary Solution A solution, usually an LVP, administered as a vehicle for additive(s) or for the pharmacological effect of the solution itself. Infusion is generally continuous. An
> LVP or piggyback has only one solution (primary solution). A hyperal can have one or more solutions.
> Print Name Drug generic name, as it is to appear on pertinent IV output, such as labels and reports. Volume or Strength is not part of the print name.
> Print Name{2} Field used to record the additives contained in a commercially purchased premixed solution.
> Profile The patient profile shows a patient's orders. The Long profile includes all the patient's orders, sorted by status: active, non-verified, pending, and non-active. The Short profile will exclude the patient's discontinued and expired orders.
> Prompt A point at which the system questions the user and waits for a response.
> Provider Another term for the physician involved in the prescription of an IV or Unit Dose order for a patient.
> PSJI MGR The name of the *key* that allows access to the supervisor functions necessary to run the IV medications software. Usually given to the Inpatient package coordinator.
> PSJI PHARM TECH The name of the *key* that must be assigned to pharmacy
> technicians using the IV Medications module. This key allows the technician to finish IV orders, but not verify them.
> PSJI PURGE The key that must be assigned to individuals allowed to purge expired IV orders. This person will most likely be the IV application coordinator.
> PSJI RNFINISH The name of the *key* that is given to a user to allow the finishing of IV orders. This user must also be a holder of the PSJ RNURSE key.
> PSJI USR1 The primary menu option that may be assigned to nurses.
> PSJI USR2 The primary menu option that may be assigned to technicians.
> PSJU MGR The name of the *primary menu option* and of the *key* that must be assigned to the pharmacy package coordinators and supervisors using the Unit Dose Medications module.
> PSJU PL The name of the *key* that must be assigned to anyone using the *Pick List Menu* options.
> PSJ PHARM TECH The name of the *key* that must be assigned to pharmacy
> technicians using the Unit Dose Medications module.
> PSJ RNFINISH The name of the *key* that is given to a user to allow the finishing of a Unit Dose order. This user must also be a holder of the PSJ RNURSE key.
> PSJ RNURSE The name of the *key* that must be assigned to nurses using the Unit Dose Medications module.
> PSJ RPHARM The name of the *key* that must be assigned to a pharmacist to use the Unit Dose Medications module. If the package coordinator is also a pharmacist he/she must also be given this key.
> PSJ STAT NOW ACTIVE A mail group that notifies subscribers when a pending
> ORDER Mail Group STAT or NOW order is made active.
> PSJ STAT NOW PENDING A mail group that notifies subscribers when a pending
> ORDER Mail Group STAT or NOW order has been received from CPRS.
> Quick Code An abbreviated form of the drug generic name (from one to ten characters) for IV orders. One of the three drug fields on which lookup is done to locate a drug. Print name and synonym are the other two. Use of quick codes will speed up order entry, etc.
> Report Device The device, identified by the user, on which computer- generated reports selected by the user will be printed.
> Schedule The frequency of administration of a medication (e.g., QID, QDAILY, QAM, STAT, Q4H).
> Schedule Type Codes include: O - one time (i.e., STAT - only once), P
> \- PRN (as needed; no set administration times). C- continuous (given continuously for the life of the order; usually with set administration times). R - fill on request (used for items that are not automatically put in the cart - but are filled on the nurse's request. These can be multidose items (e.g., eye wash, kept for use by one patient and is filled on request when the supply is exhausted). And OC - on call (one time with no
> specific time to be given, i.e., 1/2 hour before surgery).
> Self Med Medication that is to be administered by the patient to himself.
> Standard Schedule Standard medication administration schedules stored in the ADMINISTRATION SCHEDULE file (#51.1).
> Start Date/Time The date and time an order is to begin.
> STAT and NOW Order Notification Sends a text message to subscribers of the PSJ STAT
> NOW mail groups when a pending STAT or NOW order has been received from CPRS or has been verified and made active.
> Status A - active, E - expired, R - renewed (or reinstated), D - discontinued, H - on hold, I - incomplete, or N - non- verified, U – unreleased, P – pending, O – on call, DE
> – discontinued edit, RE – reinstated, DR – discontinued renewal.
> Stop Date/Time The date and time an order is to expire.
> Stop Order Notices A list of patient medications that are about to expire and may require action.
> Syringe Type of IV that uses a syringe rather than a bottle or bag. The method of infusion for a syringe-type IV may be continuous or intermittent.
> Syringe Size The syringe size is the capacity or volume of a particular syringe. The size of a syringe is usually measured in number of cubic centimeters (ccs).
> TPN Total Parenteral Nutrition. The intravenous
> administration of the total nutrient requirements of the
> patient. The term TPN is also used to mean the solution compounded to provide those requirements.
> Units per Dose The number of Units (tablets, capsules, etc.) to be dispensed as a Dose for an order. Fractional numbers will be accepted.
> VA Drug Class Code A drug classification system used by VA that separates
> drugs into different categories based upon their characteristics. IV cost reports can be run for VA Drug Class Codes.
> VDL Virtual Due List. This is a Graphical User Interface (GUI) application used by the nurses when administering medications.
> Ward Group A ward group indicates inpatient nursing units (wards) that have been defined as a group within Inpatient Medications to facilitate processing of orders.
> WARD GROUP File File \#57.5. This file contains the name of the ward group, and the wards included in that group. The grouping is necessary for the pick list to be run for specific carts and ward groups.
> Ward Group Name A field in the WARD GROUP File (#57.5) used to assign an arbitrary name to a group of wards for the pick list and medication cart.
> WARD LOCATION File File \#42. This file contains all of the facility ward
> locations and their related data, i.e., Operating beds, Bedsection, etc. The wards are created/edited using the *Ward Definition* option of the Automatic Data Transmission (ADT) module.


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSJ*5*134 Technical Manual/Security Guide Change Pages

## Introduction 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation and Maintenance 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Installation 3
2.  Inpatient Parameters 3
    1.  Fields from the PHARMACY SYSTEM File (#59.7) 4
    2.  Fields from the INPATIENT WARD PARAMETERS File (#59.6) 6
    3.  Fields from the INPATIENT USER PARAMETERS File (#53.45) 9
    4.  Fields from the IV ROOM File (#59.5) 10
    5.  Fields from the CLINIC DEFINITION File (#53.46) 14

## Package Security 15

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3.  Option Security Keys 15
4.  File Security. 16

## File List 17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

5.  Unit Dose File Diagram. 18
6.  IV File Diagram 19

## Routines 21

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

7.  Descriptions 21
8.  Callable Routines. 24
9.  Routine Mapping 24
    1.  Do Not Map 24
    2.  Mapping Highly Recommended 25
    3.  Mapping Recommended 25
    4.  Deleting Inpatient Routines 26

## Templates 27

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

10. Print Templates 27
11. Input Templates 27
12. List Templates 29

## Exported Options 31

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

13. Stand-alone Options 31
14. Top-level Menus 31
    1.  Menu Assignment 31
    2.  Menu Placement. 31
15. Options 32

## Data Archiving and Purging 41

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

16. Archiving 41
17. Purging 41
    1.  Unit Dose Auto Purging 41
    2.  IV Auto Purging 41
    3.  Unit Dose Manual Purging – Temporarily Unavailable 42
    4.  IV Manual Purging – Temporarily Unavailable 43

## Inpatient Medications and CPRS 45

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

18. Installation of the Protocols for CPRS 45
19. Converting 45
    1.  Order Conversion 45
    2.  Pick List Conversion 46
    3.  Order Set Conversion 46
    4.  Verification Data Conversion 46
20. Protocol Descriptions 47
21. Health Level Seven (HL7) Messaging 51
    1.  HL7 Ordering Fields 51
    2.  Order Event Messages 56
    3.  Special Escaping Characters 65a
22. STAT, ASAP, and NOW Order Notification 66
    1.  PSJ STAT NOW PENDING ORDER Mail Group 67
    2.  PSJ STAT NOW ACTIVE ORDER Mail Group 68
    3.  Adding a Remote Member as a Subscriber. 69
    4.  Setting Up Ward-Specific Mail Groups 69

## Inpatient Medications and BCMA 69

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

23. API Exchange 69
24. Med Order Button 70

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>PSIVSUS1</th>
<th>PSIVUDL</th>
<th>PSIVUTL</th>
<th>PSIVUTL1</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSIVUWL</td>
<td>PSIVVW1</td>
<td>PSIVWCR</td>
<td>PSIVWCR1</td>
</tr>
<tr class="even">
<td>PSIVWL</td>
<td>PSIVWL1</td>
<td>PSIVWRP</td>
<td>PSIVXREF</td>
</tr>
<tr class="odd">
<td>PSIVXU</td>
<td><blockquote>
<p>PSJ53P1</p>
</blockquote></td>
<td>PSJ59P5</td>
<td>PSJAC</td>
</tr>
<tr class="even">
<td>PSJADT</td>
<td>PSJADT0</td>
<td>PSJADT1</td>
<td>PSJADT2</td>
</tr>
<tr class="odd">
<td>PSJALG</td>
<td>PSJBCMA</td>
<td>PSJBCMA1</td>
<td>PSJBCMA2</td>
</tr>
<tr class="even">
<td>PSJBCMA3</td>
<td>PSJBCMA4</td>
<td>PSJCOM</td>
<td>PSJCOM1</td>
</tr>
<tr class="odd">
<td>PSJCOMR</td>
<td>PSJCOMV</td>
<td>PSJDCHK</td>
<td>PSJDCU</td>
</tr>
<tr class="even">
<td>PSJDDUT</td>
<td>PSJDDUT2</td>
<td>PSJDDUT3</td>
<td>PSJDEA</td>
</tr>
<tr class="odd">
<td>PSJDGAL</td>
<td>PSJDIN</td>
<td>PSJDOSE</td>
<td>PSJDPT</td>
</tr>
<tr class="even">
<td>PSJEEU</td>
<td>PSJEEU0</td>
<td>PSJENV</td>
<td>PSJEXP</td>
</tr>
<tr class="odd">
<td>PSJEXP0</td>
<td>PSJFTR</td>
<td>PSJH1</td>
<td>PSJHEAD</td>
</tr>
<tr class="even">
<td>PSJHEH</td>
<td><blockquote>
<p>PSJHIS</p>
</blockquote></td>
<td>PSJHL10</td>
<td>PSJHL11</td>
</tr>
<tr class="odd">
<td>PSJHL2</td>
<td>PSJHL3</td>
<td>PSJHL4</td>
<td>PSJHL4A</td>
</tr>
<tr class="even">
<td>PSJHL5</td>
<td>PSJHL6</td>
<td>PSJHL7</td>
<td>PSJHL9</td>
</tr>
<tr class="odd">
<td>PSJHLERR</td>
<td>PSJHLU</td>
<td>PSJHLV</td>
<td>PSJHVARS</td>
</tr>
<tr class="even">
<td>PSJLIACT</td>
<td>PSJLIFN</td>
<td>PSJLIFNI</td>
<td>PSJLIORD</td>
</tr>
<tr class="odd">
<td>PSJLIPRF</td>
<td>PSJLIUTL</td>
<td>PSJLIVFD</td>
<td>PSJLIVMD</td>
</tr>
<tr class="even">
<td>PSJLMAL</td>
<td>PSJLMDA</td>
<td>PSJLMGUD</td>
<td>PSJLMHED</td>
</tr>
<tr class="odd">
<td>PSJLMPRI</td>
<td>PSJLMPRU</td>
<td>PSJLMUDE</td>
<td>PSJLMUT1</td>
</tr>
<tr class="even">
<td>PSJLMUT2</td>
<td>PSJLMUTL</td>
<td>PSJLOAD</td>
<td><blockquote>
<p>PSJLOI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PSJMAI</td>
<td>PSJMAI1</td>
<td>PSJMDIR</td>
<td>PSJMDIR1</td>
</tr>
<tr class="even">
<td>PSJMDWS</td>
<td>PSJMEDS</td>
<td>PSJMIV</td>
<td>PSJMP</td>
</tr>
<tr class="odd">
<td>PSJMPEND</td>
<td>PSJMPRT</td>
<td>PSJMPRTU</td>
<td>PSJMUTL</td>
</tr>
<tr class="even">
<td>PSJNTEG</td>
<td>PSJNTEG0</td>
<td>PSJNTEG1</td>
<td>PSJO</td>
</tr>
<tr class="odd">
<td>PSJO1</td>
<td>PSJO2</td>
<td>PSJO3</td>
<td>PSJOE</td>
</tr>
<tr class="even">
<td>PSJOE0</td>
<td>PSJOE1</td>
<td>PSJOEA</td>
<td>PSJOEA1</td>
</tr>
<tr class="odd">
<td>PSJOEEW</td>
<td>PSJOERI</td>
<td>PSJORAPI</td>
<td>PSJORDA</td>
</tr>
<tr class="even">
<td>PSJOREN</td>
<td><blockquote>
<p>PSJORMA1</p>
</blockquote></td>
<td>PSJORMA2</td>
<td>PSJORMAR</td>
</tr>
<tr class="odd">
<td>PSJORP2</td>
<td>PSJORPOE</td>
<td>PSJORRE</td>
<td><blockquote>
<p>PSJORRE1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSJORREN</td>
<td>PSJORRO</td>
<td>PSJORRN</td>
<td>PSJORRN1</td>
</tr>
<tr class="odd">
<td>PSJORUT2</td>
<td>PSJORUTL</td>
<td><blockquote>
<p>PSJP</p>
</blockquote></td>
<td>PSJPATMR</td>
</tr>
<tr class="even">
<td>PSJPDIR</td>
<td>PSJPDV</td>
<td>PSJPDV0</td>
<td>PSJPDV1</td>
</tr>
<tr class="odd">
<td>PSJPL0</td>
<td>PSJPR</td>
<td>PSJPR0</td>
<td><blockquote>
<p>PSJPST50</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSJPXRM1</td>
<td>PSJQPR</td>
<td>PSJRXI</td>
<td>PSJSPU</td>
</tr>
<tr class="odd">
<td>PSJSPU0</td>
<td>PSJSV</td>
<td>PSJSV0</td>
<td>PSJUNITD</td>
</tr>
<tr class="even">
<td>PSJUTL</td>
<td>PSJUTL1</td>
<td>PSJUTL2</td>
<td>PSJUTL3</td>
</tr>
<tr class="odd">
<td>PSJUTL5</td>
<td>PSJUTL6</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> The following routines are not used in this version of Inpatient Medications. They were exported in the initial Kernel Installation and Distribution System (KIDS) build as Delete at Site.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>PSGDCR</th>
<th><blockquote>
<p>PSGDCT0</p>
</blockquote></th>
<th>PSGEXP</th>
<th>PSGEXP0</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSGMMPST</td>
<td>PSGOROE0</td>
<td>PSGORU</td>
<td>PSGQOS</td>
</tr>
<tr class="even">
<td>PSIVNVO</td>
<td>PSIVOEDO</td>
<td>PSIVOENT</td>
<td>PSIVOEPT</td>
</tr>
<tr class="odd">
<td>PSIVRD0</td>
<td>PSIVRD0</td>
<td>PSJMAN</td>
<td>PSJOAC</td>
</tr>
<tr class="even">
<td>PSJOAC0</td>
<td><blockquote>
<p>PSJOE8</p>
</blockquote></td>
<td>PSJOE81</td>
<td>PSJOEE</td>
</tr>
<tr class="odd">
<td>PSJOER</td>
<td>PSJOER0</td>
<td>PSJORA</td>
<td>PSJORIN</td>
</tr>
<tr class="even">
<td>PSJUTL</td>
<td>PSJUTL1</td>
<td>PSJUTL2</td>
<td>PSJUTL3</td>
</tr>
</tbody>
</table>

## Routine Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Routines not listed here are used sparingly, and can be mapped if the site desires.

### Do Not Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSGXR\* PSJIP\* PSJXR\*

> The PSGXR\* and PSJXR\* routines are created by VA FileMan when it compiles the cross- references of the NON-VERIFIED ORDERS (#53.1) and PHARMACY PATIENT (#55) files.

> 24 Inpatient Medications V. 5.0 November 2005 Technical Manual/Security Guide

> Example: How to Print the Exported Protocols Using VA FileMan

### Back Door - Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Back door orders are handled by sending OE/RR the RDE message (pharmacy encoded order) with a 'send number' order control code. This allows OE/RR to store the order in its database and return the OE/RR order number to pharmacy with a 'number assigned' order control code. OE/RR cannot actually reject pharmacy events. The 'data errors' order control code is just used as some way to communicate to pharmacy that OE/RR could not interpret the RDE message.

> This should generally not happen.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 28%" />
<col style="width: 30%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><em><strong>Action Event from Pharmacy</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>OE/RR accepts</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>OE/RR rejects</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td>SN (send number) ZC (conversion)</td>
<td><blockquote>
<p>NA (number assigned)</p>
</blockquote></td>
<td><blockquote>
<p>DE (data errors)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,3,5,9,10,12,15,16</p>
<p>RXO: 1</p>
<p>RXE: 1,2,25,26</p>
<p>NTE: 1,2,3</p>
<p>RXR: 1</p>
<p>ZRX: 1,2,3,5</p></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,6,</p>
<p>7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td></td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>SC (finished)</p>
<p>RO (finished/replaced) XX (order changed)</p></td>
<td><blockquote>
<p>ORC-5 = CM (active)</p>
</blockquote></td>
<td><blockquote>
<p>DE (data errors)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5,9,10,12,15,</p>
<blockquote>
<p>16</p>
</blockquote>
<p>RXO: 1</p>
<p>RXE: 1,2,25,26</p>
<p>NTE: 1,2,3</p>
<p>RXR: 1</p>
<p>ZRX: 1,2,3,5</p></td>
<td><blockquote>
<p>There is no return event. OE/RR must accept the instruction from Pharmacy.</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,6,</p>
<p>7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td></td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td>ZV (verified)</td>
<td></td>
<td><blockquote>
<p>DE (data errors)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,11,15</p></td>
<td><blockquote>
<p>There is no return event. OE/RR must accept the instruction from Pharmacy.</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,6,</p>
<p>7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 26%" />
<col style="width: 31%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><em><strong>Action Event from Pharmacy</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>OE/RR accepts</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>OE/RR rejects</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td></td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>OC (cancel)</p>
<p>OD (discontinue) OH (hold)</p>
<p>OR (release)</p>
<p>SC (status change)</p></td>
<td></td>
<td><blockquote>
<p>DE (data errors)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5,12,15,16</p>
<p>RXE: 1</p>
<p>ZRX: 2,5</p></td>
<td><blockquote>
<p>There is no return event. OE/RR must accept the instruction from Pharmacy.</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,6,</p>
<p>7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](psj-5-134-technical-manual-security-guide-change-pages/006.png)Note: The following are Order Control Codes:

> OC - order cancelled before pharmacist verification OD - order cancelled after pharmacist verification

> SC - sent by pharmacy when order is verified, expired, or suspended

> XX - sent by pharmacy when fields change that do not generate new order

### Front Door - IV Fluids

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IV fluid orders use a RXC segment to contain information about solutions and additives. Therefore, a special code is sent in a RXO segment;1 to identify the order as an IV order (PS- 1^IV Order^99OTH). Since RXC segments are used, the give fields in a RXO segment are unnecessary.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 28%" />
<col style="width: 23%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><em><strong>Action Request from OE/RR</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Pharmacy accepts</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Pharmacy rejects</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>OR EVSEND PS</td>
<td><blockquote>
<p>PS EVSEND OR</p>
</blockquote></td>
<td><blockquote>
<p>PS EVSEND OR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td>NW (new order) XO (changed order)</td>
<td><blockquote>
<p>OK (accepted) XR (new order)</p>
</blockquote></td>
<td><blockquote>
<p>UA (unable to accept) UX (unable to change)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,7,9,10,12,15,16</p>
<p>RXO: 1,2</p>
<p>NTE: 1,2,3</p>
<p>RXC: 1,2,3,4</p>
<p>OBX: 1,2,3,5,14,16</p>
<p>ZRX: 1,2,3</p></td>
<td><blockquote>
<p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,12,15,16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td colspan="3">OR EVSEND PS</td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td colspan="3">ZV (verified)</td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,11,15</p></td>
<td><blockquote>
<p>There is no return event.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>OR EVSEND PS</td>
<td><blockquote>
<p>PS EVSEND OR</p>
</blockquote></td>
<td><blockquote>
<p>PS EVSEND OR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>CA (cancel)</p>
<p>DC (discontinue) HD (hold)</p>
<p>RL (release)</p>
<p>SS (send status)</p></td>
<td><blockquote>
<p>CR (canceled)</p>
<p>DR (discontinued) HR (held)</p>
<p>OR (released)</p>
<p>SC (status update)</p>
</blockquote></td>
<td><blockquote>
<p>UC (unable to cancel) UD (unable to dc) UH (unable to hold)</p>
<p>UR (unable to release) DE (data errors)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,10,12,15,16</p></td>
<td><blockquote>
<p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,16</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 62 Inpatient Medications V. 5.0 November 2005

### Example: POTASSIUM CHLORIDE INJ,SOLN FOR IV ORDERS 125 MEQ in SODIUM INJ,SOLN FOR IV ORDERS 1000 ml 100 ml/hr

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Order CPRS Continuous

> MSH\|^~\\\|ORDER ENTRY\|13000\|PHARMACY\|13000\|20080304170 224-0600\|\|ORM

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE

> PV1\|\|I\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| ORC\|NW\|12615;1^OR\|\|\|\|\|^^^^^R\|\|200803041702-0600\|11884

> \|\|11884\|\|\|20080304170224-0600\|I^POLICY^99ORN^^^

> RXO\|^^^PS-1^IV^99OTH\|333 ml/hr RXR\|^^^14^INTRAVENOUS^99PSR

> RXC\|B\|^^^196^DEXTROSE INJ,SOLN ^99PSP\|50\|^^^PSIV-1^ML

> ^99OTH

> RXC\|A\|^^^435^MORPHINE INJ ^99PSP\|33\|^^^PSIV-1^ML^99OT H

> ZRX\|\|I\|N\|\|\|C

#### New Order CPRS Intermittent

> MSH\|^~\\\|ORDER ENTRY\|13000\|PHARMACY\|13000\|20080304170 224-0600\|\|ORM

> PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE

> PV1\|\|I\|5\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| ORC\|NW\|12616;1^OR\|\|\|\|\|^BID&01-13^^^^R\|\|200803041702-0 600\|11884\|\|11884\|\|\|20080304170224-0600\|I^POLICY^99ORN^^^

> RXO\|^^^PS-1^IV^99OTH\| RXR\|^^^15^INTRAMUSCULAR^99PSR

> RXC\|B\|^^^196^DEXTROSE INJ,SOLN ^99PSP\|500\|^^^PSIV-1^M L^99OTH

> RXC\|A\|^^^281^FUROSEMIDE INJ,SOLN ^99PSP\|33\|^^^PSIV-4^ MG^99OTH

> ZRX\|\|I\|N\|\|\|I

> August 2008 Inpatient Medications V. 5.0 63

> Technical Manual/Security Guide

### Back Door - IV Fluids

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><em><strong>Action Event from Pharmacy</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>OE/RR accepts</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>OE/RR rejects</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td>SN (send number) ZC (conversion)</td>
<td><blockquote>
<p>NA (number assigned)</p>
</blockquote></td>
<td><blockquote>
<p>DE (data errors)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,3,5,9,10,12,15,16</p>
<p>RXE: 1,23,24</p>
<p>RXC: 1,2,3,4</p>
<p>ZRX: 1,2,3,5,6</p></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,6,7,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,</p>
<p>6,7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td></td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>SC (finished)</p>
<p>XX (order changed)</p></td>
<td></td>
<td><blockquote>
<p>DE (data errors)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5,9,10,12,15,16</p>
<p>RXE: 1,23,24</p>
<p>NTE: 1,2,3</p>
<p>RXC: 1,2,3,4</p>
<p>ZRX: 1,2,3,5,6</p></td>
<td><blockquote>
<p>There is no return event. OE/RR must accept the instruction from Pharmacy.</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,</p>
<p>6,7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>PS EVSEND OR</td>
<td></td>
<td><blockquote>
<p>OR EVSEND PS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Order Control</strong></td>
<td><p>OC (cancel)</p>
<p>OD (discontinue) OH (hold)</p>
<p>OR (release)</p>
<p>SC (status change)</p></td>
<td></td>
<td><blockquote>
<p>DE (data errors)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>HL7 Fields</strong></td>
<td><p>MSH: 1,2,3,4,9</p>
<p>PID: 3,5</p>
<p>PV1: 2,3</p>
<p>ORC: 1,2,3,5,9,10,12,15,16</p>
<p>RXE: 1</p>
<p>ZRX: 2,5</p></td>
<td><blockquote>
<p>There is no return event. OE/RR must accept the instruction from Pharmacy.</p>
</blockquote></td>
<td><blockquote>
<p>MSH: 1,2,3,4,5,</p>
<p>6,7,9</p>
<p>PID: 3,5</p>
<p>ORC: 1,2,3,16</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 64 Inpatient Medications V. 5.0 November 2005

### Example: POTASSIUM CHLORIDE INJ,SOLN FOR IV ORDERS 125 MEQ in SODIUM INJ,SOLN FOR IV ORDERS 1000 ml 100 ml/hr

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Order Continuous

> MSH\|^~\\\|PHARMACY\|500\|\|\|\|\|ORM\|\|\|\|\|\|\|\|\| PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| PV1\|\|I\|5^\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|3351\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> \|\|\|\|\|\|\| ORC\|SC\|12619^OR\|46V^PS\|\|CM\|\|^&^^^^^\|\|200803041719-060

> 0\|11884^PROVIDER,INPATIENT\|\|11884^PROVIDER,INPATIENT\|\|\|20080

> 3041900-0600\|W^Written^99ORN^^^\|\| RXO\|^^^435^MORPHINE INJ^99PSP\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXE\|^&^^200803041900-0600^200803100000-0600^\|\|\|\|\|\|\|\|\|

> \|\|\|\|11884^PROVIDER,INPATIENT^99NP\|\|\|\|\|\|\|^^99PSA^^^\|\|300\|^^^^ ml/hr^PSU\|\|

> RXC\|A\|^^^435^MORPHINE^99PSP\|20\|^^^PSIV-1^ML^99OTH\|\|\|\|

> \|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| RXC\|B\|^^^196^DEXTROSE^99PSP\|1000\|^^^PSIV-1^ML^99OTH\|\|

> \|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| RXR\|^^^14^INTRAVENOUS^99PSR\|\|\| ZRX\|\|W\|N\|\|11884^PROVIDER,INPATIENT^99NP\|C

#### New Order Intermittent

> MSH\|^~\\\|PHARMACY\|500\|\|\|\|\|ORM\|\|\|\|\|\|\|\|\| PID\|\|\|750\|\|PSJPATIENT,TESTPAT-FIVE\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| PV1\|\|I\|5^\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|3351\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> \|\|\|\|\|\|\|

> ORC\|SC\|12620^OR\|47V^PS\|\|CM\|\|^Q4H&01-05-09-13-17-21^^^

> ^^\|\|200803041721- 0600\|11884^PROVIDER,INPATIENT\|\|11884^PROVIDER,INPATIENT\|\|\|20

> 0803041700-0600\|W

> ^Written^99ORN^^^\|\|

> RXO\|^^^281^FUROSEMIDE INJ,SOLN^99PSP\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| RXE\|^Q4H&01-05-09-13-17-21^^200803041700-0600^2008030 60000-

> 0600^\|\|\|\|\|\|\|\|\|\|\|\|\|11884^PROVIDER,INPATIENT^99NP\|\|\|\|\|\|\|^01-

> 05-09-13-17-21^99PSA^^^

> \|\|INFUSE OVER 300 MINUTES\|\|\| RXC\|A\|^^^281^FUROSEMIDE^99PSP\|250\|^^^PSIV-4^MG^99OTH\|

> \|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| RXC\|B\|^^^196^DEXTROSE^99PSP\|1000\|^^^PSIV-1^ML^99OTH\|\|

> \|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

> RXR\|^^^160^IV PIGGYBACK^99PSR\|\|\| ZRX\|\|W\|N\|\|11884^PROVIDER,INPATIENT^99NP\|I

### Special Escaping Characters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Standard HL7 field delimiters represented by the "~ , &, \| " (tilde, ampersand, pipe) characters as well as the commonly used VistA "^" (caret) are sometimes needed by users of Inpatient Medications in various fields to provide complete information about a patient or order. The use of these characters can cause sending and receiving software to format HL7 messages incorrectly, and/or construct/deconstruct the information incorrectly. Data loss can also occur if data is truncated at one of the special delimiter characters.

> The following fields require special escaping characters.

- Patient ID - PID segment / piece 3
- Patient Name - PID segment / piece 5
- Schedule - ORC segment / piece 7 / subpiece 2
- Text - ORC segment / piece 7 / subpiece 8
- Requested Give Code - RXO segment / piece 1 / subpiece 5
- Requested Dispense Code - RXO segment / piece 10 / subpieces 2 and 4
- Schedule - RXE segment / piece 1 / subpiece 2
- Text - RXE segment / piece 2 /subpiece 8
- Comment - NTE segment / piece 3
- Route - RXR segment / piece 1 / subpiece 5
- Component Code - RXC segment / piece 2 / subpiece 5
- Component Units - RXC segment / piece 4 / subpiece 4
- Observation Value - OBX segment / piece 5
- Current User - ZRX segment / piece 5 / subpieces 1 and 2

> See External Relationships for the components used to escape and unescape characters.

> *(This page added for two-sided copying.)*

## STAT, ASAP, and NOW Order Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A STAT, ASAP, and NOW Order Notification has been added in Inpatient Medications to notify pharmacy and nursing staff when orders are received with a priority of STAT and ASAP or a schedule of STAT and NOW. The Notification sends a text message when a pending STAT, ASAP, or NOW order has either been received from CPRS or has been verified and made active. To receive these messages, the user must subscribe to the mail group(s) listed in this section.

> There are three parameters that can be defined to control which priorities / schedules are used to produce these notifications.

> The SYSTEMS PARAMETERS EDIT \[PSJ SYS EDIT\] option, PRIORITIES FOR PENDING

> NOTIFY parameter will control what priority or schedule of an order will cause a notification when the order is PENDING.

> The SYSTEMS PARAMETERS EDIT \[PSJ SYS EDIT\] option, PRIORITIES FOR ACTIVE

> NOTIFY parameter will control what priority or schedule of an order will cause a notification when the order is ACTIVE.

> The INPATIENT WARD PARAMETERS EDIT \[PSJ IWP EDIT\] option, PRIORITIES FOR

> NOTIFICATION parameter will control what priority or schedule of an order will cause a notification when the order is PENDING or ACTIVE for each individual WARD.

> ![](psj-5-134-technical-manual-security-guide-change-pages/007.png)Note: If all three parameters are left blank, then STAT, ASAP, and NOW orders will cause notifications. If the PRIORITIES FOR PENDING NOTIFY parameter is set and the other parameters left blank, then the PRIORITIES FOR PENDING NOTIFY parameter will control what priorities are sent.

> 66 Inpatient Medications V. 5.0 November 2005

### From: PSJ*5*275 Technical Manual/Security Guide Change Pages

## List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSJ LM ALLERGY DETAIL PSJ LM ALLERGY DISPL

> PSJ LM BRIEF PATIENT INFO PSJ LM CLINIC ORDERS

> PSJ LM DETAILED ALLERGY PSJ LM IV AC/EDIT

> PSJ LM IV DISPLAY

> PSJ LM IV INPT ACTIVE PSJ LM IV INPT DISPLAY PSJ LM IV INPT PENDING PSJ LM IV LABELS

> PSJ LM IV OE

> PSJ LM IV PENDING PSJ LM IV PROFILE

> PSJ LM IV RETURN LABELS PSJ LM OE

> PSJ LM OE DISPLAY PSJ LM PENDING EDIT PSJ LM PNV

> PSJ LM UD ACTION PSJU LM ACCEPT PSJU LM OE

> Example: How to Print List Templates using VA FileMan

> April 2013 Inpatient Medications V. 5.0 29

> (*This page included for two-sided copying*.)

7.  Exported Options

## Stand-alone Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All of the Inpatient Medications package options are designed to stand-alone and can be accessed without first accessing the top-level menu. All of the options can be placed on menus other than their original menu without any additional editing.

## Top-level Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There is no top-level menu for Inpatient Medications. The Inpatient Medications options are included in the IV and Unit Dose top-level menus.

### Menu Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign the following menus to the Inpatient Medications users:

> PSJU MGR This is the only Unit Dose Medications menu, and is to be assigned to all Unit Dose users.

> PSJI MGR This IV Medications menu is to be assigned to the pharmacists, inpatient supervisors, and package coordinators.

> PSJI USR1 This IV Medications menu is to be assigned to the nurses.

> PSJI USR2 This IV Medications menu is to be assigned to the pharmacy technicians.

### Menu Placement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is strongly recommended that the user <u>does not</u> place the Inpatient Medications (IV and Unit Dose) menus under the Outpatient Pharmacy menu. It is suggested that they be placed on the same menu as the Outpatient Pharmacy menu instead.

> Although it has been common practice to place the Inpatient Medications top-level menus under the Outpatient Pharmacy menu, this can cause \<STORE\> errors.

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following options are exported with the Inpatient Medications package: <u>Option Name</u> <u>Menu Text</u>

> PSJ AC SET-UP AUto-Discontinue Set-Up

> PSJ CD Clinic Definition

> PSJ CHECK DRUG INTERACTION Check Drug Interaction

> PSJ ECO Edit Clinic Med Orders Start Date/Time

> PSJ EXP INpatient Stop Order Notices

> PSJ EXTP Patient Profile (Extended)

> PSJ IWP EDIT Inpatient Ward Parameters Edit

> PSJ MDWS Medications Due Worksheet

> PSJ OAOPT Order Action on Patient Transfer

> PSJ OE Inpatient Order Entry

> PSJ PARAM EDIT MENU PARameters Edit Menu

> PSJ PDV Patients on Specific Drug(s)

> PSJ PR Inpatient Profile

> PSJ SEUP Inpatient User Parameters Edit

> PSJ SYS EDIT Systems Parameters Edit

> PSJ UD ALIGN LABEL Align Unit Dose Labels

> PSJ UEUP Edit Inpatient User Parameters

> PSJI 200 Correct Changed Names in IV Orders

> PSJI ACTIVE Active Order List (IV)

> PSJI ALIGNMENT Align Labels (IV)

> (*This page included for two-sided copying*.)

## Protocol Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Inpatient Medications package sends the following protocols for use in V. 5.0. These protocols are automatically installed when the Inpatient Medications initial installation is run.

> The protocols with "PAT" as part of their name assume that the patient has already been selected through CPRS before the protocol is selected. The other protocols will prompt the user for patients.

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Protocol Name</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Item Text</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJ DISPLAY DRUG ALLERGIES</p>
</blockquote></td>
<td><blockquote>
<p>Display Drug Allergies</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM 14D MAR</p>
</blockquote></td>
<td><blockquote>
<p>14 Day MAR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM 24H MAR</p>
</blockquote></td>
<td><blockquote>
<p>24 Hour MAR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM 7D MAR</p>
</blockquote></td>
<td><blockquote>
<p>7 Day MAR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM AP1</p>
</blockquote></td>
<td><blockquote>
<p>Action Profile #1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM AP2</p>
</blockquote></td>
<td><blockquote>
<p>Action Profile #2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM BPI HIDDEN ACTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Brief Patient Info Hidden Actions Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM BRIEF PATIENT INFO MENU</p>
</blockquote></td>
<td><blockquote>
<p>Brief Allergy Display</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM BYPASS</p>
</blockquote></td>
<td><blockquote>
<p>Bypass</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM CWAD</p>
</blockquote></td>
<td><blockquote>
<p>CWAD Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM DC</p>
</blockquote></td>
<td><blockquote>
<p>Discontinue</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM DETAILED ALLERGY</p>
</blockquote></td>
<td><blockquote>
<p>Detailed Allergy/ADR List</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM DETAILED ALLERGY MENU</p>
</blockquote></td>
<td><blockquote>
<p>ALLERGY/ADR LIST MENU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM DIN</p>
</blockquote></td>
<td><blockquote>
<p>Drug Restriction/Guideline</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM DRUG CHECK</p>
</blockquote></td>
<td><blockquote>
<p>Check Interactions</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM ECO HIDDEN ACTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Clinic Order Hidden Actions Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM ECO IM PR</p>
</blockquote></td>
<td><blockquote>
<p>Inpatient Medications Profile</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM ECO MENU</p>
</blockquote></td>
<td><blockquote>
<p>Clinic Order Edit Start Date/Time</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM ECO RANGE</p>
</blockquote></td>
<td><blockquote>
<p>Date Range</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM ECO SELECT</p>
</blockquote></td>
<td><blockquote>
<p>Edit Start Date</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM ECO START</p>
</blockquote></td>
<td><blockquote>
<p>Edit Start Date</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM EDIT ALLERGY/ADR DATA</p>
</blockquote></td>
<td><blockquote>
<p>Enter/Edit Allergy/ADR Data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM EDIT NEW</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM EXTP</p>
</blockquote></td>
<td><blockquote>
<p>Patient Profile (Extended)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM FINISH</p>
</blockquote></td>
<td><blockquote>
<p>Finish</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM FINISH MENU</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM FLAG</p>
</blockquote></td>
<td><blockquote>
<p>Flag</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM HOLD</p>
</blockquote></td>
<td><blockquote>
<p>Hold</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM INTERVENTION DELETE</p>
</blockquote></td>
<td><blockquote>
<p>Delete Pharmacy Intervention</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM INTERVENTION EDIT</p>
</blockquote></td>
<td><blockquote>
<p>Edit Pharmacy Intervention</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM INTERVENTION NEW ENTRY</p>
</blockquote></td>
<td><blockquote>
<p>Enter Pharmacy Intervention</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM INTERVENTION PRINTOUT</p>
</blockquote></td>
<td><blockquote>
<p>Print Pharmacy Intervention</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM INTERVENTION VIEW</p>
</blockquote></td>
<td><blockquote>
<p>View Pharmacy Intervention</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM IV NEW SELECT ORDER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM IV OE MENU</p>
</blockquote></td>
<td><blockquote>
<p>IV ORDER ENTRY MENU</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Protocol Name</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Item Text</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJ LM IV SELECT ORDER</p>
</blockquote></td>
<td><blockquote>
<p>Select Order</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM LABEL PRINT/REPRINT MENU</p>
</blockquote></td>
<td><blockquote>
<p>Label Print/Reprint</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM MAR MENU</p>
</blockquote></td>
<td><blockquote>
<p>MAR Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM MDWS</p>
</blockquote></td>
<td><blockquote>
<p>Medications Due Worksheet</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM NEW ORDER</p>
</blockquote></td>
<td><blockquote>
<p>New Order Entry</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM NEW ORDER FROM PROFILE</p>
</blockquote></td>
<td><blockquote>
<p>New Order Entry</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM NEW SELECT ALLERGY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM NEW SELECT ORDER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM OE MENU</p>
</blockquote></td>
<td><blockquote>
<p>ORDER ENTRY MENU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM ORDER VIEW HIDDEN</p>
<p>ACTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Order View Hidden Actions Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM OTHER PHARMACY OPTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Other Pharmacy Options</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><span id="_bookmark2" class="anchor"></span>PSJ LM OVERRIDES</p>
</blockquote></td>
<td><blockquote>
<p>Overrides/Interventions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM PAT PR</p>
</blockquote></td>
<td><blockquote>
<p>Inpatient Medications Profile</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM PATIENT DATA</p>
</blockquote></td>
<td><blockquote>
<p>Patient Record Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM PATIENT INFO</p>
</blockquote></td>
<td><blockquote>
<p>Patient Information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM PENDING ACTION</p>
</blockquote></td>
<td><blockquote>
<p>Pending Order Actions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM PHARMACY INTERVENTION</p>
<p>MENU</p>
</blockquote></td>
<td><blockquote>
<p>Pharmacy Intervention Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM PNV JUMP</p>
</blockquote></td>
<td><blockquote>
<p>Jump to a Patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM PRINT OUTPATIENT PROFILE</p>
</blockquote></td>
<td><blockquote>
<p>Outpatient Prescriptions</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM PROFILE HIDDEN ACTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Profile Hidden Actions Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM PROFILE MENU</p>
</blockquote></td>
<td><blockquote>
<p>Patient Profiles</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM RETURNS/DESTROYED MENU</p>
</blockquote></td>
<td><blockquote>
<p>Returns/Destroyed Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ LM SELECT ORDER</p>
</blockquote></td>
<td><blockquote>
<p>Select Order</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ LM SHOW PROFILE</p>
<p>PSJ LM VIEW ORDER DETAIL</p>
</blockquote></td>
<td><blockquote>
<p>View Profile</p>
<p>View Order Detail</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ OR MENU</p>
</blockquote></td>
<td><blockquote>
<p>Inpatient Medications Ward Reports</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ OR PAT ADT</p>
</blockquote></td>
<td><blockquote>
<p>Inpatient Medications Actions on Patient ADT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ OR PAT MENU</p>
</blockquote></td>
<td><blockquote>
<p>Inpatient Medications Patient Reports</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ OR PAT OE</p>
</blockquote></td>
<td><blockquote>
<p>Inpatient Medications</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ OR PAT OE MENU</p>
</blockquote></td>
<td><blockquote>
<p>Inpatient Medications</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ OR PAT PR</p>
</blockquote></td>
<td><blockquote>
<p>Inpatient Medications Profile</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ OR PAT PR MENU</p>
</blockquote></td>
<td><blockquote>
<p>Inpatient Medications Profiles</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ OR PR</p>
</blockquote></td>
<td><blockquote>
<p>Inpatient Medications Profile</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ PC IV AC/EDIT ACTION</p>
</blockquote></td>
<td><blockquote>
<p>IV ACCEPT EDIT ACTIONS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ PC IV ACCEPT</p>
</blockquote></td>
<td><blockquote>
<p>Accept</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ PC IV CANCELLED</p>
</blockquote></td>
<td><blockquote>
<p>Cancelled</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ PC IV DESTROYED</p>
</blockquote></td>
<td><blockquote>
<p>Destroyed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ PC IV LABELS ACTION</p>
</blockquote></td>
<td><blockquote>
<p>INDIVIDUAL IV LABEL ACTIONS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ PC IV LOG</p>
</blockquote></td>
<td><blockquote>
<p>Activity Logs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ PC IV NEW LABELS</p>
</blockquote></td>
<td><blockquote>
<p>PRINT NEW IV LABELS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ PC IV RECYCLED</p>
</blockquote></td>
<td><blockquote>
<p>Recycled</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Protocol Name</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Item Text</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJ PC IV REPRINT LABELS</p>
</blockquote></td>
<td><blockquote>
<p>Reprint IV label(s)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJ PC RETURN IV LABELS ACTION</p>
</blockquote></td>
<td><blockquote>
<p>RETURN IV LABELS ACTIONS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJ SELECT ALLERGY</p>
</blockquote></td>
<td><blockquote>
<p>Select Allergy</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI LM ACTIVE MENU</p>
</blockquote></td>
<td><blockquote>
<p>IV Active Order Actions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI LM ACTIVITY LOG</p>
</blockquote></td>
<td><blockquote>
<p>View Activity Log</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI LM ALIGNMENT</p>
</blockquote></td>
<td><blockquote>
<p>Align Labels (IV)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI LM DISCONTINUE</p>
</blockquote></td>
<td><blockquote>
<p>Discontinue</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI LM EDIT</p>
</blockquote></td>
<td><blockquote>
<p>Edit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI LM FINISH</p>
</blockquote></td>
<td><blockquote>
<p>Finish</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI LM LABEL LOG</p>
</blockquote></td>
<td><blockquote>
<p>View Label Log</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI LM LBLI</p>
</blockquote></td>
<td><blockquote>
<p>Individual Labels (IV)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI LM LBLR</p>
</blockquote></td>
<td><blockquote>
<p>Reprint Scheduled Labels (IV)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI LM LBLS</p>
</blockquote></td>
<td><blockquote>
<p>Scheduled Labels (IV)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI LM LOG MENU</p>
</blockquote></td>
<td><blockquote>
<p>IV Profile Log Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI LM PAT PR</p>
</blockquote></td>
<td><blockquote>
<p>IV Medications Profile</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI LM PENDING ACTION</p>
</blockquote></td>
<td><blockquote>
<p>IV Pending Order Actions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI LM RETURNS</p>
</blockquote></td>
<td><blockquote>
<p>Returns/Destroyed Entry (IV)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI OR PAT FLUID OE</p>
</blockquote></td>
<td><blockquote>
<p>IV Fluids</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI OR PAT FLUID OE MENU</p>
</blockquote></td>
<td><blockquote>
<p>IV FLUIDS...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI OR PAT HYPERAL OE</p>
</blockquote></td>
<td><blockquote>
<p>IV Hyperal</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI OR PAT PR</p>
</blockquote></td>
<td><blockquote>
<p>IV Medications Profile</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI OR PR</p>
</blockquote></td>
<td><blockquote>
<p>IV Medications Profile</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI PC HOLD</p>
</blockquote></td>
<td><blockquote>
<p>Hold</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJI PC ONCALL</p>
</blockquote></td>
<td><blockquote>
<p>On Call</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJI PC RENEWAL</p>
</blockquote></td>
<td><blockquote>
<p>Renew</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM ACCEPT</p>
</blockquote></td>
<td><blockquote>
<p>Accept</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM ACCEPT EDIT</p>
</blockquote></td>
<td><blockquote>
<p>Edit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM ACCEPT MENU</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM ACTIONS MENU</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM ACTIVITY LOG</p>
</blockquote></td>
<td><blockquote>
<p>Activity Logs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM AL</p>
</blockquote></td>
<td><blockquote>
<p>Align Labels (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM COPY</p>
</blockquote></td>
<td><blockquote>
<p>Copy</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM EDIT</p>
</blockquote></td>
<td><blockquote>
<p>Edit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM HIDDEN ACTIONS</p>
</blockquote></td>
<td><blockquote>
<p>UD Hidden Actions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM HIDDEN UD ACTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Unit Dose Hidden Actions</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM LABEL</p>
</blockquote></td>
<td><blockquote>
<p>Label Print/Reprint</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM MARK INCOMPLETE</p>
</blockquote></td>
<td><blockquote>
<p>Mark Order As Incomplete</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM MARK NOT GIVE</p>
</blockquote></td>
<td><blockquote>
<p>Mark Order Not To Be Given</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM PAT PR</p>
</blockquote></td>
<td><blockquote>
<p>Unit Dose Medications Profile</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM PL</p>
</blockquote></td>
<td><blockquote>
<p>Pick List</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM PL MENU</p>
</blockquote></td>
<td><blockquote>
<p>Pick List Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM PLDP</p>
</blockquote></td>
<td><blockquote>
<p>Enter Units Dispensed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM PLEUD</p>
</blockquote></td>
<td><blockquote>
<p>Extra Units Dispensed</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Protocol Name</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Item Text</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSJU LM PLRP</p>
</blockquote></td>
<td><blockquote>
<p>Reprint Pick List</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM PLUP</p>
</blockquote></td>
<td><blockquote>
<p>Update Pick List</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM RENEW</p>
</blockquote></td>
<td><blockquote>
<p>Renew</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM RET</p>
</blockquote></td>
<td><blockquote>
<p>Report Returns (UD)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM SPEED DISCONTINUE</p>
</blockquote></td>
<td><blockquote>
<p>Speed Discontinue</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM SPEED FINISH</p>
</blockquote></td>
<td><blockquote>
<p>Speed Finish</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM SPEED RENEW</p>
</blockquote></td>
<td><blockquote>
<p>Speed Renew</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU LM SPEED VERIFY</p>
</blockquote></td>
<td><blockquote>
<p>Speed Verify</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU LM VERIFY</p>
</blockquote></td>
<td><blockquote>
<p>Verify</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU OR 14D MAR</p>
</blockquote></td>
<td><blockquote>
<p>14 Day MAR (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU OR 7D MAR</p>
</blockquote></td>
<td><blockquote>
<p>7 Day MAR (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU OR AP-1</p>
</blockquote></td>
<td><blockquote>
<p>Action Profile #1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU OR AP-2</p>
</blockquote></td>
<td><blockquote>
<p>Action Profile #2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU OR DS</p>
</blockquote></td>
<td><blockquote>
<p>Authorized Absence/Discharge Summary (Unit</p>
<p>Dose)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU OR PAT 14D MAR</p>
</blockquote></td>
<td><blockquote>
<p>14 Day MAR (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU OR PAT 7D MAR</p>
</blockquote></td>
<td><blockquote>
<p>7 Day MAR (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU OR PAT AP-1</p>
</blockquote></td>
<td><blockquote>
<p>Action Profile #1 (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU OR PAT AP-2</p>
</blockquote></td>
<td><blockquote>
<p>Action Profile #2 (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU OR PAT DS</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Summary (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU OR PAT PR</p>
</blockquote></td>
<td><blockquote>
<p>Unit Dose Medications Profile</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU OR PAT VBW</p>
</blockquote></td>
<td><blockquote>
<p>Non-Verified Orders (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU OR PR</p>
</blockquote></td>
<td><blockquote>
<p>Patient Profile (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSJU OR VBW</p>
</blockquote></td>
<td><blockquote>
<p>Non-Verified Orders (Unit Dose)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSJU PLATCS</p>
</blockquote></td>
<td><blockquote>
<p>Send Pick List to ATC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VALM DOWN A LINE</p>
</blockquote></td>
<td><blockquote>
<p>Down a Line</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VALM FIRST SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>First Screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VALM GOTO PAGE</p>
</blockquote></td>
<td><blockquote>
<p>Go to Page</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VALM HIDDEN ACTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Standard Hidden Actions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VALM LAST SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Last Screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VALM LEFT</p>
</blockquote></td>
<td><blockquote>
<p>Shift View to Left</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VALM NEXT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Next Screen</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VALM PREVIOUS SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Previous Screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VALM PRINT LIST</p>
</blockquote></td>
<td><blockquote>
<p>Print List</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VALM PRINT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Print Screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VALM QUIT</p>
</blockquote></td>
<td><blockquote>
<p>Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VALM REFRESH</p>
</blockquote></td>
<td><blockquote>
<p>Re-Display Screen</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VALM RIGHT</p>
</blockquote></td>
<td><blockquote>
<p>Shift View to Right</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VALM SEARCH LIST</p>
</blockquote></td>
<td><blockquote>
<p>Search List</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VALM TURN ON/OFF MENUS</p>
</blockquote></td>
<td><blockquote>
<p>Auto-Display (On/Off)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VALM UP ONE LINE</p>
</blockquote></td>
<td><blockquote>
<p>Up a Line</p>
</blockquote></td>
</tr>
</tbody>
</table>

### From: PSJ*5*254 Technical Manual/Security Guide Change Pages

## Revision History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 63%" />
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
<td>01/2012</td>
<td>i-ii, v-viii</td>
<td><blockquote>
<p>PSJ*5*254</p>
</blockquote></td>
<td>Updated Table of Contents</td>
</tr>
<tr class="even">
<td></td>
<td>22, 23</td>
<td></td>
<td>Updated Routines</td>
</tr>
<tr class="odd">
<td></td>
<td>69</td>
<td></td>
<td>Added API</td>
</tr>
<tr class="even">
<td></td>
<td>94</td>
<td></td>
<td>Added 5653 and 5654 Inpatient Medications Integration</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>Agreements</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/2011</td>
<td>i, v, vi,</td>
<td><blockquote>
<p>PSJ*5*181</p>
</blockquote></td>
<td>Changes to <em>Revision History</em>, <em>Table of Contents</em>; added new field</td>
</tr>
<tr class="even">
<td></td>
<td>vii, vii, 5-</td>
<td></td>
<td>to PHARMACY SYSTEM File (#59.7), added new field to the</td>
</tr>
<tr class="odd">
<td></td>
<td>8b,</td>
<td></td>
<td>INPATIENT WARD PARAMETERS File (#59.6). Added</td>
</tr>
<tr class="even">
<td></td>
<td>(changed</td>
<td></td>
<td>information re: the Pharmacy Reengineering (PRE) API Manual</td>
</tr>
<tr class="odd">
<td></td>
<td>flow) 22,</td>
<td></td>
<td>under "<em>Callable Routines</em>"; removed entire section 5.3, Routine</td>
</tr>
<tr class="even">
<td></td>
<td>23, 24,</td>
<td></td>
<td>Mapping, and all its sub-sections; added Health Level Seven</td>
</tr>
<tr class="odd">
<td></td>
<td>removed</td>
<td></td>
<td>(HL7) data field under segment { RXC}. Added the following</td>
</tr>
<tr class="even">
<td></td>
<td>25-26,</td>
<td></td>
<td>"<em>Inpatient Medications Custodial Integration Agreements</em>":</td>
</tr>
<tr class="odd">
<td></td>
<td>changed</td>
<td></td>
<td>4074, 4264, 4580, 5001, 5057; 5058, 5306, 5385. Added two</td>
</tr>
<tr class="even">
<td></td>
<td>53, 85, 86,</td>
<td></td>
<td>packages, HWSC and VistALink, to <em>External Relationships</em>,</td>
</tr>
<tr class="odd">
<td></td>
<td>93-</td>
<td></td>
<td>under <em>Packages Needed to Run Inpatient Medications</em>. Added the</td>
</tr>
<tr class="even">
<td></td>
<td>94;94a-b,</td>
<td></td>
<td>following call routines and their entry points: OROCAPI,</td>
</tr>
<tr class="odd">
<td></td>
<td>121--130</td>
<td></td>
<td>PSSDSAPD, PSSDSAPI, PSSFDBRT, PSODDPR4,</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>PSODRDU2. Added the items <strong>DATUP, MOCHA, PECS, and</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><strong>PEPS</strong> in Glossary, which shifted all subsequent glossary items.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>Added routines PSJMISC2 &amp;PSJOCVAR to the routines table</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>and removed Section 5.3</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>02/11</td>
<td><blockquote>
<p>i, 53, 62,</p>
<p>64, 65</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*226</p>
</blockquote></td>
<td>Added to RXC section Field 5, "Additive Frequency" in HL7 Ordering Fields; updated Front Door – IV Fluids table with Field 5; updated Back Door – IV Fluids table with Field 5; updated example.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>06/10</td>
<td>i, 22-23</td>
<td><blockquote>
<p>PSJ*5*113</p>
</blockquote></td>
<td><p>Added routine PSGSICH1.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 63%" />
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
<td>02/10</td>
<td><a href="#revision-history">i,</a> 23</td>
<td><blockquote>
<p>PSJ*5*214</p>
</blockquote></td>
<td><p>Added PSJQUTIL to the routine list in Section 5.1 for Patients on Specific Drug(s) Multidivisional Enhancements Project.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/09</td>
<td>22-23</td>
<td><blockquote>
<p>PSJ*5*222</p>
</blockquote></td>
<td><p>Added routine PSGOEF2.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>08/08</td>
<td>vi, 23, 51-</td>
<td><blockquote>
<p>PSJ*5*134</p>
</blockquote></td>
<td>Parameters for escaping special characters added. New HL7</td>
</tr>
<tr class="even">
<td></td>
<td>53, 57-58,</td>
<td></td>
<td>messages added. New routines added. HL7 order fields table</td>
</tr>
<tr class="odd">
<td></td>
<td>60-61, 63,</td>
<td></td>
<td>contains an asterisk for each field that has special escaping characters.</td>
</tr>
<tr class="even">
<td></td>
<td><p>65, 65a-</p>
<p>65b</p></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>02/07</td>
<td>74-76</td>
<td><blockquote>
<p>PSJ*5*178</p>
</blockquote></td>
<td><p>MED ROUTE now appears in larger font on IV labels from the Zebra bar code printer. Med ROUTE now prints on the IV labels for bar-code enabled printers, and it prints in larger font than surrounding text.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>09/06</td>
<td>23, 94</td>
<td><blockquote>
<p>PSJ*5*172</p>
</blockquote></td>
<td><p>Encapsulation Cycle II project: Added PSJ53P1 to the Routine List in Section 5.1. Added DBIA 4537 to DBIA list. Changed the date on the Title Page to December 1997.</p>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>05/06</td>
<td><blockquote>
<p>v-viii 8a-8b 66-68b</p>
</blockquote></td>
<td><blockquote>
<p>PSJ*5*154</p>
</blockquote></td>
<td><p>In Section 2.2.2 Added "PRIORITIES FOR NOTIFICATION"</p>
<p>field.</p>
<p>In Section 9.5, made correction to include the priority of ASAP in notifications. Added information regarding the three notifications parameters.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/2005</td>
<td>23</td>
<td><blockquote>
<p>PSJ*5*146</p>
</blockquote></td>
<td><p>Remote Data Interoperability (RDI) Project: Added PSJLMUT2 to the Routine List in Section 5.1.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/2005</td>
<td>All</td>
<td><blockquote>
<p>PSJ*5*163</p>
</blockquote></td>
<td><p>Encapsulation Cycle II project: Added PSJ59P5 to the Routine List in Section 5.1. Added DBIA 4819 to DBIA list. Deleted DBIAs 172, 634, and 1882 from the DBIA list.</p>
<p>Reissued entire document due to a page numbering issue. <mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

### API Exchange

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient and order information is exchanged between Inpatient Medications and BCMA. This exchange is possible through Application Program Interfaces (APIs).

> <u>APIs provided to BCMA</u>

> PSJBCMA - The entry point EN^PSJBCMA is provided by the Inpatient Medications package to return patient active orders to BCMA to be used in administering medications at patient's bedside. The SEND TO BCMA field (#3) in the CLINIC DEFINITION file (#53.46) allows the user to specify, by clinic, whether or not Inpatient Medication Orders for Outpatients will be sent to BCMA.

> PSJBCMA1 - The entry point EN^PSJBCMA1 is provided by the Inpatient Medications package to return the detail information on a patient's order for BCMA to use.

> PSJBCMA2 - The entry point EN^PSJBCMA2 is provided by Inpatient Medications package to return a patient order's activity logs for BCMA to use.

> PSJBCMA3 - The purpose of this API is to get information from BCMA to put in the PHARMACY PATIENT FILE (#55). It also updates the BCMA status information for the bag associated with a Unique Bar Code ID label.

> PSJBCMA4- The purpose of this API is to allow BCMA to expire/reinstate Inpatient Medications orders based on an administration event.

> PSGSICH1 - The entry point GETPROVL^PSGSICH1 is provided by the Inpatient Medications package to return CPRS Provider Overrides associated with a specific Inpatient Medications order. Entry point INTRDIC^PSGSICH1 is provided by the Inpatient Medications package to return Pharmacist Interventions associated with a specific Inpatient Medications order.

> <u>APIs provided to Inpatient Medications</u>

> EN^PSBIPM - The entry point EN^PSBIPM is provided by the BCMA package to provide information to Inpatient Medications to be used in determining the start date for a renewed order. \[Database Integration Agreement (DBIA) \# 3174\].

> MOB^PSBIPM - The entry point MOB^PSBIPM is provided by the BCMA package to provide Inpatient Medications with an array of data returned by the BCMA/CPRS Med Order function.

> MOBR^PSBIPM - The entry point MOBR^PSBIPM is provided by the BCMA package to provide Inpatient Medications a way to notify BCMA that the BCMA/CPRS Med Order Button order has been processed or rejected. There is no return from this entry point.

January 2012 Inpatient Medications V. 5.0 69

> Technical Manual/Security Guide PSJ\*5\*254

### Med Order Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The BCMA/CPRS Med Order Button (Med Order) software is an integrated component of the VistA environment and uses bar code technology to electronically order, sign, and document STAT and NOW medications from verbal or telephoned medication orders for inpatients from the BCMA Virtual Due List (VDL). Medications are ordered and signed through the CPRS Inpatient Medication order dialog and are passed to the Inpatient Medications V. 5.0 software application as nurse-verified orders with the Priority of Done. The medications are documented as administered to the patient in the BCMA Medication Log and Medication Administration History (MAH).

> The BCMA VDL has been modified to contain a Med Order button that allows the authorized user the ability to properly document a STAT or NOW medication order through BCMA. Each user must hold a special key to allow them access to the button on the BCMA VDL. There is a system parameter in BCMA that allows the site the added ability to turn off or on the functionality system wide.

> When the Med Order button is activated, BCMA opens a CPRS Graphical User Interface (GUI) medication dialog ordering session. The medication dialog screen allows for the entry of STAT or NOW Unit Dose or IV Type orders within the same session. The user is able to scan a bar coded IEN or National Drug Code (NDC) number affixed to the product, to select the dispense drug for this administration. Pharmacy Orderable item, IV Additive, and IV Solution selection (based on dispense drug) occurs in the background and is automatic. Dispense drugs selected for IV Type orders that point to multiple active IV Additive or IV Solution file links require the user to make a single selection. Manual entry of the dispense drug into the medication field is allowed if bar codes are damaged or missing.

> All orders entered through this interface are automatically marked as "Done" in CPRS GUI. Unit Dose, Piggyback, and Syringe (intermittent) orders are marked as "GIVEN" in BCMA and will not appear on the VDL. IV Type orders including Admixture and Syringe (non-intermittent) are marked as "INFUSING" in BCMA and will appear on the VDL for further interaction. CPRS GUI passes the order to Inpatient Medications for pharmacist verification. Order administration data will still be available to be edited through the BCMA menu option Edit Medication Log. All orders require an electronic signature.

> The administration date/time box on the order screen defaults to the time the Med Order button was accessed. The user is allowed to edit this date/time to a date/time in the past since some STAT and NOW orders are actually entered after they are administered. The user will NOT be allowed to enter a date/time in the future.

> Once the Unit Dose or IV Type order is entered and the accept order button is selected, the user will be taken back to the order screen to specify ordering dialog and enter additional orders.

> 2945 NAME: Use of calls in PSIVSP

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSIVSP

> 3143 NAME: DBIA3143

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: CLINICAL REMINDERS Salt Lake City

> ROUTINE: PSJORAPI

> 3167 NAME: 3167

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSJORPOE

> 3243 NAME: Active Flag

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSJORREN

> 3320 NAME: UPDATE BCMA STATUS INFORMATION

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

> ROUTINE: PSJBCMA3

> 3416 NAME: DBIA3416

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

> ROUTINE: PSJBCMA4

> 3598 NAME: DBIA3598

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSJOERI

> 3836 NAME: PSJPXRM1

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: CLINICAL REMINDERS Salt Lake City

> ROUTINE: PSJPXRM1

> 3876 NAME: PSJBCBU

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

> ROUTINE: PSJBCBU

> 4074 NAME: OR Call to PSJORUT2

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSJORUT2

> 4264 NAME: PDM ACCESS TO PSJXRFS

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

> ROUTINE: PSJXRFS

> 4265 NAME: PDM ACCESS TO PSJXRFK

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

> ROUTINE: PSJXRFK

> 4537 NAME: PSJ53P1

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE:

> ROUTINE: PSJ53P1

> 4580 NAME: VALIDATE DOW SCHEDULES

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: PHARMACY DATA MANAGEMENT Birmingham

> ROUTINE: PSIVUTL

> 4819 NAME: PSJ59P5

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE:

> ROUTINE: PSJ59P5

> 5001 NAME: Pointing to the PHARMACY QUICK ORDER (#57.1) File

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE:

> USUAGE: Supported

> 5057 NAME: BCMA LAST ACTION

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

> DRUG ACCOUNTABILITY ROUTINE: PSJUTL2

> 5058 NAME: ALLERIES ARRAY

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

> ROUTINE: PSJMUTL

> 5306 NAME: PSJBLDOC

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: OUTPATIENT PHARMACY Birmingham

> ROUTINE: PSJBLDOC

> 5385 NAME: Dosing Checks for IVs

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: ORDER ENTRY/RESULTS REPORTING Salt Lake City

> ROUTINE: PSJAPIDS

> 5653 NAME: RETURN CPRS ORDER CHECKS AND OVERRIDES TO BCMA

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

> ROUTINE: GETPROVL^PSGSICH1

> 5654 NAME: INPATIENT INTERVENTIONS TO BCMA

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

> ROUTINE: INTRDIC^PSGSICH1

> 94 Inpatient Medications V. 5.0 January 2012

### From: PSJ*5*284 Technical Manual/Security Guide Change Pages

## Device File Setup Network Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Edit the Device File (#3.5) for ATC Device to use Network Channel.

> Obtain the IP address and port assignment for the Receiving Lantronix/TCP IP Interface. Lookup the ATC Device setup for the Ward location(s):

> Edit the Device with the following information:

> Verify Device File changes:

## Common Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Occasionally, a site experiences trouble getting the interface to run properly when the site first acquires an ATC, or has trouble later with the interface stopping in the middle of pick lists sends. If this happens, please try one or more of the following:

- Some sites have found that lowering the baud rate from 9600 to 4800, or even 2400, solves their problem.
- Sometimes, there is an error in the ATC HPS CONFIGURATION SETTINGS. If the user experiences trouble, please double-check these settings.
- In some cases, it is only a matter of changing the time of day that pick lists are sent to the ATC to avoid peak loads on the VistA computer system.
- In other cases, it has simply been a matter of adjusting the RESPONSE TIMER- CONTROL and/or RESPONSE TIMER-DATA settings within the HPS CONFIGURATION settings.
- If all else fails and the interface still does not want to work, the user may consider setting the USE OLD INTERFACE flag in the WARD GROUP file (#57.5) for all ward groups that will be sending pick lists to the ATC. (See the Ward Groups section in the *Inpatient Medications Supervisor's User Manual*.)

> (*This page included for two-sided copying*.)

### From: PSJ*5*222 Technical Manual/Security Guide Change Pages

### Do Not Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSGXR\* PSJIP\* PSJXR\*

> The PSGXR\* and PSJXR\* routines are created by VA FileMan when it compiles the cross- references of the NON-VERIFIED ORDERS (#53.1) and PHARMACY PATIENT (#55) files.

### From: PSJ*5*178 Technical Manual/Security Guide Change Pages

## Hardware Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files.

## Software Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The type of printer will determine the next step. The Zebra printer requires Control Codes where the Dot Matrix or Laser printers do not require these codes. The IV label print routine checks the existence of the Control Codes before attempting to execute. It is not required for all Control Codes to be defined; just build the necessary Control Codes for the selected printer.

### Zebra Printers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For this type of printer to print a Unique Bar Code on the IV labels, IRM must build Control Codes. The CONTROL CODES fields are added to the TERMINAL TYPE file (#3.2) in the Kernel patch XU\*8\*205. This patch must be installed before proceeding.

> <u>Control Code Set Up</u>

> The IV label print uses twelve control codes presently. These control codes must be built with FileMan using the names listed in order for the routine to work correctly. These twelve codes are listed below:

> <u>Code</u> <u>Description</u>

> FI Format Initialization

> FE Format End

November 2005 Inpatient Medications V. 5.0 73

> Technical Manual/Security Guide

> <u>Code</u> <u>Description</u>

> SL Start of Label

> EL End of Label

> SB Start of Bar Code

> EB End of Bar Code

> SBF Start of Bar Code Field

> EBF End of Bar Code Field

> ST Start of Text

> ET End of Text

> STF Start of Text Field

> ETF End of Text Field

> Patch PSJ\*5\*178 provides the ability to make the medication route print on the IV labels as well as making it appear in a larger font than the other text. The following new control codes must be set up to provide this functionality:

> <u>Code</u> <u>Description</u>

> SM Start Med Route

> EM End Med Route

> SMF Start Med Route Field

> EMF End Med Route Field <u>Pseudo-Code Listing</u>

> The following pseudo-code listing shows the flow and the points at which each of the

> CONTROL CODES are used. (It is not required for all Control Codes to be defined; just build the necessary Control Codes for the selected printer.)

1.  Label print routine invoked.
2.  CONTROL CODES loaded into local array PSJIO. Variable PSJIO defined to indicate whether or not CONTROL CODES exist.
3.  Format Initialization.
4.  If selected, header label printed.
    1.  Start of Label.
    2.  Start of Text.\*
    3.  Start of Text Field.\*
    4.  Text Information.\*
    5.  End of Text Field.\*
    6.  End of Text.\*
    7.  End of Label.
5.  IV label printed.
    1.  Start of Label.
    2.  Barcode unique ID assigned.
    3.  Print barcode.
        1.  If no CONTROL CODES, check for IOBARON and execute.
        2.  If CONTROL CODES, Start of Barcode, Start of Barcode Field.
        3.  Unique ID printed.
        4.  If no CONTROL CODES, check for IOBAROFF and execute.
        5.  If CONTROL CODES, End of Barcode Field, End of Barcode.
    4.  Start of Text.\*

> 74 Inpatient Medications V. 5.0 February 2007 Technical Manual/Security Guide

> PSJ\*5\*178

5.  Start of Text Field.\*
6.  Text Information.\*
7.  End of Text Field.\*
8.  End of Text.\*
9.  End of Label.
6.  Format End.

> In the event the label text needs to continue on another label, the following CONTROL CODE sequence will be used.

1.  End of Label.
2.  Start of Label.

> '\*' indicates items that may be executed repeatedly.

> <u>Example Set Up</u>

> The following is a setup example that was used in the development process. This example is provided to guide the user in this set up. Please note that it is only an example and may not hold true in all cases.

> Example: Zebra Printer Example Set Up

### Dot Matrix and Laser Printers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Control Codes in the TERMINAL TYPE file (#3.2) are not required for these printers. However, the BAR CODE ON and BAR CODE OFF fields in the TERMINAL TYPE file (#3.2) are needed.

February 2007 Inpatient Medications V. 5.0 75

> Technical Manual/Security Guide PSJ\*5\*178

> An example of each field is shown below for the Output Technology Corporation (OTC) printers. Please note that it is only an example and may not hold true in all cases.

> Example: OTC Printer Example

## Printed Bar Code IV Label Sample

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> With this interface, a Unique Bar Code will be printed on the first line of the IV label with the label number printed below it. This label number is comprised of the patient IEN, a "V" as a delimiter, and the label sequential number for the patient (not the order). Depending upon the type of printer used, the asterisks (\*) may or may not be printed on either side of the label number.

> Example: Bar Code IV Label Example

![](psj-5-178-technical-manual-security-guide-change-pages/002.png)

> 76 Inpatient Medications V. 5.0 February 2007 Technical Manual/Security Guide

> PSJ\*5\*178
