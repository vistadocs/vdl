---
title: PSS*1*147 Technical Manual/Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: null
app_code: PSS
app_name: 'Pharmacy: Data Management'
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*147
group_key: PSS:PSS:1
file_numbers:
- '2'
- '3'
- '6'
- '7.1'
- '8'
- '9'
- '18'
- '20.412'
- '31'
- '50'
- '50.02'
- '50.0903'
- '50.1'
- '50.3'
- '50.606'
- '50.7'
- '51'
- '51.1'
- '51.2'
- '51.23'
- '51.24'
- '51.7'
- '52.6'
- '52.7'
- '59'
- '59.7'
- '101'
- '101.43'
- '105'
- '105.2'
- '400'
- '2005'
- '2006'
- '2007'
- '900001'
security_keys:
- PSA ORDERS
- PSDMGR
- PSJI MGR
- PSORPH
menu_options: 5
description: '> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the exi'
audience: Technical staff, IRM, system administrators
keywords: []
page_count: 0
word_count: 11406
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: September 1997
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p147_tm_cp.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p147_tm_cp.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=93
audit_applied: '2026-05-31'
master_source: PSS*1*147 Technical Manual/Security Guide Change Pages
master_pub_date: September 1997
consolidated_from: 12 versions
prior_versions:
- PSS*1*112 Technical Manual/Security Guide Change Pages
- PSS*1*129 Technical Manual/Security Guide Change Pages
- PSS*1*140 Technical Manual/Security Guide Change Pages
- PSS*1*141 Technical Manual/Security Guide Change Pages
- PSS*1*142 Technical Manual/Security Guide Change Pages
- PSS*1*153 Technical Manual/Security Guide Change Pages
- PSS*1*155 Technical Manual/Security Guide Change Pages
- PSS*1*159 Technical Manual/Security Guide Change Pages
- PSS*1*167 Technical Manual/Security Guide Change Pages
- PSS*1*172 Technical Manual/Security Guide Change Pages
- PSS*1*94 Technical Manual/Security Guide Change Pages
consolidated_title: technical manual/security guide change pages
---

> ![](pss-1-147-technical-manual-security-guide-change-pages/001.png)

PHARMACY DATA MANAGEMENT

> TECHNICAL MANUAL/ SECURITY GUIDE

> Version 1.0

> September 1997

> (Revised February 2010)

> Department of Veterans Affairs Office of Enterprise Development

> <span id="_bookmark0" class="anchor"></span> Revision History

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 52%" />
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
<p>02/10</p>
</blockquote></td>
<td><blockquote>
<p>i-iii, 5, 8, 24f,</p>
<p>25, 29-30,</p>
<p>31b- 32, 32a-</p>
<p>32h, 45-50</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*147</p>
</blockquote></td>
<td><blockquote>
<p>Updated patch references to include PSS*1*147. Described files, fields, options and routines added/modified as part of this patch. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/09</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0"><u>i-ii</u>,</a> <a href="#_bookmark1"><u>5</u>,</a> <a href="#_bookmark2"><u>8</u></a></p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*141</p>
</blockquote></td>
<td><blockquote>
<p>Updated patch references to include PSS*1*141. Added ASSOCIATED IMMUNIZATION field (#9) to the PHARMACY ORDERABLE ITEM file (#50.7).</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>08/09</p>
</blockquote></td>
<td><blockquote>
<p>24f</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*140</p>
</blockquote></td>
<td><blockquote>
<p>Added new option <em>Default Med Route OI Rpt</em> [PSS DEF MED ROUTE OI RPT].</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>02/09</p>
</blockquote></td>
<td><blockquote>
<p>i-ii, 24b-f, 25, 29-31b,</p>
<p>48-52, 55-58</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*129</p>
</blockquote></td>
<td><blockquote>
<p>Pharmacy Re-Engineering (PRE) V.0.5 Pre-Release. Restructured main PSS MGR menu and added new <em>Enhanced Order Checks Setup Menu</em>. Described files, fields, options and routines added/modified as part of this project.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>08/08</p>
</blockquote></td>
<td><blockquote>
<p>iii, 25, 33-34</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*94</p>
</blockquote></td>
<td><blockquote>
<p>Added Medication Routes and Administration Scheduling sections. Added PSSSCHED routine.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/06</p>
</blockquote></td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*112</p>
</blockquote></td>
<td><blockquote>
<p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routines PSS55MIS and PSS50TMP to the Routine List.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>09/06</p>
</blockquote></td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*108</p>
</blockquote></td>
<td><blockquote>
<p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routine PSS551 to the Routine List.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04/06</p>
</blockquote></td>
<td><blockquote>
<p>i, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*90</p>
</blockquote></td>
<td><blockquote>
<p>HIPAA NCPDP Global project. Added routines PSSDAWUT and PSSNDCUT to the Routine List. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04/06</p>
</blockquote></td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*106</p>
</blockquote></td>
<td><blockquote>
<p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routine PSS781 to the Routine List.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 52%" />
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
<p>11/05</p>
</blockquote></td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*101</p>
</blockquote></td>
<td><blockquote>
<p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routines PSS55 and PSS59P7 to the Routine List.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/05</p>
</blockquote></td>
<td><blockquote>
<p>i, ii, 24a, 25, 29-31, 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*87</p>
</blockquote></td>
<td><blockquote>
<p>Laser Labels Phase II project. Added <em>Warning Builder</em> and <em>Warning Mapping</em> options descriptions and updated the menu options. Added four new routines to the routine list. Cleaned up misspelled words and such on many pages. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10/04</p>
</blockquote></td>
<td><blockquote>
<p>i., 25, 33</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*85</p>
</blockquote></td>
<td><blockquote>
<p>Added routines and a reference to the <em>Pharmacy Re- Engineering (PRE) Application Program Interface (API) Manual</em> created for the Pharmacy Re-Engineering (PRE) project Encapsulation cycle 1.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/04</p>
</blockquote></td>
<td><blockquote>
<p>i, 24a, 25, 29-</p>
<p>31, 32d-h, 48,</p>
<p>53</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*82</p>
</blockquote></td>
<td><blockquote>
<p>Updated the option description to include <em>Send Entire Drug File to External Interface</em> [PSS MASTER FILE ALL] option. Added new master file update information to the "HL7 Messaging with an External System" section. Updated routine list to include PSSMSTR. Updated the web address for the VistA Documentation Library (VDL).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>07/03</p>
</blockquote></td>
<td><blockquote>
<p>i, 25, 31, 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*61</p>
</blockquote></td>
<td><blockquote>
<p>Updated routine list to four new add PKI routines. Added new <em>Controlled Substances/PKI Reports</em> [PSS/PKI REPORTS] menu and four associated report options to the <em>Pharmacy Data Management</em> [PSS MGR] menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04/03</p>
</blockquote></td>
<td><blockquote>
<p>i, 5, 8, 29, 35,</p>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*68</p>
</blockquote></td>
<td><blockquote>
<p>Updated patch references to include PSS*1*68. Added NON-VA MED field (#8) to the PHARMACY ORDERABLE ITEM file (#50.7).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/03</p>
</blockquote></td>
<td><blockquote>
<p>i., 5, 8, 24a,</p>
<p>29, 31, 35, 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*47</p>
</blockquote></td>
<td><blockquote>
<p>Updated patch references to include PSS*1*47. Added new field OTHER LANGUAGE INSTRUCTIONS (#7.1) to the PHARMACY</p>
<p>ORDERABLE ITEM file (#50.7) list and <em>Other Language Translation Setup</em> option description.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11/02</p>
</blockquote></td>
<td><blockquote>
<p>i, ii 5, (6)</p>
<p>23 - 25, (26)</p>
<p>29-30,(47), 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*55</p>
</blockquote></td>
<td><blockquote>
<p>Renumbered front matter starting from this Revision History page. Updated Patch number. Updated Option descriptions to include <em>Drug Text File Report</em> option. Added routine PSSDTR in the Routines section. Added the <em>Drug Text File Report</em> option to the current PDM Menu in the Exported Options section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10/02</p>
</blockquote></td>
<td><blockquote>
<p>Title, i-iv, 32a-32d</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*57</p>
</blockquote></td>
<td><blockquote>
<p>Updated Title Page, Revision Page and Table of Contents. A section was added for the new HL7 Messaging with an External System.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>09/01</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*38</p>
</blockquote></td>
<td><blockquote>
<p>Added this Revision History Page. Added Patch Release changes and Pharmacy Ordering Enhancements (POE) edits. Updated manual to comply with current documentation standards.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>09/97</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>Original Release of Technical Manual.</p>
</blockquote></td>
</tr>
</tbody>
</table>
# Implementation and Maintenance


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Implementation and Maintenance](#implementation-and-maintenance)
- [Routines](#routines)
- [Protocols](#protocols)
- [HL7 Messaging with an External System](#hl7-messaging-with-an-external-system)
  - [New Protocol](#new-protocol)
  - [HL7 Drug Message Segment Definition Table](#hl7-drug-message-segment-definition-table)
  - [New Protocol](#new-protocol-1)
  - [Specific Transaction](#specific-transaction)
  - [Example:](#example)
  - [HL7 Drug Message Segment Definition Table](#hl7-drug-message-segment-definition-table-1)
- [Security Management](#security-management)
- [Mail Groups](#mail-groups)
- [Alerts](#alerts)
- [Remote Systems](#remote-systems)
- [Archiving/Purging](#archivingpurging)
- [Contingency Planning](#contingency-planning)
- [Interfacing](#interfacing)
- [Electronic Signatures](#electronic-signatures)
- [Menus](#menus)
- [Security Keys](#security-keys)
> The PHARMACY ORDERABLE ITEM file (#50.7) must be built prior to the installation of Outpatient Pharmacy V. 7.0 and Inpatient Medications V. 5.0. The PHARMACY ORDERABLE ITEM file (#50.7) will be similar to the PRIMARY DRUG file (#50.3) used by Inpatient Medications V. 4.5. The main difference is that each entry in the PHARMACY ORDERABLE ITEM file (#50.7) has an associated Dosage Form that will always print next to the name. The PHARMACY ORDERABLE ITEM file (#50.7) will be duplicated in the ORDERABLE ITEM file (#101.43) that will reside in CPRS V. 1.0. Any update to the PHARMACY ORDERABLE ITEM file (#50.7) will automatically update the corresponding entry in the ORDERABLE ITEM file (#101.43). The NAME field (#.01) and the DOSAGE FORM field (#.02) values in the PHARMACY ORDERABLE ITEM file (#50.7) will print on Outpatient Pharmacy reports, profiles, Inpatient Medication reports, MAR labels etc., in place of the Primary Drug Name.
> The PHARMACY ORDERABLE ITEM file (#50.7) includes the following fields. These fields reflect the package content up to and including the release of patch PSS\*1\*147.
>  These fields were necessary for the initial installation but were deleted following later patches.
> \* These fields were not exported with the initial installation but were added with later patches.
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 39%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>.01</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>NAME</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is the name of the Pharmacy Orderable Item. It is a free text field that can be up to 40 characters in</p>
<p>length.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>.02</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>DOSAGE FORM</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a pointer to the DOSAGE FORM file (#50.606). This is a required field and will always print next to the Pharmacy Orderable Item</p>
<p>name.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>.03</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>IV FLAG</strong></p>
</blockquote></td>
<td><blockquote>
<p>This field will be set to 1 to indicate that the Pharmacy Orderable Item entry is pointed to by either the IV ADDITIVES file (#52.6), or the IV SOLUTIONS file (#52.7). If this field is not set to 1, it indicates that the entry</p>
<p>is pointed to from the DRUG file (#50).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>.04</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>INACTIVE DATE</strong></p>
</blockquote></td>
<td><blockquote>
<p>This will contain the date the entry had</p>
<p>been made inactive.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>.05</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>DAY (nD) or DOSE (nL) LIMIT</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a free text field used to calculate</p>
<p>a default value for the "STOP DATE" prompt of the order.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 39%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>.06</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>MED ROUTE</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a pointer to the MEDICATION ROUTES file (#51.2). If a MED</p>
<p>ROUTE is entered here, it will be used as the default value during order entry when this drug is selected.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>.07</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>SCHEDULE TYPE</strong></p>
</blockquote></td>
<td><blockquote>
<p>This field is a set of codes and will be</p>
<p>used as a default value when selecting this drug in order entry.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>.08</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>SCHEDULE</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a free text field and will be used</p>
<p>as a default value during order entry when this drug is selected.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>.09</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>SUPPLY</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a set of codes with 1 (one) indicating that the Orderable Item is a</p>
<p>supply.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>2</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>SYNONYM (multiple)</strong></p>
</blockquote></td>
<td><blockquote>
<p>This multiple will contain all the</p>
<p>associated synonyms for the Pharmacy Orderable Item.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p><strong>.01</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>SYNONYM</strong></p>
</blockquote></td>
<td><blockquote>
<p>A free text synonym name up to 30</p>
<p>characters long.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>3</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>CORRESPONDING UD ITEM</strong></p>
</blockquote></td>
<td><blockquote>
<p>If CHANGE TYPE OF ORDER</p>
<p>FROM OERR field (#20.412) in the PHARMACY SYSTEM file (#59.7)</p>
<p>parameter in Inpatient Mediations package is set, this field will be asked to user. This field will indicate corresponding Orderable Items to choose from and which package (UD or IV) to finish the order.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>4</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>CORRESPONDING IV ITEM</strong></p>
</blockquote></td>
<td><blockquote>
<p>If CHANGE TYPE OF ORDER</p>
<p>FROM OERR field (#20.412) in the PHARMACY SYSTEM file (#59.7)</p>
<p>parameter in Inpatient Mediations package is set, this field will be asked to user. This field will indicate corresponding Orderable Items to choose from and which package (UD or IV) to finish the order.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 39%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>*5</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>FORMULARY STATUS</strong></p>
</blockquote></td>
<td><blockquote>
<p>This field will designate the formulary status of the Orderable Item. The non- formulary status will be displayed to the provider next to the selectable list of Orderable Item(s) during CPRS order entry (List Manager and GUI). This field is not editable. The software controls it. An Orderable Item will only be marked as non-formulary if there</p>
<p>are no active Dispense Drugs that are formulary drugs matched to the item.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>*6</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>OI-DRUG TEXT ENTRY</strong></p>
<p><strong>(multiple)</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>*.01</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>OI-DRUG TEXT ENTRY</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a pointer to the DRUG TEXT file (#51.7). This file contains such information as drug restrictions, guidelines and protocols to help assure that medications are being used according to formulary specifications. This information will be seen in CPRS and Pharmacy when a medication order is placed for the Pharmacy Orderable Item. New entries to the DRUG TEXT file (#51.7) must be made through the <em>Drug Text Enter/Edit</em> option.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>*7</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>PATIENT INSTRUCTIONS</strong></p>
</blockquote></td>
<td><blockquote>
<p>The text in this field shall be presented as a default for the Patient Instructions prompt in the Outpatient Pharmacy package when entering orders, if the Dispense Drug selected is matched to this Pharmacy Orderable Item. This text will also be presented during the Outpatient Medication order entry process through CPRS, and the CPRS user can then determine whether or not these Instructions should be part of the order. For all words entered in this field, the software will check for expansions for each word in the MEDICATION INSTRUCTION file</p>
<p>(#51) and expand the word accordingly.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 39%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><span id="_bookmark1" class="anchor"></span><strong>Field Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><span id="_bookmark2" class="anchor"></span><strong>7.1</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>OTHER LANGUAGE INSTRUCTIONS</strong></p>
</blockquote></td>
<td><blockquote>
<p>The text in this field shall be presented as a default for the OTHER PATIENT INSTRUCTIONS prompt in the Outpatient Pharmacy package when entering orders, if the order being entered is for a patient who has designated a preference for another</p>
<p>language.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>8</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>NON-VA MED</strong></p>
</blockquote></td>
<td><blockquote>
<p>This field indicates whether the Pharmacy Orderable Item is selectable as a Non-VA Med (either an herbal supplement, an over-the-counter (OTC) medication, or a prescription drug not dispensed by the VA). This field is not</p>
<p>editable.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>9</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>ASSOCIATED IMMUNIZATION</strong></p>
</blockquote></td>
<td><blockquote>
<p>This field is added by the Immunizations Documentation by BCMA application. A mapping relationship is created between the PHARMACY ORDERABLE ITEM</p>
<p>file (#50.7) and the pointed-to immunization so that a record can be created in the V IMMUNIZATION file (#9000010.11) corresponding to the BCMA administration of an immunization.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>NAME: PSS DOSE UNIT REQUEST</strong></p>
<p>MENU TEXT: Request Change to Dose Unit TYPE: run routine</p>
<p>DESCRIPTION: This option enables a request to be made to have a new entry added, or a current entry changed in the DOSE UNITS (#51.24) File.</p>
<p>ROUTINE: DOSE^PSSMEDRQ</p>
<p>UPPERCASE MENU TEXT: REQUEST CHANGE TO DOSE UNIT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>NAME: PSS MARK PREMIX SOLUTIONS</strong></p>
<p>MENU TEXT: Mark PreMix Solutions TYPE: run routine</p>
<p>DESCRIPTION: This option will be used to mark entries from the IV SOLUTIONS (#52.7) File as PreMixes, by allowing editing of the PREMIX (#18) Field.</p>
<p>ROUTINE: EDIT^PSSPRUTL</p>
<p>UPPERCASE MENU TEXT: MARK PREMIX SOLUTIONS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>NAME: PSS IV SOLUTION REPORT</strong></p>
<p>MENU TEXT: IV Solution Report TYPE: run routine</p>
<p>DESCRIPTION: This report will display all entries from the IV SOLUTIONS (#52.7) File, or just those entries marked as PreMixes in the PREMIX (#18) Field.</p>
<p>ROUTINE: REP^PSSPRMIX</p>
<p>UPPERCASE MENU TEXT: IV SOLUTION REPORT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>NAME: PSS SCHEDULE REPORT</strong></p>
<p>MENU TEXT: Administration Schedule File Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report of entries from the ADMINISTRATION SCHEDULE (#51.1) File that shows whether or not data has been entered in the FREQUENCY (IN MINUTES) (#2) Field for the entries. To perform Dosage checks on medication orders, a frequency must be derived from the Schedule of the order.</p>
<p>ROUTINE: EN^PSSSCHRP</p>
<p>UPPERCASE MENU TEXT: ADMINISTRATION SCHEDULE FILE R</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>NAME: PSS MED INSTRUCTION REPORT</strong></p>
<p>MENU TEXT: Medication Instruction File Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report of entries from the MEDICATION INSTRUCTION (#51) File that shows whether or not data has been entered in the FREQUENCY (IN MINUTES) (#31) Field. To perform Dosage checks on medication orders, a frequency must be derived from the Schedule of the order.</p>
<p>ROUTINE: EN^PSSMIRPT</p>
<p>UPPERCASE MENU TEXT: MEDICATION INSTRUCTION FILE RE</p>
</blockquote></td>
</tr>
</tbody>
</table>
> The following option was retrieved from VA FileMan and reflects the new option added to PDM following the installation of PSS\*1\*140.
<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 12%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 10%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p><strong>NAME: PSS MEDICATION ROUTES MGMT</strong></p>
<p>MENU TEXT: Medication Routes Management TYPE: menu</p>
<p>DESCRIPTION: This Sub-Menu contains options related to Medication Routes in both the MEDICATION ROUTES (#51.2) File and the STANDARD MEDICATION ROUTES (#51.23) File.</p>
<p>ITEM: PSS MEDICATION ROUTES EDIT ITEM: PSS MED ROUTE MAPPING REPORT ITEM: PSS MED ROUTE MAPPING CHANGES</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ITEM: PSS MEDICATION ROUTE REQUEST</p>
</blockquote></td>
<td colspan="4" rowspan="2"><blockquote>
<p>This option introduced with PSS*1*140.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ITEM: PSS DEF MED ROUTE OI RPT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS DEF MED ROUTE OI RPT</strong></p>
<p>MENU TEXT: Default Med Route For OI Report TYPE: print</p>
<p>DIC {DIP}: PS(50.7, L.: 0</p>
<p>FLDS: [PSS DEF MED ROUTE FOR OI] BY: [PSS DEF MED DHD: [PSS HDR DEF MED ROUTE]</p>
<p>UPPERCASE MENU TEXT: DEFAULT MED ROUTE FOR OI REPOR</p>
</blockquote></td>
<td><blockquote>
<p>ROUTE</p>
</blockquote></td>
<td><blockquote>
<p>FOR</p>
</blockquote></td>
<td><blockquote>
<p>OI]</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>
> The following options were retrieved from VA FileMan and reflect the new options added to PDM following the installation of patch PSS\*1\*147.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following routines are used by the Pharmacy Data Management package.

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PSS129EN</p>
</blockquote></th>
<th><blockquote>
<p>PSS147EN</p>
</blockquote></th>
<th><blockquote>
<p>PSS147PO</p>
</blockquote></th>
<th><blockquote>
<p>PSS32P3</p>
</blockquote></th>
<th><blockquote>
<p>PSS32P5</p>
</blockquote></th>
<th><blockquote>
<p>PSS50</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSS50A</p>
</blockquote></td>
<td><blockquote>
<p>PSS50A1</p>
</blockquote></td>
<td><blockquote>
<p>PSS50AQM</p>
</blockquote></td>
<td><blockquote>
<p>PSS50ATC</p>
</blockquote></td>
<td><blockquote>
<p>PSS50B</p>
</blockquote></td>
<td><blockquote>
<p>PSS50B1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSS50B2</p>
</blockquote></td>
<td><blockquote>
<p>PSS50C</p>
</blockquote></td>
<td><blockquote>
<p>PSS50C1</p>
</blockquote></td>
<td><blockquote>
<p>PSS50CMP</p>
</blockquote></td>
<td><blockquote>
<p>PSS50D</p>
</blockquote></td>
<td><blockquote>
<p>PSS50DAT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSS50DOS</p>
</blockquote></td>
<td><blockquote>
<p>PSS50E</p>
</blockquote></td>
<td><blockquote>
<p>PSS50F</p>
</blockquote></td>
<td><blockquote>
<p>PSS50F1</p>
</blockquote></td>
<td><blockquote>
<p>PSS50LAB</p>
</blockquote></td>
<td><blockquote>
<p>PSS50NDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSS50P4</p>
</blockquote></td>
<td><blockquote>
<p>PSS50P66</p>
</blockquote></td>
<td><blockquote>
<p>PSS50P7</p>
</blockquote></td>
<td><blockquote>
<p>PSS50P7A</p>
</blockquote></td>
<td><blockquote>
<p>PSS50TMP</p>
</blockquote></td>
<td><blockquote>
<p>PSS50WS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSS51</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P1</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P15</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P1A</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P1B</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P1C</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSS51P2</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P5</p>
</blockquote></td>
<td><blockquote>
<p>PSS52P6</p>
</blockquote></td>
<td><blockquote>
<p>PSS52P6A</p>
</blockquote></td>
<td><blockquote>
<p>PSS52P6B</p>
</blockquote></td>
<td><blockquote>
<p>PSS52P7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSS52P7A</p>
</blockquote></td>
<td><blockquote>
<p>PSS54</p>
</blockquote></td>
<td><blockquote>
<p>PSS55</p>
</blockquote></td>
<td><blockquote>
<p>PSS551</p>
</blockquote></td>
<td><blockquote>
<p>PSS55MIS</p>
</blockquote></td>
<td><blockquote>
<p>PSS59P7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSS781</p>
</blockquote></td>
<td><blockquote>
<p>PSSADDIT</p>
</blockquote></td>
<td><blockquote>
<p>PSSADRPT</p>
</blockquote></td>
<td><blockquote>
<p>PSSAUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSSCHENV</p>
</blockquote></td>
<td><blockquote>
<p>PSSCHPRE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSCHPST</p>
</blockquote></td>
<td><blockquote>
<p>PSSCLDRG</p>
</blockquote></td>
<td><blockquote>
<p>PSSCOMMN</p>
</blockquote></td>
<td><blockquote>
<p>PSSCPRS</p>
</blockquote></td>
<td><blockquote>
<p>PSSCPRS1</p>
</blockquote></td>
<td><blockquote>
<p>PSSCREAT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSCSPD</p>
</blockquote></td>
<td><blockquote>
<p>PSSDAWUT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDDUT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDDUT2</p>
</blockquote></td>
<td><blockquote>
<p>PSSDDUT3</p>
</blockquote></td>
<td><blockquote>
<p>PSSDEE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSDEE1</p>
</blockquote></td>
<td><blockquote>
<p>PSSDEE2</p>
</blockquote></td>
<td><blockquote>
<p>PSSDELOI</p>
</blockquote></td>
<td><blockquote>
<p>PSSDENT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDFEE</p>
</blockquote></td>
<td><blockquote>
<p>PSSDGUPD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSDI</p>
</blockquote></td>
<td><blockquote>
<p>PSSDIN</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOS</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSCR</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSCX</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSDOSER</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSRP</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSDAT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSPON</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSPOP</p>
</blockquote></td>
<td><blockquote>
<p>PSSDTR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSENV</p>
</blockquote></td>
<td><blockquote>
<p>PSSENVN</p>
</blockquote></td>
<td><blockquote>
<p>PSSFIL</p>
</blockquote></td>
<td><blockquote>
<p>PSSFILED</p>
</blockquote></td>
<td><blockquote>
<p>PSSFILES</p>
</blockquote></td>
<td><blockquote>
<p>PSSGENM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSGIU</p>
</blockquote></td>
<td><blockquote>
<p>PSSGMI</p>
</blockquote></td>
<td><blockquote>
<p>PSSGS0</p>
</blockquote></td>
<td><blockquote>
<p>PSSGSH</p>
</blockquote></td>
<td><blockquote>
<p>PSSHELP</p>
</blockquote></td>
<td><blockquote>
<p>PSSHL1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSHLSCH</p>
</blockquote></td>
<td><blockquote>
<p>PSSHLU</p>
</blockquote></td>
<td><blockquote>
<p>PSSJEEU</p>
</blockquote></td>
<td><blockquote>
<p>PSSJORDF</p>
</blockquote></td>
<td><blockquote>
<p>PSSJSPU</p>
</blockquote></td>
<td><blockquote>
<p>PSSJSPU0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSJSV</p>
</blockquote></td>
<td><blockquote>
<p>PSSJSV0</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR1</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR10</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR11</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSJXR12</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR13</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR14</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR15</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR16</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR17</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSJXR18</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR19</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR2</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR20</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR21</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR22</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSJXR4</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR5</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR6</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR7</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR8</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR9</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSLAB</p>
</blockquote></td>
<td><blockquote>
<p>PSSLDALL</p>
</blockquote></td>
<td><blockquote>
<p>PSSLDEDT</p>
</blockquote></td>
<td><blockquote>
<p>PSSLDOSE</p>
</blockquote></td>
<td><blockquote>
<p>PSSLDOSE</p>
</blockquote></td>
<td><blockquote>
<p>PSSLOOK</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSMARK</p>
</blockquote></td>
<td><blockquote>
<p>PSSMATCH</p>
</blockquote></td>
<td><blockquote>
<p>PSSMEDCH</p>
</blockquote></td>
<td><blockquote>
<p>PSSMEDRQ</p>
</blockquote></td>
<td><blockquote>
<p>PSSMEDRT</p>
</blockquote></td>
<td><blockquote>
<p>PSSMEDX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSMIRPT</p>
</blockquote></td>
<td><blockquote>
<p>PSSMRTUP</p>
</blockquote></td>
<td><blockquote>
<p>PSSMRTUX</p>
</blockquote></td>
<td><blockquote>
<p>PSSMSTR</p>
</blockquote></td>
<td><blockquote>
<p>PSSNDCUT</p>
</blockquote></td>
<td><blockquote>
<p>PSSNOUNR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSNTEG</p>
</blockquote></td>
<td><blockquote>
<p>PSSOICT</p>
</blockquote></td>
<td><blockquote>
<p>PSSOICT1</p>
</blockquote></td>
<td><blockquote>
<p>PSSOPKI</p>
</blockquote></td>
<td><blockquote>
<p>PSSOPKI1</p>
</blockquote></td>
<td><blockquote>
<p>PSSORPH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSORPH1</p>
</blockquote></td>
<td><blockquote>
<p>PSSORUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSSOUTSC</p>
</blockquote></td>
<td><blockquote>
<p>PSSPKIPI</p>
</blockquote></td>
<td><blockquote>
<p>PSSPKIPR</p>
</blockquote></td>
<td><blockquote>
<p>PSSPNSRP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSPO129</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOI</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIC</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOID1</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOID2</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOID3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSPOIDT</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIKA</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIM</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIM1</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIM2</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIM3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSPOIMN</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIMO</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOST</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOST1</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOST2</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOST5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSPRE</p>
</blockquote></td>
<td><blockquote>
<p>PSSPRETR</p>
</blockquote></td>
<td><blockquote>
<p>PSSPRMIX</p>
</blockquote></td>
<td><blockquote>
<p>PSSPRUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSSQORD</p>
</blockquote></td>
<td><blockquote>
<p>PSSREF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSREMCH</p>
</blockquote></td>
<td><blockquote>
<p>PSSSCHED</p>
</blockquote></td>
<td><blockquote>
<p>PSSSCHRP</p>
</blockquote></td>
<td><blockquote>
<p>PSSSOLI1</p>
</blockquote></td>
<td><blockquote>
<p>PSSSOLIT</p>
</blockquote></td>
<td><blockquote>
<p>PSSSPD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSSUTIL</p>
</blockquote></td>
<td><blockquote>
<p>PSSSYN</p>
</blockquote></td>
<td><blockquote>
<p>PSSTRENG</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTIL</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTLA1</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTLPR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSVIDRG</p>
</blockquote></td>
<td><blockquote>
<p>PSSVX6</p>
</blockquote></td>
<td><blockquote>
<p>PSSVX61</p>
</blockquote></td>
<td><blockquote>
<p>PSSVX62</p>
</blockquote></td>
<td><blockquote>
<p>PSSVX63</p>
</blockquote></td>
<td><blockquote>
<p>PSSVX64</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSVX65</p>
</blockquote></td>
<td><blockquote>
<p>PSSVX66</p>
</blockquote></td>
<td><blockquote>
<p>PSSWMAP</p>
</blockquote></td>
<td><blockquote>
<p>PSSWRNA</p>
</blockquote></td>
<td><blockquote>
<p>PSSWRNB</p>
</blockquote></td>
<td><blockquote>
<p>PSSWRNE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSYSP</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

> The PDM menu that was exported with the original PDM package has been modified to include subsequent changes and patches.

> The PDM menu up to and including PSS\*1\*147 appears below. PSS\*1\*147 was the last patch to affect a change to the PDM menu.

> Pharmacy Data Management \[PSS MGR\]

> CMOP Mark/Unmark (Single drug) \[PSSXX MARK\] ![](pss-1-147-technical-manual-security-guide-change-pages/002.png)

> Dosages…

> \[PSS DOSAGES MANAGEMENT\]

> Auto Create Dosages

> \[PSS DOSAGE CONVERSION\]

> Dosage Form File Enter/Edit \[PSS DOSAGE FORM EDIT\]

> Enter/Edit Dosages \[PSS EDIT DOSAGES\]

> Most Common Dosages Report \[PSS COMMON DOSAGES\]

> Noun/Dosage Form Report

> \[PSS DOSE FORM/ NOUN REPORT\]

> Review Dosages Report

> \[PSS DOSAGE REVIEW REPORT\]

> Local Possible Dosages Report

> \[PSS LOCAL POSSIBLE DOSAGES\]

> Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

> Drug Enter/Edit

> \[PSS DRUG ENTER/ EDIT\]

> Drug Interaction Management… \[PSS DRG INTER MANAGEMENT\]

> Enter/Edit Local Drug Interaction \[PSS INTERACTION LOCAL ADD\]

> Report of Locally Entered Interactions \[PSS REPORT LOCAL INTERACTIONS\]

> Electrolyte File (IV)

> \[PSSJI ELECTROLYTE FILE\]

> Lookup into Dispense Drug File \[PSS LOOK\]

> Medication Instruction Management ...

> \[PSS MED INSTRUCTION MANAGEMENT\]

> Medication Instruction File Add/Edit *\<\<Moved from main PSS MGR menu*

> \[PSSJU MI\]

> Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

> Medication Routes Management ...

> \[PSS MEDICATION ROUTES MGMT\]

> Medication Route File Enter/Edit *\<\<Moved from main PSS MGR menu*

> \[PSS MEDICATION ROUTES EDIT\]

> Medication Route Mapping Report

> \[PSS MED ROUTE MAPPING REPORT\]

> Medication Route Mapping History Report \[PSS MED ROUTE MAPPING CHANGES\]

> Request Change to Standard Medication Route \[PSS MEDICATION ROUTE REQUEST\]

> Default Med Route for OI Report \[PSS DEF MED ROUTE OI RPT\]

> Orderable Item Management

> \[PSS ORDERABLE ITEM MANAGEMENT\]

> Edit Orderable Items

> \[PSS EDIT ORDERABLE ITEMS\]

> Dispense Drug/Orderable Item Maintenance \[PSS MAINTAIN ORDERABLE ITEMS\]

> Enter/Edit Dosages \[PSS EDIT DOSAGES\]

> Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

> Mark PreMix Solutions

> \[PSS MARK PREMIX SOLUTIONS\]

> IV Solution Report

> \[PSS IV SOLUTION REPORT\]

> Administration Schedule File Report \[PSS SCHEDULE REPORT\]

> Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

> IV Additive/Solution Reports…

> \[PSS ADDITIVE/SOLUTION REPORTS\]

> IV Additive Report

> \[PSS IV ADDITIVE REPORT\]

> IV Solution Report

> \[PSS IV SOLUTION REPORT\]

> Warning Builder

> \[PSS WARNING BUILDER\]

> Warning Mapping

> \[PSS WARNING MAPPING\]

> ![](pss-1-147-technical-manual-security-guide-change-pages/003.png) Locked: PSXCMOPMGR

> Without the PSXCMOPMGR key, the *CMOP Mark/Unmark (Single drug)* option will not appear on your menu.

> ![](pss-1-147-technical-manual-security-guide-change-pages/004.png)

> 32 Pharmacy Data Management V. 1.0 February 2010

# Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: PSS EXT MFU CLIENT

> DESCRIPTION: This protocol will be used as the ACK from the external interface for a MFN_M01 message.

> NAME: PSS EXT MFU SERVER

> DESCRIPTION: This protocol will be used to send even notification and data when new drugs are added to the DRUG file (#50) and when certain fields are updated in the same file. This information will be sent to the automated dispensing machines through HL7 V.2.4 formatted messages.

> NAME: PSS HUI DRUG UPDATE

> DESCRIPTION: This protocol will be used to send event notification and data when new drugs are added to the Drug file (#50) and when certain fields are updated in same file.

> NAME: PSS MED ROUTE RECEIVE

> DESCRIPTION: This protocol processes updates to the Standard Medication Routes (#51.23) File.

# HL7 Messaging with an External System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A new protocol, PSS HUI DRUG UPDATE, is exported and has been created to generate HL7 messages when new drugs are added to the DRUG file (#50) and existing entries are updated. This protocol is exported with the text "DELETE ONLY TO SEND DRUG UPDATE MESSAGES" in the DISABLE field (#2) of the PROTOCOL file (#101). To activate the sending of these HL7 messages, the text from the DISABLE field (#2) of the PROTOCOL file (#101) must be deleted and at least one receiving protocol added as a subscriber. The drug data elements included in the HL7 message are defined in the table below.

## HL7 Drug Message Segment Definition Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the PSS HUI DRUG UPDATE protocol is enabled, the following table defines the data elements sent in each segment of the HL7 drug message.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 13%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Piece</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7 TBL</strong></p>
<p><strong># or Data Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>MSH</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Field Separator</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>^~\&amp;</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Encoding Characters</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Pharmacy</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
<p>suggested value</p>
</blockquote></td>
<td><blockquote>
<p>Sending Application</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>MFN</p>
</blockquote></td>
<td><blockquote>
<p>0076</p>
</blockquote></td>
<td><blockquote>
<p>Message Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>MFI</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>50^DRUG^99PSD</p>
</blockquote></td>
<td><blockquote>
<p>0175</p>
</blockquote></td>
<td><blockquote>
<p>Master File ID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>UPD</p>
</blockquote></td>
<td><blockquote>
<p>0178</p>
</blockquote></td>
<td><blockquote>
<p>File-Level Event Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>NE</p>
</blockquote></td>
<td><blockquote>
<p>0179</p>
</blockquote></td>
<td><blockquote>
<p>Response Level Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>MFA</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>MUP/MAD</p>
</blockquote></td>
<td><blockquote>
<p>0180</p>
</blockquote></td>
<td><blockquote>
<p>UPDATE/ADD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>MFE</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>MUP/MAD</p>
</blockquote></td>
<td><blockquote>
<p>0180</p>
</blockquote></td>
<td><blockquote>
<p>UPDATE/ADD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>IEN^DRUG</p>
<p>NAME^99PSD</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>File 50 Entry</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>ZPA</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>NDC</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>National Drug Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>LOCAL NON-</p>
<p>FORMULARY</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>If "1" true</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>INACTIVE DATE</p>
</blockquote></td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>HL7 Format (YYYYMMDD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>APPLICATION</p>
<p>PACKAGE USE</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Used by what packages</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>MESSAGE</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Info on drug</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>VA</p>
<p>CLASSIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>VA Class</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>DEA SPECIAL</p>
<p>HDLG</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>How drug is dispense based on DEA</p>
<p>codes</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>FSN</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Federal Stock #</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>WARNING LABEL</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Drug Warnings for patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>VISN NON-</p>
<p>FORMULAR</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>If '1' true</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 13%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Piece</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7 TBL</strong></p>
<p><strong># or Data Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>ZPB</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>PHARMACY</p>
<p>ORDERABLE ITEM</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>IEN^OI tied to dispense drug^PSD50.7</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>DOSAGE FORM</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>IEN^Dosage Form associated with</p>
<p>OI^PSD50.606</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>MEDICATION</p>
<p>ROUTE</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>IEN^Med Route associated with</p>
<p>OI^PSD51.2</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>PSNDF VA PRODUCT NAME ENTRY</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>IEN^VA PRODUCT NAMES^PSD50.68</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>DISPENSE UNIT</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Dispense Unit for a drug</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>CMOP DISPENSE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>1 or 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>OP EXTERNAL</p>
<p>DISPENSE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>1 or 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>EXPIRATION</p>
<p>DATE</p>
</blockquote></td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>HL7 Format (YYYYMMDD)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>LAB TEST</p>
<p>MONITOR</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>IEN^Lab Test^LAB60</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>ZPC</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>SPECIMEN TYPE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>IEN^ SPECIMEN TYPE^LAB61</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>MONITOR ROUTINE</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Program that runs to find lab test and results</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>LAB MONITOR MARK</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>If '1' true</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>STRENGTH</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>Dose of drug</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>UNIT</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>IEN^Unit of measure^PSD50.607</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>PRICE PER ORDER UNIT</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>PRICE PER</p>
<p>DISPENSE UNIT</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>[{ZPD}]</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>SYNONYM</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Trade Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>NDC CODE</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>National Drug Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>INTENDED USE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE^INTENTED USE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>VSN</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Vendor Stock Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>ORDER UNIT</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>IEN^ABBREVIATION^EXPANSION</p>
<p>^PSD51.5</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>PRICE PER ORDER</p>
<p>UNIT</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>DISPENSE UNITS</p>
<p>PER ORDER UNIT</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 13%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Segment</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Piece</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HL7 TBL</strong></p>
<p><strong># or Data Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>PRICE PER</p>
<p>DISPENSE UNIT</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>VENDOR</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>Vendor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>[{ZPE}]</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVITY LOG</p>
</blockquote></td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>HL7 Format</p>
<p>YYYYMMDDHHMM[SS]-ZZZZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>REASON</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>E^EDIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>INITIATOR OF</p>
<p>ACTIVITY</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>IEN^NEW PERSON^VA200</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>FIELD EDITED</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>NEW VALUE</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>NDF UPDATE</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>[{ZPF}]</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>DISPENSE UNITS</p>
<p>PER DOSE</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>DOSE</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>PACKAGE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE^PACKAGE(S)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>BCMA UNITS PER</p>
<p>DOSE</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>[{ZPG}]</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>CLOZAPINE LAB</p>
<p>TEST</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>IEN^LAB TEST^LAB60</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>MONITOR MAX</p>
<p>DAYS</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>SPECIMEN TYPE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>IEN^ SPECIMEN TYPE^LAB61</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>TYPE OF TEST</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>1^WBC or 2^ANC</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>[{ZPH}]</strong></p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>LOCAL POSSIBLE</p>
<p>DOSAGE</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>FREE TEXT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>PACKAGE</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>CE^PACKAGE(S)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>BCMA UNITS PER</p>
<p>DOSE</p>
</blockquote></td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

## New Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Two new protocols, PSS EXT MFU CLIENT and PSS EXT MFU SERVER, are exported and have been created to generate HL7 messages when new drugs are added to the DRUG file (#50) and existing entries are updated. These protocols can only be activated by setting the following parameters in the OUTPATIENT SITE file (#59):

- AUTOMATED DISPENSE field (#105) needs to be set to 2.4.
- ENABLE MASTER FILE UPDATE field (#105.2) needs to be set to YES.
- LOGICAL LINK field (#2005) needs to be set to PSO DISP.
- DISPENSE DNS NAME field (#2006) needs to be set to the dispensing system DNS name (for example, dispensemachine1.vha.med.va.gov).
- DISPENSE DNS PORT field (#2007) needs to be set to the dispensing system port number.

## Specific Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Pharmacy/Treatment Encoded Order Message is as follows:

> <u>MFN Master File Notification Message</u> MSH Message Header

> MFI Master File Identifier

> {MFE Master File Entry

> {{ZPA} Drug File Information

> {RXD} Pharmacy/Treatment Dispense

> {OBR}} Observation Request

> }

## Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MSH\|~^\\\|PSS VISTA\|521~FO-BIRM.VHA.MED.VA.GOV~DNS\|PSS DISPENSE\|~DISPENSE1.VHA.MED.VA.GOV:9300~DNS\|20030701\|\|MFN~M01~MFN_M01\|10001\|P\|2.4\|\|\|AL\|AL MFI\|50~DRUG~99PSD\|\|UPD\|\|\|NE

> MFE\|MUP\|\|\|PROPANTHELINE 15MG TAB

> ZPA\|PROPANTHELINE 15MG TAB\|N\|LFN~Local Non-Formulary~Pharm Formulary Listing\|20031226\|Take with food\|DE200\|6\|P\|50~6505-00-960-8383~LPS50\|8~NO ALCOHOL~LPS54\|229~Bacitracin~LPSD50.7\|3~CAP,ORAL~LPSD50.606\|15~IV PUSH~LPSD51.2\|3643~ATROPINE SO4

> 0.4MG TAB~LPSD50.68\|OP~OP Dispense~99OP\|20030830\|9~Rubella~LLAB60\|72~Hair of Scalp~LLAB61\|PSOCLO1\|N\|100\|20~MG~LPSD50.607\|4.28&USD~UP\|15.64&USD~UP\|TAB\|2\|BLUE HOUSE VENDOR\|0010-0501-33\|TRADENAME

> RXD\|\|\|\|1\|\|\|\|\|1\|\|\|~P&200&LPSD50.0903\|\|\|\|\|\|\|\|\|\|\|\|O OBR\|\|\|\|1102~ACETAZOLAMIDE~LLAB60\|\|\|\|\|\|\|\|\|\|\|70&NECK&LLAB61\|\|\|\|\|\|\|\|\|WBC\|\|\|7

## HL7 Drug Message Segment Definition Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the PSS EXT MFU SERVER protocol is enabled, the following table defines the data elements sent in each segment of the HL7 drug message.

> Segments used in the Master File Update message:

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SEGMENT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>SEQ#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>LEN</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>R/O</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>RP/#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>EXAMPLE</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MSH</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Field Separator</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Encoding Characters</p>
</blockquote></td>
<td><blockquote>
<p>~^\&amp;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0361</p>
</blockquote></td>
<td><blockquote>
<p>Sending Application</p>
</blockquote></td>
<td><blockquote>
<p>PSS VISTA</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0362</p>
</blockquote></td>
<td><blockquote>
<p>Sending Facility – station ID and station DNS name</p>
</blockquote></td>
<td><blockquote>
<p>521~FO- BIRM.MED.VA.</p>
<p>GOV~DNS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0361</p>
</blockquote></td>
<td><blockquote>
<p>Receiving Application</p>
</blockquote></td>
<td><blockquote>
<p>PSS DISPENSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>HD</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0362</p>
</blockquote></td>
<td><blockquote>
<p>Receiving Facility – DNS name and port of</p>
<p>dispensing machine</p>
</blockquote></td>
<td><blockquote>
<p>~DISPENSE.VH A.MED.VA.GOV</p>
<p>:9300~DNS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td>26</td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Date/Time of Message</p>
</blockquote></td>
<td><blockquote>
<p>20040405152416</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td>15</td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>0076</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Message Type</p>
</blockquote></td>
<td><blockquote>
<p>MFN_M01</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>20</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Message Control ID</p>
</blockquote></td>
<td><blockquote>
<p>10001</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>PT</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>0103</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Processing ID</p>
</blockquote></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>VID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>0104</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Version ID</p>
</blockquote></td>
<td><blockquote>
<p>2.4</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0155</p>
</blockquote></td>
<td><blockquote>
<p>Accept Ack. Type</p>
</blockquote></td>
<td><blockquote>
<p>AL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>0155</p>
</blockquote></td>
<td><blockquote>
<p>Application Ack Type</p>
</blockquote></td>
<td><blockquote>
<p>AL</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="9"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MFI</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0175</p>
</blockquote></td>
<td><blockquote>
<p>Master File Identifier</p>
</blockquote></td>
<td><blockquote>
<p>50^DRUG^99PS D</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0178</p>
</blockquote></td>
<td><blockquote>
<p>File-Level Event Code</p>
</blockquote></td>
<td><blockquote>
<p>UPD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0179</p>
</blockquote></td>
<td><blockquote>
<p>Response Level Code</p>
</blockquote></td>
<td><blockquote>
<p>NE</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="9"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MFE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0180</p>
</blockquote></td>
<td><blockquote>
<p>Record-Level Event Code</p>
</blockquote></td>
<td><blockquote>
<p>MUP</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>Varies</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Primary Key Value – MFE</p>
</blockquote></td>
<td><blockquote>
<p>PROPANTHELI</p>
<p>NE 15MG TAB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="9"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ZPA</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>Varies</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Primary Key Value – ZPA</p>
</blockquote></td>
<td><blockquote>
<p>PROPANTHELI</p>
<p>NE 15MG TAB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0136</p>
</blockquote></td>
<td><blockquote>
<p>Is Synonym</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Formulary Listing</p>
</blockquote></td>
<td><blockquote>
<p>LFN~Local Non-</p>
<p>Formulary~Pharm Formulary Listing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>10</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Inactive Date</p>
</blockquote></td>
<td><blockquote>
<p>20031226</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Drug Message</p>
</blockquote></td>
<td><blockquote>
<p>Take with Food</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td>30</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Drug Classification</p>
</blockquote></td>
<td><blockquote>
<p>DE200</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td>10</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>DEA-Schedule Code</p>
</blockquote></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>DEA-Drug Type</p>
</blockquote></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>100</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Stock Number</p>
</blockquote></td>
<td><blockquote>
<p>50~6505-00-960-</p>
<p>8383~LPS50</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>100</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Warning Label</p>
</blockquote></td>
<td><blockquote>
<p>8~NO ALCOHOL~LPS</p>
<p>54</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Segments used in the Master File Update message: (continued)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 25%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SEGMENT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>SEQ#</strong></p>
</blockquote></th>
<th><strong>LEN</strong></th>
<th><blockquote>
<p><strong>DT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>R/O</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>RP/#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TBL#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ELEMENT NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>EXAMPLE</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>100</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Pharmacy Orderable Item</p>
</blockquote></td>
<td><blockquote>
<p>229~Bacitracin~L</p>
<p>PSD50.7</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>100</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Dosage Form</p>
</blockquote></td>
<td><blockquote>
<p>3~CAP,ORAL~L</p>
<p>PSD50.606</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td>100</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Medication Route</p>
</blockquote></td>
<td><blockquote>
<p>15~IV</p>
<p>PUSH~LPSD51.2</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td>100</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Drug Name Identifiers</p>
</blockquote></td>
<td><blockquote>
<p>3643~ATROPIN E SO4 0.4MG</p>
<p>TAB~LPSD50.68</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>100</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Dispense Flags</p>
</blockquote></td>
<td><blockquote>
<p>OP~OP</p>
<p>Dispense~99OP</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>15</td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Drug Expiration Date</p>
</blockquote></td>
<td><blockquote>
<p>20030830</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>17</p>
</blockquote></td>
<td>100</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Lab Test Monitor</p>
</blockquote></td>
<td><blockquote>
<p>9~Rubella~LLAB</p>
<p>60</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td>100</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Specimen Type</p>
</blockquote></td>
<td><blockquote>
<p>72~Hair of</p>
<p>Scalp~LLAB61</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td>10</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Monitor Routine</p>
</blockquote></td>
<td><blockquote>
<p>PSOCLO1</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Lab Monitor Mark</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>21</p>
</blockquote></td>
<td>50</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Strength</p>
</blockquote></td>
<td><blockquote>
<p>100</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Unit</p>
</blockquote></td>
<td><blockquote>
<p>20~MG~LPSD50.</p>
<p>607</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td>50</td>
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Price Per Order Unit</p>
</blockquote></td>
<td><blockquote>
<p>4.28&amp;USD~UP</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>24</p>
</blockquote></td>
<td>50</td>
<td><blockquote>
<p>CP</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Price Per Dispense Unit</p>
</blockquote></td>
<td><blockquote>
<p>15.64&amp;USD~UP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>25</p>
</blockquote></td>
<td>25</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Dispense Unit</p>
</blockquote></td>
<td><blockquote>
<p>TAB</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>50</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Dispense Units Per Order</p>
<p>Unit</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>27</p>
</blockquote></td>
<td>50</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Vendor</p>
</blockquote></td>
<td><blockquote>
<p>BLUE HOUSE</p>
<p>VENDOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>28</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>NDC Code</p>
</blockquote></td>
<td><blockquote>
<p>0010-0501-33</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>29</p>
</blockquote></td>
<td>25</td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Intended Use</p>
</blockquote></td>
<td><blockquote>
<p>TRADE NAME</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="9"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RXD</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>20</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Actual Dispense Amount</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td>20</td>
<td><blockquote>
<p>NM</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Dispense Notes</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>10</td>
<td><blockquote>
<p>CQ</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Total Daily Dose</p>
</blockquote></td>
<td><blockquote>
<p>~P&amp;200&amp;LPSD5</p>
<p>0.0903</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>24</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Dispense Package Method</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="9"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OBR</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>250</td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Universal Service Identifier</p>
</blockquote></td>
<td><blockquote>
<p>1102~ACETAZO LAMIDE~LLAB</p>
<p>60</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>300</td>
<td><blockquote>
<p>CM</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Specimen Source</p>
</blockquote></td>
<td><blockquote>
<p>70&amp;NECK&amp;LLA B61</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>24</p>
</blockquote></td>
<td>3</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Diagnostic Serv Sect ID</p>
</blockquote></td>
<td><blockquote>
<p>WBC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>27</p>
</blockquote></td>
<td>200</td>
<td><blockquote>
<p>TQ</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Quantity/Timing</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Notes pertaining to some of the data elements:

> \[MSH-3\] Sending Application is the station ID along with the DNS name of the sending facility.

> \[MSH-5\] Receiving Application is the DNS name and DNS port number of the dispensing application.

> \[MSH-10\] Message Control ID is the number that uniquely identifies the message. It is returned in MSA-2 of the dispense completion message.

> \[MFI-1\] Master File Identifier is hard-coded to 50~DRUG~99PSD.

> \[MFE-1\] Record-Level Event Code can be either MUP for Update or MAD for Add.

> \[MFE-4\] Primary Key Value – MFE is the GENERIC NAME field (#.01) from the DRUG file (#50).

> \[ZPA-1\] Primary Key Value – ZPA will be the generic name of the drug first and then all synonyms will follow in consecutive ZPA segments.

> \[ZPA-2\] Is Synonym is set to Y or N depending on whether the primary key is a synonym.

> \[ZPA-3\] Formulary Listing will contain LFN and/or VISN is the formulary is not to appear on the Local or VISN formulary.

> \[ZPA-9\] Stock Number is the FSN field (#6) from the DRUG file (#50) or the VSN field (#400) from the SYNONYM subfile (#50.1) of the PRESCRIPTION file (#50).

> \[ZPA-15\] Dispense Flags will indicate if this drug may be dispensed to an external interface and if it is marked to be dispensed at a Consolidated Outpatient Pharmacy (CMOP). If both are yes, the answer would be OP~OP Dispense~Pharm dispense^CMOP~CMOP dispense~Pharm dispense flag.

> \[ZPA-29\] Intended User will be TRADE NAME, QUICK CODE, DRUG ACCOUNTABILITY or CONTROLLED SUBSTANCES.

> \[RXD-4\] Actual Dispense Amount is the BCMA UNITS PER DOSE field (#3) from the POSSIBLE DOSAGES file (#50.0903).

> \[RXD-9\] Dispense Notes is the DISPENSE UNITS PER DOSE field (#.01) from the POSSIBLE DOSAGES file (#50.0903).

> \[RXD-12\] Total Daily Dose will be either P for Possible Dosages or LP for Local Possible Dosages. \[OBR-4\] Universal Service Identifier is used for Clozapine Lab Test.

> \[OBR-15\] Specimen Source is used for Clozapine Specimen Type. \[OBR-24\] Diagnostic Serv Sect ID is used for Clozapine Type of Test.

> \[OBR-27\] Quantity/Timing is used to encode Monitor Max days from the CLOZAPINE LAB TEST file (#50.02).

# Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PDM package does not contain any VA FileMan security codes except for programmer security (@) on the data dictionaries for the PDM files. Security with respect to standard options in the module is implemented by carefully assigning options to users and by the use of security keys.

# Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PSS\*1\*147 creates a new mail group called PSS ORDER CHECKS. The mail group description below was retrieved from VA FileMan. The IRM Pharmacy support and Pharmacy ADPACs (and backups) should at a minimum be added to this mail group.

# Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no alerts in the PDM package.

# Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PDM does not transmit data to any remote system or facility.

# Archiving/Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no archiving and purging functions necessary with the PDM package.

# Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites utilizing the PDM package should develop a local contingency plan to be used in the event of product problems in a live environment. The facility contingency plan must identify the procedure for maintaining functionality provided by this package in the event of system outage. Field station Information Security Officers (ISOs) may obtain assistance from their Regional Information Security Officer (RISO).

# Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no specialized products embedded within or required by the PDM package.

# Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No electronic signatures are utilized in the PDM package.

# Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Pharmacy Data Management* menu that is exported with the initial release of the PDM package is as follows.

> *\*Primary/VA Generic Orderable Item Report*

> *\*VA Generic Orderable Item Report*

> *\*Create Pharmacy Orderable Items*

> *\*Manually Match Dispense Drugs*

> *\*Orderable Item Matching Status CMOP Mark/Unmark (Single drug)*

> *Locked with PSXCMOPMGR Drug Enter/Edit*

> *IMPORTANT:* Once Pharmacy Data Management is installed, the *Outpatient Drug Enter/Edit* and the *Inpatient Medications Dispense Drug Fields* options will be disabled and the *PDM Drug Enter/Edit* option should be used.

> *Drug Interaction Management...*

> *Enter/Edit Local Drug Interaction Edit Drug Interaction Severity*

> *Electrolyte File (IV)*

> *Lookup into Dispense Drug File*

> *Med. Route/Instructions Table Maintenance Medication Instruction File Add/Edit Orderable Item Management...*

> *Edit Orderable Items*

> *Dispense Drug/Orderable Item Maintenance Additive/Solutions, Orderable Items*

> *Orderable Item Report*

> *\*Primary Drug Edit*

> *Pharmacy System Parameters Edit Standard Schedule Edit*

> \* These items are for pre-release only and will be deleted with the installation Outpatient Pharmacy V. 7.0 and Inpatient Medications V. 5.0.

> The PDM menu up to and including the release of PSS\*1\*147 appears below. PSS\*1\*147 was the last patch to affect a change to the PDM menu.

> *CMOP Mark/Unmark (Single drug)* ![](pss-1-147-technical-manual-security-guide-change-pages/005.png) *Dosages ...*

> *Auto Create Dosages Dosage Form File Enter/Edit Enter/Edit Dosages*

> *Most Common Dosages Report Noun/Dosage Form Report Review Dosages Report*

> *Local Possible Dosages Report Request Change to Dose Unit*

> *Drug Enter/Edit*

> *Drug Interaction Management ...*

> *Enter/Edit Local Drug Interaction Report of Locally Entered Interactions*

> *Electrolyte File (IV)*

> *Lookup into Dispense Drug File Medication Instruction Management*

> *Medication Instruction File Add/Edit Medication Instruction File Report*

> *Medication Routes Management Medication Route File Enter/Edit Medication Route Mapping Report*

> *Medication Route Mapping History Report Request Change to Standard Medication Route Default Med Route for OI Report*

> *Orderable Item Management ...*

> *Edit Orderable Items*

> *Dispense Drug/Orderable Item Maintenance Orderable Item/Dosages Report*

> *Patient Instructions Report Orderable Item Report*

> *Formulary Information Report Drug Text Management*

> *Drug Text Enter/Edit Drug Text File Report*

> *Pharmacy System Parameters Edit Standard Schedule Management*

> *Standard Schedule Edit Administration Schedule File Report*

> *Synonym Enter/Edit*

> *Other Language Translation Setup*

> *Controlled Substances/PKI Reports*

> *DEA Spec Hdlg & CS Fed Sch Discrepancy Controlled Substances Not Matched to NDF CS (DRUGS) Inconsistent with DEA Spec Hdlg*

> *CS (Ord. Item) Inconsistent with DEA Spec Hdlg Send Entire Drug File to External Interface*

> *\*\*Enhanced Order Checks Setup Menu*

> *Find Unmapped Local Medication Routes Map Local Medication Route to Standard Medication Route Mapping Report Medication Route File Enter/Edit Medication Route Mapping History Report*

> *Request Change to Standard Medication Route Find Unmapped Local Possible Dosages*

> *Map Local Possible Dosages Local Possible Dosages Report Strength Mismatch Report Enter/Edit Dosages*

> *Request Change to Dose Unit Mark PreMix Solutions*

> *IV Solution Report*

> *Administration Schedule File Report Medication Instruction File Report*

> *IV Additive/Solution Reports IV Additive Report*

> *IV Solution Report Warning Builder Warning Mapping*

> ![](pss-1-147-technical-manual-security-guide-change-pages/006.png)Locked: PSXCMOPMGR

> Without the PSXCMOPMGR key, the *CMOP Mark/Unmark (Single drug)* option will not appear on your menu.

![](pss-1-147-technical-manual-security-guide-change-pages/007.png)

> \*\* This menu is for the Pharmacy Reengineering (PRE) Version 0.5 Pre-Release only and will be deleted with the installation of PRE V. 0.5.

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to mark or edit package specific fields in a DRUG file (#50) entry, the user must hold the corresponding package key. The keys are assigned for the individual packages. PDM does not export any of these keys.

> Package Keys

> Outpatient Pharmacy PSORPH

> Inpatient Medications PSJU MGR

> Inpatient Medications PSJI MGR

> Automatic Replenishment/Ward Stock PSGWMGR

> Drug Accountability/Inventory Interface PSAMGR Drug Accountability/Inventory Interface PSA ORDERS Controlled Substances PSDMGR

> National Drug File PSNMGR

> Consolidated Mail Outpatient Pharmacy PSXCMOPMGR

> Patch PSS\*1\*147 exports the following four security keys, that will be used by the Pharmacy Enterprise Customization System (PECS) application. Only a few users who will be granted access to the PECS application will need one or more keys assigned based on their role.

> Assignment of these keys should be by request only. The security key descriptions were retrieved from VA FileMan.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSS*1*172 Technical Manual/Security Guide Change Pages

### File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following PDM files are exported with the PDM package.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 23%" />
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File#</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>NAME</strong></p>
</blockquote></th>
<th></th>
<th colspan="3"><blockquote>
<p><strong>UPDATE DD</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>DATA COMES USER WITH FILE OVERRIDE</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DRUG</p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>FULL</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>50.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DRUG ELECTROLYTES</p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>FULL</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>50.606</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DOSAGE FORM</p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>FULL</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>YES (MERGE) NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>50.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PHARMACY ORDERABLE</p>
</blockquote></td>
<td><blockquote>
<p>ITEM</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>FULL</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>MEDICATION INSTRUCTION</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>FULL</p>
</blockquote></td>
<td>NO</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>51.1</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ADMINISTRATION SCHEDULE</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>FULL</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>(MERGE)</p>
</blockquote></td>
<td>YES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51.2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>MEDICATION ROUTES</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>FULL</p>
</blockquote></td>
<td>YES</td>
<td><blockquote>
<p>(MERGE)</p>
</blockquote></td>
<td>YES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>51.5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ORDER UNIT</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>FULL</p>
</blockquote></td>
<td>NO</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51.7</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DRUG TEXT</p>
</blockquote></td>
<td colspan="2">FULL</td>
<td></td>
<td colspan="2"><blockquote>
<p>YES (OVERWRITE)</p>
</blockquote></td>
<td>YES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>52.6</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>IV ADDITIVES</p>
</blockquote></td>
<td colspan="2">FULL</td>
<td></td>
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>52.7</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>IV SOLUTIONS</p>
</blockquote></td>
<td colspan="2">FULL</td>
<td></td>
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>53.47</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>INFUSION INSTRUCTIONS</p>
</blockquote></td>
<td colspan="2">FULL</td>
<td></td>
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>54</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>RX CONSULT</p>
</blockquote></td>
<td colspan="2">FULL</td>
<td><blockquote>
<p>(SCREEN)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>55 PHARMACY PATIENT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(Partial</p>
</blockquote></td>
<td><blockquote>
<p>DD)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PARTIAL</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>59.7 PHARMACY SYSTEM</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"><blockquote>
<p>FULL</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>59.73 VENDOR DISABLE/ENABLE</p>
</blockquote></td>
<td colspan="2">FULL</td>
<td colspan="4"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>59.74 VENDOR INTERFACE DATA</p>
</blockquote></td>
<td colspan="2">FULL</td>
<td colspan="4"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### The following non-PDM files are exported with the PDM package.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 15%" />
<col style="width: 21%" />
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File#</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>NAME</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>UPDATE DD</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DATA COMES WITH FILE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>USER OVERRIDE</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><blockquote>
<p>200 NEW PERSON (Partial DD) PARTIAL</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9009032.3</p>
<p>9009032.4</p>
</blockquote></td>
<td><blockquote>
<p>APSP APSP</p>
</blockquote></td>
<td><blockquote>
<p>INTERVENTION INTERVENTION</p>
</blockquote></td>
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
<td><blockquote>
<p>FULL FULL</p>
</blockquote></td>
<td><blockquote>
<p>YES (OVERWRITE)</p>
<p>NO</p>
</blockquote></td>
<td>NO</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9009032.5</p>
</blockquote></td>
<td><blockquote>
<p>APSP</p>
</blockquote></td>
<td><blockquote>
<p>INTERVENTION</p>
</blockquote></td>
<td><blockquote>
<p>RECOMMENDATION</p>
</blockquote></td>
<td><blockquote>
<p>FULL</p>
</blockquote></td>
<td><blockquote>
<p>YES (OVERWRITE)</p>
</blockquote></td>
<td>NO</td>
</tr>
</tbody>
</table>

> *MARk/Unmark Dispense Drugs For Unit Dose*

> \[PSSJU MARK UD ITEMS\]

> *PRimary Solution File (IV)*

> \[PSSJI SOLN\]

> *Check Drug Interaction*

> \[PSS CHECK DRUG INTERACTION\]

*Infusion Instruction Management …*

> \[PSS INFINS MGR\]

*Infusion Instructions Add/Edit*

> \[PSS INFINS ADED\]

> *Infusion Instruction Report*

> \[PSS INFINS RPT\]

> ![](pss-1-172-technical-manual-security-guide-change-pages/005.png)Locked: PSXCM OPM GR

> Without the PSXCMOPMGR key, the *CMOP Mark/Unmark (Single drug)* option will not appear on your menu.

> *(This page included for two-sided copying.)*

### Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The option descriptions below were retrieved from VA FileMan and provide the PDM options following the initial installation of the PDM package.

<table>
<colgroup>
<col style="width: 78%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>PSS MGR Pharmacy Data Management</strong></p>
<p>This menu contains the options necessary to build and maintain the PHARMACY ORDERABLE ITEM file (#50.7), and to also build and maintain the Med. Route/Instructions table.</p>
<p>ITEM: PSS DRUG ENTER/EDIT ITEM: PSS LOOK</p>
<p>ITEM: PSSJI ELECTROLYTE FILE ITEM: PSSXX MARK</p>
<p>ITEM: PSS SYS EDIT</p>
<p>ITEM: PSS ORDERABLE ITEM MANAGEMENT ITEM: PSSNFI</p>
<p>ITEM: PSS SYNONYM EDIT</p>
<p>ITEM: PSS DOSAGES MANAGEMENT ITEM: PSS CS/PKI REPORTS ITEM: PSS MASTER FILE ALL</p>
<p>ITEM: PSS MEDICATION ROUTES MGMT ITEM: PSS SCHEDULE MANAGEMENT ITEM: PSS DRUG TEXT MANAGEMENT</p>
<p>ITEM: PSS MED INSTRUCTION MANAGEMENT ITEM: PSS ORDER CHECK MANAGEMENT ITEM: PSS ADDITIVE/SOLUTION</p>
<p>ITEM: PSS WARNING BUILDER ITEM: PSS WARNING MAPPING ITEM: PSS PEPS SERVICES ITEM: PSS INP MGR</p>
<p>ITEM: PSS Check Drug Interaction ITEM: PSS INFINS MGR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>PSS DRUG ENTER/EDIT</strong></p>
<p>Drug Enter/Edit</p>
<p>This option allows the user to edit fields for ALL pharmacy packages if they package key. It also will allow the user to match to NDF and Orderable Item.</p>
<p>TYPE: run routine ROUTINE: PSSDEE</p>
</blockquote></td>
<td rowspan="2">possess the proper</td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PSS LOOK</strong></p>
<p>Lookup into Dispense Drug File</p>
<p>This option provides a report of all information regarding the dispense drug. TYPE: run routine ROUTINE: PSSLOOK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>PSSJI ELECTROYLYTE FILE</strong></p>
<p><strong>Electrolyte File (IV)</strong></p>
<p>This option will allow you to alter the contents of the DRUG ELECTORYLYTES file (#50.4). This is the file that is pointed to by the ELECTROLYTE field in both the IV ADDITIVES (#52.6) and IV SOLUTIONS (#52.7) files.</p>
<p>TYPE: run routine ROUTINE: ELECTRO^PSSIVDRG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PSSXX MARK</strong></p>
<p>CMOP Mark/Unmark (Single drug)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> December 2013 Pharmacy Data Management V. 1.0 7

<table>
<colgroup>
<col style="width: 78%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>This option allows the user to mark/unmark a single drug for transmission to</p>
<p>TYPE: run routine ROUTINE: PSSMARK</p>
</blockquote></th>
<th>the CMOP.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>PSS SYS EDIT</strong></p>
<p>Pharmacy System Parameters Edit</p>
<p>This option allows the user to edit the Pharmacy System parameters used in Pharmacy Data Management.</p>
<p>TYPE: run routine ROUTINE: PSSYSP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PSS ORDERABLE ITEM MANAGEMENT</strong></p>
<p>Orderable Item Management</p>
<p>This is the sub-menu driver for Orderable Item maintenance. ITEM: PSS MAINTAIN ORDERABLE ITEMS</p>
<p>ITEM: PSS EDIT ORDERABLE ITEMS ITEM: PSS ORDERABLE ITEM DOSAGES ITEM: PSS INSTRUCTIONS/ITEMS REPORT ITEM: PSS ORDERABLE ITEM REPORT</p>
<p>TYPE: menu</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>PSSNFI</strong></p>
<p>Formulary Information Report</p>
<p>This option provides a listing of pertinent pharmacy formulary information. TYPE: run routine ROUTINE: PSSNFI</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>PSS SYNONYM EDIT</strong></p>
<p>Synonym Enter/Edit</p>
<p>The option provides easy access to update the synonym information for an entry in the local DRUG file.</p>
<p>TYPE: run routine ROUTINE: PSSSEE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>PSS DOSAGES MANAGEMENT</strong></p>
<p>Dosages</p>
<p>This menu option contains options that control the editing of dosages. ITEM: PSS DOSAGE FORM EDIT</p>
<p>ITEM: PSS EDIT DOSAGES ITEM: PSS COMMON DOSAGES</p>
<p>ITEM: PSS DOSE FORM/NOUN REPORT ITEM: PSS DOSAGE REVIEW REPORT ITEM: PSS LOCAL POSSIBLE DOSAGES ITEM: PSS DOSE UNIT REQUEST</p>
<p>TYPE: menu</p>
</blockquote></td>
<td rowspan="4"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PSS CS/PKI REPORTS</strong></p>
<p>Controlled Substances/PKI Reports</p>
<p>PKI POST-INSTALL REPORTS PROVIDED AS OPTIONS. ITEM: PSS DEA VS CS FED. SCH. DISCR.</p>
<p>ITEM: PSS CS NOT MATCHED TO NDF ITEM: PSS CS DRUGS INCON WITH DEA ITEM: PSS CS (OI) INCON WITH DEA</p>
<p>TYPE: menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>PSS MASTER FILE ALL</strong></p>
<p>Send Entire Drug File to External Interface</p>
<p>TYPE: run routine ROUTINE: PSSMSTR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PSS MEDICATION ROUTES MGMT</strong></p>
<p>Medication Routes Management</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 78%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>This Sub-Menu contains options related to Medication Routes in both the MEDICATION ROUTES (#51.2) File and the STANDARD MEDICATION ROUTES (#51.23) File.</p>
<p>ITEM: PSS MEDICATION ROUTES EDIT ITEM: PSS MED ROUTE MAPPING REPORT ITEM: PSS MED ROUTE MAPPING CHANGES ITEM: PSS MEDICATION ROUTE REQUEST ITEM: PSS DEF MED ROUTE OI RPT</p>
<p>TYPE: menu</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>PSS SCHEDULE MANAGEMENT</strong></p>
<p>Standard Schedule Management</p>
<p>This Sub-Menu contains options needed for Schedule maintenance. ITEM: PSS SCHEDULE EDIT</p>
<p>ITEM: PSS SCHEDULE REPORT</p>
<p>TYPE: menu</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PSS DRUG TEXT MANAGEMENT</strong></p>
<p>Drug Text Management</p>
<p>This Sub-Menu contains options concerning Drug Text. ITEM: PSS EDIT TEXT</p>
<p>ITEM: PSS DRUG TEXT FILE REPORT</p>
<p>TYPE: menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>PSS MED INSTRUCTION MANAGEMENT</strong></p>
<p>Medication Instruction Management</p>
<p>The Sub-Menu contains options related to the MEDICATION INSTRUCTION (#51) File. ITEM: PSSJU MI</p>
<p>ITEM: PSS MED INSTRUCTION REPORT</p>
<p>TYPE: menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>PSS ORDER CHECK MANAGEMENT</strong></p>
<p>Order Check Management</p>
<p>This is the sub-menu for functionality related to managing medication order checks. ITEM: PSS ORDER CHECK CHANGES</p>
<p>ITEM: PSS REPORT LOCAL INTERACTIONS</p>
<p>TYPE: menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>PSS ADDITIVE/SOLUTION</strong></p>
<p>IV Additive/Solution</p>
<p>This Sub-Menu contains options that can be used to run reports from the IV ADDITIVES (#52.6) File and the IV SOLUTIONS (#52.7) File. It also provides an option to edit the PREMIX (#18) Field in the IV SOLUTIONS (#52.7) File.</p>
<p>ITEM: PSS IV ADDITIVE REPORT ITEM: PSS IV SOLUTION REPORT ITEM: PSS MARK PREMIX SOLUTIONS</p>
<p>TYPE: menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>PSS WARNING BUILDER</strong></p>
<p>Warning Builder</p>
<p>This option will allow you to define a custom warning label list containing entries from both the new warning label source and the old Rx Consult file entries.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 78%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>TYPE: run routine ROUTINE: PSSWRNB</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>PSS WARNING MAPPING</strong></p>
<p>Warning Mapping</p>
<p>This option is used to match an entry from the old Rx Consult file to the new commercial data source warning file to aid in using the Warning Builder (to identify local warnings that do not have an equivalent entry in the new commercial data source). The user can also enter a Spanish translation for an Rx Consult file entry, if desired, but whenever possible, the new commercial data source's warnings (English or Spanish depending on the patient setting) should be used.</p>
<p>TYPE: run routine ROUTINE: EDIT^PSSWMAP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PSS PEPS SERVICES</strong></p>
<p>PEPS</p>
<p>ITEM: PSS CHECK VENDOR DATABASE LINK ITEM: PSS CHECK PEPS SERVICES SETUP ITEM: PSS SCHEDULE PEPS INTERFACE CK <strong>ITEM: PSS VENDOR INTERFACE REPORT</strong></p>
<p>TYPE: menu</p>
</blockquote></td>
<td rowspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>PSS INP MGR</strong></p>
<p>Inpatient Drug Management</p>
<p>This Sub-Menu contains options related to INPATIENT DRUG MANAGEMENT. ITEM: PSSJI DRUG</p>
<p>ITEM: PSSJU DRG</p>
<p>ITEM: PSSJU DRUG/ATC SET UP ITEM: PSSJU DCC</p>
<p>ITEM: PSSJI EDIT DRUG COST ITEM: PSSJU MARK UD ITEMS ITEM: PSSJI SOLN</p>
<p>TYPE: Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PSS CHECK DRUG INTERACTION</strong></p>
<p>Check Drug Interaction</p>
<p>This menu contains options pertaining to maintaining pharmacy</p>
<p>data files, creating Pharmacy Orderable Items, and the Medication Route/ Instructions table among other assorted functions.</p>
<p>TYPE: run routine ROUTINE: PSSDIUTL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>PSS INFINS MGR</strong></p>
<p>Infusion Instruction Management</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following routines are used by the Pharmacy Data Management package.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PSS0052</p>
</blockquote></th>
<th><blockquote>
<p>PSS0093</p>
</blockquote></th>
<th><blockquote>
<p>PSS0114</p>
</blockquote></th>
<th><blockquote>
<p>PSS102RP</p>
</blockquote></th>
<th><blockquote>
<p>PSS117EN</p>
</blockquote></th>
<th><blockquote>
<p>PSS117PO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSS127PI</p>
</blockquote></td>
<td><blockquote>
<p>PSS127PT</p>
</blockquote></td>
<td><blockquote>
<p>PSS129EN</p>
</blockquote></td>
<td><blockquote>
<p>PSS147EN</p>
</blockquote></td>
<td><blockquote>
<p>PSS147PO</p>
</blockquote></td>
<td><blockquote>
<p>PSS160EN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSS160PO</p>
</blockquote></td>
<td><blockquote>
<p>PSS172PO</p>
</blockquote></td>
<td><blockquote>
<p>PSS1P135</p>
</blockquote></td>
<td><blockquote>
<p>PSS1P154</p>
</blockquote></td>
<td><blockquote>
<p>PSS1P23</p>
</blockquote></td>
<td><blockquote>
<p>PSS1P43</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSS32P3</p>
</blockquote></td>
<td><blockquote>
<p>PSS32P5</p>
</blockquote></td>
<td><blockquote>
<p>PSS50</p>
</blockquote></td>
<td><blockquote>
<p>PSS50A</p>
</blockquote></td>
<td><blockquote>
<p>PSS50A1</p>
</blockquote></td>
<td><blockquote>
<p>PSS50AQM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSS50ATC</p>
</blockquote></td>
<td><blockquote>
<p>PSS50B</p>
</blockquote></td>
<td><blockquote>
<p>PSS50B1</p>
</blockquote></td>
<td><blockquote>
<p>PSS50B2</p>
</blockquote></td>
<td><blockquote>
<p>PSS50C</p>
</blockquote></td>
<td><blockquote>
<p>PSS50C1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSS50CMP</p>
</blockquote></td>
<td><blockquote>
<p>PSS50D</p>
</blockquote></td>
<td><blockquote>
<p>PSS50DAT</p>
</blockquote></td>
<td><blockquote>
<p>PSS50DOS</p>
</blockquote></td>
<td><blockquote>
<p>PSS50E</p>
</blockquote></td>
<td><blockquote>
<p>PSS50F</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSS50F1</p>
</blockquote></td>
<td><blockquote>
<p>PSS50LAB</p>
</blockquote></td>
<td><blockquote>
<p>PSS50NDF</p>
</blockquote></td>
<td><blockquote>
<p>PSS50P4</p>
</blockquote></td>
<td><blockquote>
<p>PSS50P66</p>
</blockquote></td>
<td><blockquote>
<p>PSS50P7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSS50P7A</p>
</blockquote></td>
<td><blockquote>
<p>PSS50TMP</p>
</blockquote></td>
<td><blockquote>
<p>PSS50WS</p>
</blockquote></td>
<td><blockquote>
<p>PSS51</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P1</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P15</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSS51P1A</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P1B</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P1C</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P2</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P5</p>
</blockquote></td>
<td><blockquote>
<p>PSS51P5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSS52P6A</p>
</blockquote></td>
<td><blockquote>
<p>PSS52P6B</p>
</blockquote></td>
<td><blockquote>
<p>PSS52P7</p>
</blockquote></td>
<td><blockquote>
<p>PSS52P7A</p>
</blockquote></td>
<td><blockquote>
<p>PSS54</p>
</blockquote></td>
<td><blockquote>
<p>PSS55</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSS551</p>
</blockquote></td>
<td><blockquote>
<p>PSS55MIS</p>
</blockquote></td>
<td><blockquote>
<p>PSS59P7</p>
</blockquote></td>
<td><blockquote>
<p>PSS70UTL</p>
</blockquote></td>
<td><blockquote>
<p>PSS781</p>
</blockquote></td>
<td><blockquote>
<p>PSSADDIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSADRPT</p>
</blockquote></td>
<td><blockquote>
<p>PSSAUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSSBPSUT</p>
</blockquote></td>
<td><blockquote>
<p>PSSCHENV</p>
</blockquote></td>
<td><blockquote>
<p>PSSCHPRE</p>
</blockquote></td>
<td><blockquote>
<p>PSSCHPST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSCLDRG</p>
</blockquote></td>
<td><blockquote>
<p>PSSCLINR</p>
</blockquote></td>
<td><blockquote>
<p>PSSCLOZ</p>
</blockquote></td>
<td><blockquote>
<p>PSSCMOPE</p>
</blockquote></td>
<td><blockquote>
<p>PSSCOMMN</p>
</blockquote></td>
<td><blockquote>
<p>PSSCPRS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSCPRS1</p>
</blockquote></td>
<td><blockquote>
<p>PSSCREAT</p>
</blockquote></td>
<td><blockquote>
<p>PSSCSPD</p>
</blockquote></td>
<td><blockquote>
<p>PSSCUSRQ</p>
</blockquote></td>
<td><blockquote>
<p>PSSDACS</p>
</blockquote></td>
<td><blockquote>
<p>PSSDAWUT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSDDUT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDDUT2</p>
</blockquote></td>
<td><blockquote>
<p>PSSDDUT3</p>
</blockquote></td>
<td><blockquote>
<p>PSSDEE</p>
</blockquote></td>
<td><blockquote>
<p>PSSDEE1</p>
</blockquote></td>
<td><blockquote>
<p>PSSDEE2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSDELOI</p>
</blockquote></td>
<td><blockquote>
<p>PSSDENT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDFEE</p>
</blockquote></td>
<td><blockquote>
<p>PSSDGUPD</p>
</blockquote></td>
<td><blockquote>
<p>PSSDI</p>
</blockquote></td>
<td><blockquote>
<p>PSSDIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSDINT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDIUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOS</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSED</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSER</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSLZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSDOSRP</p>
</blockquote></td>
<td><blockquote>
<p>PSSDRINT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDRDOS</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSAPA</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSAPD</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSAPI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSDSAPK</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSAPL</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSAPM</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSBBP</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSBDA</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSBDB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSDSBPA</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSBPB</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSBPC</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSBPD</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSDAT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSEXC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSDSFDB</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSONF</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSPON</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSPOP</p>
</blockquote></td>
<td><blockquote>
<p>PSSDTR</p>
</blockquote></td>
<td><blockquote>
<p>PSSEC123</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSENV</p>
</blockquote></td>
<td><blockquote>
<p>PSSENVN</p>
</blockquote></td>
<td><blockquote>
<p>PSSFDBDI</p>
</blockquote></td>
<td><blockquote>
<p>PSSFDBRT</p>
</blockquote></td>
<td><blockquote>
<p>PSSFIL</p>
</blockquote></td>
<td><blockquote>
<p>PSSFILED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSFILES</p>
</blockquote></td>
<td><blockquote>
<p>PSSGENM</p>
</blockquote></td>
<td><blockquote>
<p>PSSGIU</p>
</blockquote></td>
<td><blockquote>
<p>PSSGMI</p>
</blockquote></td>
<td><blockquote>
<p>PSSGS0</p>
</blockquote></td>
<td><blockquote>
<p>PSSGSGUI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSGSH</p>
</blockquote></td>
<td><blockquote>
<p>PSSHELP</p>
</blockquote></td>
<td><blockquote>
<p>PSSHFREQ</p>
</blockquote></td>
<td><blockquote>
<p>PSSHL1</p>
</blockquote></td>
<td><blockquote>
<p>PSSHLSCH</p>
</blockquote></td>
<td><blockquote>
<p>PSSHLU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSHRCOM</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRENV</p>
</blockquote></td>
<td><blockquote>
<p>PSSHREQ</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRIT</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRPST</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRQ2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSHRQ2</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRQ22</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRQ23</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRQ2O</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRVAL</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRVL1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSHTTP</p>
</blockquote></td>
<td><blockquote>
<p>PSSHUIDG</p>
</blockquote></td>
<td><blockquote>
<p>PSSIIRPT</p>
</blockquote></td>
<td><blockquote>
<p>PSSJEEU</p>
</blockquote></td>
<td><blockquote>
<p>PSSJORDF</p>
</blockquote></td>
<td><blockquote>
<p>PSSJSPU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSJSPU0</p>
</blockquote></td>
<td><blockquote>
<p>PSSJSV</p>
</blockquote></td>
<td><blockquote>
<p>PSSJSV0</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR1</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR10</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSJXR11</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR12</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR13</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR14</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR15</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSJXR17</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR18</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR19</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR2</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR20</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR21</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSJXR22</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR23</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR24</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR25</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR26</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR27</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSJXR28</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR29</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR3</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR30</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR31</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR32</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSJXR33</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR34</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR4</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR5</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR6</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSJXR8</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR9</p>
</blockquote></td>
<td><blockquote>
<p>PSSLAB</p>
</blockquote></td>
<td><blockquote>
<p>SSLDALL</p>
</blockquote></td>
<td><blockquote>
<p>PSSLDEDT</p>
</blockquote></td>
<td><blockquote>
<p>PSSLDOSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSLOCK</p>
</blockquote></td>
<td><blockquote>
<p>PSSLOOK</p>
</blockquote></td>
<td><blockquote>
<p>PSSMARK</p>
</blockquote></td>
<td><blockquote>
<p>PSSMATCH</p>
</blockquote></td>
<td><blockquote>
<p>PSSMEDCH</p>
</blockquote></td>
<td><blockquote>
<p>PSSMEDRQ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSMEDRT</p>
</blockquote></td>
<td><blockquote>
<p>PSSMEDX</p>
</blockquote></td>
<td><blockquote>
<p>PSSMIRPT</p>
</blockquote></td>
<td><blockquote>
<p>PSSMONT</p>
</blockquote></td>
<td><blockquote>
<p>PSSMRTUP</p>
</blockquote></td>
<td><blockquote>
<p>PSSMRTUX</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSMSTR</p>
</blockquote></td>
<td><blockquote>
<p>PSSNCPDP</p>
</blockquote></td>
<td><blockquote>
<p>PSSNDCUT</p>
</blockquote></td>
<td><blockquote>
<p>PSSNFI</p>
</blockquote></td>
<td><blockquote>
<p>PSSNFIP</p>
</blockquote></td>
<td><blockquote>
<p>PSSNOD2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSNOUNR</p>
</blockquote></td>
<td><blockquote>
<p>PSSNTEG</p>
</blockquote></td>
<td><blockquote>
<p>PSSOICT</p>
</blockquote></td>
<td><blockquote>
<p>PSSOICT1</p>
</blockquote></td>
<td><blockquote>
<p>PSSOIDOS</p>
</blockquote></td>
<td><blockquote>
<p>PSSOPKI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSOPKI1</p>
</blockquote></td>
<td><blockquote>
<p>PSSORPH</p>
</blockquote></td>
<td><blockquote>
<p>PSSORPH1</p>
</blockquote></td>
<td><blockquote>
<p>PSSORPHZ</p>
</blockquote></td>
<td><blockquote>
<p>PSSORUTE</p>
</blockquote></td>
<td><blockquote>
<p>PSSORUTL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSORUTZ</p>
</blockquote></td>
<td><blockquote>
<p>PSSOUTSC</p>
</blockquote></td>
<td><blockquote>
<p>PSSP110</p>
</blockquote></td>
<td><blockquote>
<p>PSSP130</p>
</blockquote></td>
<td><blockquote>
<p>PSSP134</p>
</blockquote></td>
<td><blockquote>
<p>PSSPCH13</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSPI89</p>
</blockquote></td>
<td><blockquote>
<p>PSSPKIPI</p>
</blockquote></td>
<td><blockquote>
<p>PSSPKIPR</p>
</blockquote></td>
<td><blockquote>
<p>PSSPNSRP</p>
</blockquote></td>
<td><blockquote>
<p>PSSPO129</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSPOIC</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOID1</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOID2</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOID3</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIDT</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIKA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSPOIM</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIM1</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIM2</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIM3</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIMN</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOIMO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSPOIMP</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOST</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOST2</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOST5</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOST6</p>
</blockquote></td>
<td><blockquote>
<p>PSSPRE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSPRE38</p>
</blockquote></td>
<td><blockquote>
<p>PSSPRETR</p>
</blockquote></td>
<td><blockquote>
<p>PSSPRMIX</p>
</blockquote></td>
<td><blockquote>
<p>PSSPRUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSSQOC</p>
</blockquote></td>
<td><blockquote>
<p>PSSQORD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSREF</p>
</blockquote></td>
<td><blockquote>
<p>PSSREMCH</p>
</blockquote></td>
<td><blockquote>
<p>PSSRXACT</p>
</blockquote></td>
<td><blockquote>
<p>PSSSCHED</p>
</blockquote></td>
<td><blockquote>
<p>PSSSCHRP</p>
</blockquote></td>
<td><blockquote>
<p>PSSSEE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSTRENG</p>
</blockquote></td>
<td><blockquote>
<p>PSSTXT</p>
</blockquote></td>
<td><blockquote>
<p>PSSUNMSI</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTIL</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTIL1</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTIL3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSUTLA1</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTLA2</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTLAZ</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTLPR</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTLPZ</p>
</blockquote></td>
<td><blockquote>
<p>PSSVIDRG</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PSSVX6</p>
</blockquote></th>
<th><blockquote>
<p>PSSVX61</p>
</blockquote></th>
<th><blockquote>
<p>PSSVX62</p>
</blockquote></th>
<th><blockquote>
<p>PSSVX63</p>
</blockquote></th>
<th><blockquote>
<p>PSSVX64</p>
</blockquote></th>
<th><blockquote>
<p>PSSVX65</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PSSVX66</p>
</blockquote></td>
<td><blockquote>
<p>PSSWMAP</p>
</blockquote></td>
<td><blockquote>
<p>PSSWRNA</p>
</blockquote></td>
<td><blockquote>
<p>PSSWRNB</p>
</blockquote></td>
<td><blockquote>
<p>PSSWRNC</p>
</blockquote></td>
<td><blockquote>
<p>PSSWRNE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSXDIC</p>
</blockquote></td>
<td><blockquote>
<p>PSSXREF</p>
</blockquote></td>
<td><blockquote>
<p>PSSXRF1</p>
</blockquote></td>
<td><blockquote>
<p>PSSYSP</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Stand-Alone Options

> The following is a list of all stand-alone options that are NOT exported as part of the main PDM menu \[PSS MGR\]:

> *Other Language Translation Setup*

> \[PSS OTHER LANGUAGE SETUP\]

> *Drug Inquiry (IV)*

> \[PSSJI DRUG INQUIRY\]

> *Electrolyte File (IV)*

> \[PSSJI ELECTROLYTE FILE\]

> *Enable/Disable Vendor Database Link*

> \[PSS ENABLE/DISABLE DB LINK\]

> *Add Default Med Route*

> \[PSS ADD DEFAULT MED ROUTE\]

> *Find Unmapped Local Possible Dosages*

> \[PSS LOCAL DOSAGES EDIT ALL\]

> ![](pss-1-172-technical-manual-security-guide-change-pages/006.png)The *Enable/Disable Vendor Database Link* option exists ONLY as a way for technical personnel to turn on/off the database connection if required for debugging. Normally, it is enabled and the Vendor Database updates are performed centrally on the MOCHA Servers, not at the individual sites. It is NOT exported as part of the main PDM menu \[PSS MGR\].

> In the rare case where this option is used and the database link is disabled, NO drug-drug interaction, duplicate therapy, or dosing order checks will be performed in Pharmacy or in the Computerized Patient Record System (CPRS).

> Five security keys were introduced with Patch PSS\*1\*167 that will be used to authenticate users accessing the Pharmacy Product System-National (PPS-N) using Kernel Authentication and Authorization for J2EE (KAAJEE). Users requiring access to the Pharmacy Product System-National should be assigned these keys as appropriate to their level of approved access. PPS-N is a reengineered product that will replace the National Drug File Management System (NDFMS). Site users may be assigned the PSS_PPSN_VIEWER key only. The other four security keys are only to be assigned to members of the National NDF Management Group.

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Information about all files, including these, can be obtained by using the VA FileMan to generate a list of file attributes.

#### PDM Files

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 29%" />
<col style="width: 21%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong><u>File</u> <u>Numbers</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>File Names</u></strong></p>
</blockquote></th>
<th><strong><u>DD</u></strong></th>
<th><blockquote>
<p><strong><u>RD</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>WR</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>DEL</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>LAYGO</u></strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><blockquote>
<p>50 DRUG @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>50.4 DRUG ELECTROLYTES @</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>50.606 DOSAGE FORM @ @ @ @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>50.7 PHARMACY ORDERABLE ITEM @</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>51 MEDICATION INSTRUCTION @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>51.1 ADMINISTRATION SCHEDULE @</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>51.2 MEDICATION ROUTES @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>51.23 STANDARD MEDICATION ROUTES @ Pp @ @ @</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>51.24 DOSE UNIT</p>
</blockquote></th>
<th></th>
<th>@</th>
<th><blockquote>
<p>Pp</p>
</blockquote></th>
<th><blockquote>
<p>@</p>
</blockquote></th>
<th>@</th>
<th>@</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><blockquote>
<p>51.5 ORDER UNIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>51.7 DRUG TEXT</p>
</blockquote></td>
<td></td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>52.6 IV ADDITIVES</p>
</blockquote></td>
<td></td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>52.7 IV SOLUTIONS</p>
<p>53.47 INFUSION INSTRUCTIONS</p>
</blockquote></td>
<td></td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>54 RX CONSULT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>55 PHARMACY PATIENT (Partial</p>
</blockquote></td>
<td><blockquote>
<p>DD)</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>P</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>59.7 PHARMACY SYSTEM</p>
</blockquote></td>
<td></td>
<td>^</td>
<td></td>
<td><blockquote>
<p>^</p>
</blockquote></td>
<td>^</td>
<td>^</td>
</tr>
<tr class="even">
<td><blockquote>
<p>59.73 VENDOR DISABLE/ENABLE</p>
</blockquote></td>
<td></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>59.74 VENDOR INTERFACE DATA</p>
</blockquote></td>
<td></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

> Non-PDM Files

<table style="width:100%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 20%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong><u>File</u></strong></p>
<p><strong><u>Numbers</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>File Names</u></strong></p>
</blockquote></th>
<th><strong><u>DD</u></strong></th>
<th><blockquote>
<p><strong><u>RD</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>WR</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>DEL</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>LAYGO</u></strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><blockquote>
<p>200 NEW PERSON (Partial DD) # # # # #</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>9009032.3 APSP INTERVENTION TYPE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>9009032.4 APSP INTERVENTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>9009032.5 APSP INTERVENTION RECOMMENDATION</p>
</blockquote></td>
</tr>
</tbody>
</table>

![](pss-1-172-technical-manual-security-guide-change-pages/007.png)

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no regulations or directives related to the Pharmacy Data Management package. Additional manuals related to the Pharmacy Data Management package can be found at the VistA Documentation Library (VDL) on the Internet.
> 32 Pharmacy Data Management V. 1.0 December 2013
> Glossary
> Administration Schedule File The ADMINISTRATION SCHEDULE file (#51.1) contains
> administration schedule names and standard dosage administration times. The name is a common abbreviation for an administration schedule (e.g., QID, Q4H, PRN). The administration time is entered in military time.
> CPRS A VistA computer software package called Computerized Patient Record System. CPRS is an application in VistA that allows the user to enter all necessary orders for a patient in different packages from a single application.
> DATUP Functionality that allows the Pharmacy Enterprise Customization System (PECS) to send out custom and standard commercial-off-the-shelf (COTS) vendor database changes to update the two centralized databases at Austin and Martinsburg.
> Dispense Drug The Dispense Drug is pulled from DRUG file (#50) and usually has the strength attached to it (e.g., Acetaminophen 325 mg). Usually, the name alone without a strength attached is the Pharmacy Orderable Item name.
> Dosage Form File The DOSAGE FORM file (#50.606) contains all dosage forms and associated data that are used by Pharmacy packages and CPRS. The dosage form is used in SIG construction, default values and in the determination of the type of each dosage created for each application.
> Dose Unit File The DOSE UNIT file (#51.24) was created to accomplish the mapping to First Data Bank (FDB). All entries in this file have been mapped to an FDB Dose Unit. Although this file has not yet been standardized by Standards and Terminology Services (SRS), no local editing will be allowed. When populating the Dose Unit field for a Local Possible Dosage, selection will be from this new file.
> Drug Electrolytes File The DRUG ELECTROLYTES file (#50.4) contains the names of anions/cations, and their cations and concentration units.
> Drug File The DRUG file (#50) holds the information related to each drug that can be used to fill a prescription or medication order. It is pointed to from several other files and should be handled carefully, usually only by special individuals in the Pharmacy Service. Entries are not typically deleted, but rather made inactive by entering an inactive date.
> Drug Text File The DRUG TEXT file (#51.7) stores rapidly changing drug restrictions, guidelines, and protocols to help assure medications are being used according to defined specifications.
> Infusion Instructions File The INFUSION INSTRUCTIONS file (#53.47) holds
> abbreviations used when entering the Infusion Rate (#.08) field in the IV (#100) multiple of the PHARMACY PATIENT (#55) FILE, AND THE infusion rate (#59) FIELD IN THE non-verified orders (#53.1) file. Each record holds an expansion of the abbreviation which replaces the abbreviation in the Infusion Rate at the time the IV order is created.
> IV Additives File The IV ADDITIVES file (#52.6) contains drugs that are used as Additives in the IV room. Data entered includes drug generic name, print name, drug information, synonym(s), dispensing units, cost per unit, days for IV order, usual IV schedule, administration times, electrolytes, and quick code information.
> IV Solutions File The IV SOLUTIONS file (#52.7) contains drugs that are used as primary solutions in the IV room. The solution must already exist in the DRUG file (#50) to be selected. Data in this file includes: drug generic name, print name, status, drug information, synonym(s), volume, and electrolytes.
> Local Possible Dosages Local Possible Dosages are free text dosages that are associated with drugs that do not meet all of the criteria for Possible Dosages.
> Medication Instruction File The MEDICATION INSTRUCTION file (#51) is used by
> Unit Dose and Outpatient Pharmacy. It contains the medication instruction name, expansion and intended use.
> Medication Routes File The MEDICATION ROUTES file (#51.2) contains medication route names. The user can enter an abbreviation for each route to be used at their site. The abbreviation will most likely be the Latin abbreviation for the term.
> Medication Routes/Abbreviations The MEDICATION ROUTES file (#51.2) contains the
> medication routes and abbreviations, which are selected by each Department of Veterans Affairs Medical Centers
> 34 Pharmacy Data Management V. 1.0 December 2013
> (VAMC). The abbreviation cannot be longer than five characters to fit on labels and the Medical Administration Record (MAR). The user can add new routes and abbreviations as appropriate.
> MOCHA Medication Order Check Healthcare Application.
> National Drug File The National Drug File provides standardization of the local drug files in all VA medical facilities. Standardization includes the adoption of new drug nomenclature and drug classification and links the local drug file entries to data in the National Drug File. For drugs approved by the Food and Drug Administration (FDA), VA medical facilities have access to information concerning dosage form, strength and unit; package size and type; manufacturer's trade name; and National Drug Code (NDC). The NDF software lays the foundation for sharing prescription information among medical facilities.
> Non-Formulary Drugs Drugs that are not available for use by all providers.
> Orderable Item An Orderable Item is pulled from the PHARMACY ORDERABLE ITEM file (#50.7) and usually has no strength attached to it (e.g., Acetaminophen). The name, with a strength attached, is the Dispense Drug name (e.g., Acetaminophen 325mg).
> Orderable Item File The ORDERABLE ITEM file (#101.43) is a CPRS file that provides the Orderable Items for selection within CPRS. Pharmacy Orderable Items are a subset of this file.
> PECS Pharmacy Enterprise Customization System. A Graphical User Interface (GUI) web-based application used to research, update via DATUP, maintain, and report VA customizations of the commercial-off-the-shelf (COTS) vendor database used to perform Pharmacy order checks such as drug-drug interactions, duplicate therapy, and dosing.
> PEPS Pharmacy Enterprise Product Services. A suite of services that includes Outpatient and Inpatient services.
> Pending Order A pending order is one that has been entered by a provider through CPRS without Pharmacy finishing the order. Once Pharmacy has finished (and verified for Unit Dose only) the order, it will become active.
> Pharmacy Orderable Item The Pharmacy Orderable Item is used through CPRS to
> order Inpatient Medications and Outpatient Pharmacy prescriptions.
> Pharmacy Orderable Item File The PHARMACY ORDERABLE ITEM file (#50.7)
> contains the Order Entry name for items that can be ordered in the Inpatient Medications and Outpatient Pharmacy packages.
> Possible Dosages Dosages that have a numeric dosage and numeric Dispense Units Per Dose appropriate for administration. For a drug to have possible dosages, it must be a single ingredient product that is matched to VA PRODUCT file (#50.68). The VA PRODUCT file (#50.68) entry must have a numeric strength and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.
> Prompt A point at which the system questions the user and waits for a response.
> Standard Medication Route File The STANDARD MEDICATION ROUTE file (#51.23) was
> created to map Local Medication Routes in VistA to an FDB Route in order to perform dosage checks in PRE V.0.5. This file has been standardized by Standards and Terminology Service (STS) and is mapped to an FDB Route. It cannot be edited locally.
> Standard Schedule Standard medication administration schedules are stored in the ADMINISTRATION SCHEDULE file (#51.1).
> Units Per Dose The Units Per Dose is the number of Units (tablets, capsules, etc.) to be dispensed as a dose for an order. Fractional numbers will be accepted.
> VA Drug Class Code A drug classification system used by VA that separates drugs into different categories based upon their characteristics.
> Some cost reports can be run for VA Drug Class Codes.
> VA Product File The VA PRODUCT file (#50.68) contains a list of available drug products.

### From: PSS*1*155 Technical Manual/Security Guide Change Pages

## Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 52%" />
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
<td>04/11</td>
<td><blockquote>
<p>i-iii, 21-24r, 25, 29-30h,</p>
<p>48-49b</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*155</p>
</blockquote></td>
<td><p>Removed <em>Auto Create Dosages</em> [PSS DOSAGE CONVERSION] option from the Dosages [PSS DOSAGES MANAGEMENT] menu. Updated menus to show menu structure of Pharmacy Data Management [PSS MGR] after install of PSS*1*155, but before installing MOCHA V. 1.0 (PSS*1*117) due to phased implementation of MOCHA. Also showing menu structure with PSS*1*155 and MOCHA V. 1.0 (PSS*1*117) installed.</p>
<p>Added PSSUTIL3 routine and deleted PSSDOSCR and PSSDOSCX routines.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/11</td>
<td><blockquote>
<p>i-iv, 5, 8, removed 8a-b, 13, 24f-g, added</p>
<p>24h-l, 25,</p>
<p>28, added 28a-b for paging sense, 29, 30, renumbered</p>
<p>31a-b to be 30a- b for paging sense, 31, 32,</p>
<p>32a, 35, 45-49,</p>
<p>51, 55-59,</p>
<p>added 60</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*136 and PSS*1*117</p>
</blockquote></td>
<td><p>Added reference to latest patch info, PSS*1*117 and PSS*1*136;</p>
<p>Added new files VENDOR DISABLE/ENABLE (#59.73) and VENDOR INTERFACE DATA (#59.74) to <strong>File List</strong></p>
<p>and <strong>File Security</strong> sections.</p>
<p>Updated <strong>Options Descriptions</strong> to include the new options available after the installation of PSS*1*136 and PSS*1*117</p>
<p>Updated <strong>Routines</strong> list</p>
<p>Added new options <em>PEPS Services</em> [PSS PEPS SERVICES<em>], Check PEPS Services Setup</em> [PSS CHECK PEPS SERVICES SETUP], <em>Check Vendor Database Link</em> [PSS CHECK VENDOR DATABASE LINK], and</p>
<p><em>Schedule/Reschedule Check PEPS Interface</em> [PSS SCHEDULE PEPS INTERFACE CK], and updated</p>
<p>menus where they appear (<strong>Exported Options</strong>)</p>
<p>Added a <strong>Bulletins</strong> section to both Technical Manual and Security Guide and defined terms in <strong>Glossary</strong></p>
<p>Updated <strong>Package Requirements</strong> section</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/11</td>
<td><blockquote>
<p>i-iii, 5, 6, 8a-b,</p>
<p>33</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*153</p>
</blockquote></td>
<td><p>Renamed the MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) to be</p>
<p>DEFAULT MED ROUTE. Provided the ability to print the POSSIBLE MED ROUTES multiple on the <em>Default Med Route For OI Report</em> [PSS DEF MED ROUTE OI RPT]</p>
<p>option.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/11</td>
<td><blockquote>
<p>i, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*151</p>
</blockquote></td>
<td><p>Added PSSDSAPA routine to the Routine List. Released with CPRS version 28.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 52%" />
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
<td>02/11</td>
<td><blockquote>
<p>i, 33-34</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*142</p>
</blockquote></td>
<td><p>Added functionality to denote the default med route for IV orders in the selection list in CPRS if all of the orderable items on the order have the same default med route defined. Released with CPRS version 28.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/10</td>
<td><blockquote>
<p>i-iii, 5, <u>8</u>, 24f,</p>
<p>25, 29-30,</p>
<p>31b- 32, 32a-</p>
<p>32h, 45-50</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*147</p>
</blockquote></td>
<td>Updated patch references to include PSS*1*147. Described files, fields, options and routines added/modified as part of this patch. <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/09</td>
<td><blockquote>
<p>i-ii, 5, 8</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*141</p>
</blockquote></td>
<td><p>Updated patch references to include PSS*1*141. Added ASSOCIATED IMMUNIZATION field (#9) to the PHARMACY ORDERABLE ITEM file (#50.7).</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>08/09</td>
<td><blockquote>
<p>24f</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*140</p>
</blockquote></td>
<td><p>Added new option <em>Default Med Route OI Rpt</em> [PSS DEF MED ROUTE OI RPT].</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/09</td>
<td><blockquote>
<p>i-ii, 24b-f, 25,</p>
<p>29-31b, 48-52,</p>
<p>55-58</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*129</p>
</blockquote></td>
<td><p>Pharmacy Re-Engineering (PRE) V.0.5 Pre-Release. Restructured main PSS MGR menu and added new <em>Enhanced Order Checks Setup Menu</em>. Described files, fields, options and routines added/modified as part of this project.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>08/08</td>
<td><blockquote>
<p>iii, 25, 33-34</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*94</p>
</blockquote></td>
<td><p>Added Medication Routes and Administration Scheduling sections. Added PSSSCHED routine.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>10/06</td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*112</p>
</blockquote></td>
<td><p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routines PSS55MIS and PSS50TMP to the Routine List.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>09/06</td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*108</p>
</blockquote></td>
<td><p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routine PSS551 to the Routine List.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/06</td>
<td><blockquote>
<p>i, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*90</p>
</blockquote></td>
<td>HIPAA NCPDP Global project. Added routines PSSDAWUT and PSSNDCUT to the Routine List. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/06</td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*106</p>
</blockquote></td>
<td><p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routine PSS781 to the Routine List.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/05</td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*101</p>
</blockquote></td>
<td><p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routines PSS55 and PSS59P7 to the Routine List.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>03/05</td>
<td><blockquote>
<p>i, ii, 24a, 25, 29-31, 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*87</p>
</blockquote></td>
<td>Laser Labels Phase II project. Added <em>Warning Builder</em> and <em>Warning Mapping</em> options descriptions and updated the menu options. Added four new routines to the routine list. Cleaned up misspelled words and such on many pages. <mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 52%" />
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
<td>10/04</td>
<td><blockquote>
<p>i., 25, 33</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*85</p>
</blockquote></td>
<td>Added routines and a reference to the <em>Pharmacy Re- Engineering (PRE) Application Program Interface (API) Manual</em> created for the Pharmacy Re-Engineering (PRE) project Encapsulation cycle 1.</td>
</tr>
<tr class="even">
<td>10/04</td>
<td><blockquote>
<p>i, 24a, 25, 29-</p>
<p>31, 32d-h, 48,</p>
<p>53</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*82</p>
</blockquote></td>
<td><p>Updated the option description to include <em>Send Entire Drug File to External Interface</em> [PSS MASTER FILE ALL] option. Added new master file update information to the "HL7 Messaging with an External System" section.</p>
<p>Updated routine list to include PSSMSTR. Updated the web address for the VistA Documentation Library (VDL).</p></td>
</tr>
<tr class="odd">
<td>07/03</td>
<td><blockquote>
<p>i, 25, 31, 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*61</p>
</blockquote></td>
<td>Updated routine list to four new add PKI routines. Added new <em>Controlled Substances/PKI Reports</em> [PSS/PKI REPORTS] menu and four associated report options to the <em>Pharmacy Data Management</em> [PSS MGR] menu.</td>
</tr>
<tr class="even">
<td>04/03</td>
<td><blockquote>
<p>i, 5, 8, 29, 35,</p>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*68</p>
</blockquote></td>
<td>Updated patch references to include PSS*1*68. Added NON-VA MED field (#8) to the PHARMACY ORDERABLE ITEM file (#50.7).</td>
</tr>
<tr class="odd">
<td>03/03</td>
<td><blockquote>
<p>i., 5, 8, 24a,</p>
<p>29, 31, 35, 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*47</p>
</blockquote></td>
<td><p>Updated patch references to include PSS*1*47.</p>
<p>Added new field OTHER LANGUAGE INSTRUCTIONS (#7.1) to the PHARMACY ORDERABLE ITEM file</p>
<p>(#50.7) list and <em>Other Language Translation Setup</em> option description.</p></td>
</tr>
<tr class="even">
<td>11/02</td>
<td><blockquote>
<p>i, ii 5, (6)</p>
<p>23 - 25, (26)</p>
<p>29-30,(47), 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*55</p>
</blockquote></td>
<td>Renumbered front matter starting from this Revision History page. Updated Patch number. Updated Option descriptions to include <em>Drug Text File Report</em> option. Added routine PSSDTR in the Routines section. Added the <em>Drug Text File Report</em> option to the current PDM Menu in the Exported Options section.</td>
</tr>
<tr class="odd">
<td>10/02</td>
<td><blockquote>
<p>Title, i-iv, 32a- 32d</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*57</p>
</blockquote></td>
<td>Updated Title Page, Revision Page and Table of Contents. A section was added for the new HL7 Messaging with an External System.</td>
</tr>
<tr class="even">
<td>09/01</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*38</p>
</blockquote></td>
<td>Added this Revision History Page. Added Patch Release changes and Pharmacy Ordering Enhancements (POE) edits. Updated manual to comply with current documentation standards.</td>
</tr>
<tr class="odd">
<td>09/97</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>Original Release of Technical Manual.</td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

> NAME: PSSJI ELECTROLYTE FILE

> MENU TEXT: Electrolyte File (IV) TYPE: run routine

> DESCRIPTION:

> This option will allow you to alter the contents of the DRUG ELECTROLYTES file (50.4). This is the file that is pointed to by the ELECTROLYTES sub-file in the IV ADDITIVES (52.6) and IV SOLUTIONS (#52.7) files.

> EXIT ACTION: K I1 ROUTINE: ELECTRO^PSSVIDRG

> UPPERCASE MENU TEXT: ELECTROLYTE FILE (IV)

> NAME: PSS LOOK

> MENU TEXT: Lookup into Dispense Drug File TYPE: run routine

> DESCRIPTION: This option provides a lookup into DISPENSE DRUG file. It displays fields commonly edited.

> ROUTINE: PSSLOOK

> UPPERCASE MENU TEXT: LOOKUP INTO DISPENSE DRUG FILE

> NAME: PSSJU MI

> MENU TEXT: Medication Instruction File Add/Edit TYPE: run routine

> DESCRIPTION: The UNIT DOSE package contains a field called SPECIAL INSTRUCTIONS. This field utilizes the abbreviations and expansions of the MEDICATION INSTRUCTION file when printing on various reports. This option allow the user to enter and edit abbreviations and expansions in the MEDICATION INSTRUCTION file and to "flag" those entries for use by the INPATIENT packages only, OUTPATIENT package only, or by both.

> ROUTINE: ENMI^PSSFILED

> UPPERCASE MENU TEXT: MEDICATION INSTRUCTION FILE ADD/EDIT

> NAME: PSS MEDICATION ROUTES EDIT

> MENU TEXT: Medication Route File Enter/Edit TYPE: run routine

> DESCRIPTION: This option provides the ability to edit data in the MEDICATION ROUTES file (#51.2).

> ROUTINE: MR^PSSDFEE

> UPPERCASE MENU TEXT: MEDICATION ROUTE FILE ENTER/EDIT

> NAME: PSS EDIT ORDERABLE ITEMS

> MENU TEXT: Edit Orderable Items TYPE: run routine

> DESCRIPTION: This option is for editing Pharmacy Orderable Items. ROUTINE: PSSPOIMO

> UPPERCASE MENU TEXT: EDIT ORDERABLE ITEMS

> NAME: PSS MAINTAIN ORDERABLE ITEMS

> MENU TEXT: Dispense Drug/Orderable Item Maintenance TYPE: run routine

> DESCRIPTION: This option is for maintaining the relationship between Dispense Drugs and Orderable Items.

> ROUTINE: PSSPOIMN

> UPPERCASE MENU TEXT: DISPENSE DRUG/ORDERABLE ITEM MAINTENANCE

> NAME: PSS ORDERABLE ITEM DOSAGES

> MENU TEXT: Orderable Item/Dosages Report TYPE: run routine

> DESCRIPTION: This option prints a report that displays Inpatient and Outpatient Dosages for each Pharmacy Orderable Item. These are the dosages that will display for selection through Computerized Patient Record System (CPRS) when an Orderable Item is selected for a medication order.

> ROUTINE: EN^PSSOIDOS

> UPPERCASE MENU TEXT: ORDERABLE ITEM/DOSAGES REPORT

> NAME: PSS INSTRUCTIONS/ITEMS REPORT

> MENU TEXT: Patient Instructions Report TYPE: run routine

> DESCRIPTION: This option prints a report that displays Pharmacy Orderable Items, along with the expanded Patient Instructions for each Orderable Item. These Patient Instructions are used as default values for Outpatient orders entered through Computerized Patient Record System (CPRS) and Outpatient Pharmacy.

> ROUTINE: EN^PSSPNSRP

> UPPERCASE MENU TEXT: PATIENT INSTRUCTIONS REPORT

> September 1997 Pharmacy Data Management V. 1.0 21

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p><strong>NAME: PSS ORDERABLE ITEM REPORT</strong></p>
<p>MENU TEXT: Orderable Item Report TYPE: run routine</p>
<p>DESCRIPTION: This option lists items from your Pharmacy Orderable Item file, along with the associated Dispense Drugs.</p>
<p>ROUTINE: PSSPOIKA</p>
<p>UPPERCASE MENU TEXT: ORDERABLE ITEM REPORT</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSSNFI</strong></p>
<p>MENU TEXT: Formulary Information Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a listing of pertinent pharmacy formulary information.</p>
<p>ROUTINE: PSSNFI</p>
<p>UPPERCASE MENU TEXT: FORMULARY INFORMATION REPORT</p></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>NAME: PSS EDIT TEXT</strong></p>
<p>MENU TEXT: Drug Text Enter/Edit TYPE: run routine</p>
<p>DESCRIPTION: This option enables you to edit entries in the DRUG TEXT file. This file contains drug information, restrictions, and guidelines, etc.</p>
<p>ROUTINE: PSSTXT</p>
<p>UPPERCASE MENU TEXT: DRUG TEXT ENTER/EDIT</p></td>
</tr>
<tr class="odd">
<td><p><strong>NAME: PSS SYS EDIT</strong></p>
<p>MENU TEXT: Pharmacy System Parameters Edit TYPE: run routine</p>
<p>DESCRIPTION: This option allows the user to edit the Pharmacy parameters used in Pharmacy Data Management.</p>
<p>ROUTINE: PSSYSP</p>
<p>UPPERCASE MENU TEXT: PHARMACY SYSTEM PARAMETERS EDIT</p></td>
<td>System</td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>NAME: PSS SCHEDULE EDIT</strong></p>
<p>MENU TEXT: Standard Schedule Edit TYPE: run routine</p>
<p>DESCRIPTION: Allows user to edit the set of times associated with the standard dosage administration schedules (Q3H,Q8H,TID, etc.). This may be used to define the outpatient expansion to be used when the schedule is entered for an outpatient medication order.</p>
<p>ROUTINE: ENPSJSE^PSSJEEU</p>
<p>UPPERCASE MENU TEXT: STANDARD SCHEDULE EDIT</p></td>
</tr>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS SYNONYM EDIT</strong></p>
<p>MENU TEXT: Synonym Enter/Edit TYPE: run routine</p>
<p>DESCRIPTION: The option provides easy access to update the synonym information for an entry in the local DRUG file.</p>
<p>ROUTINE: PSSSEE</p>
<p>UPPERCASE MENU TEXT: SYNONYM ENTER/EDIT</p></td>
</tr>
</tbody>
</table>

## The option description below was retrieved from VA FileMan and reflects the new option added to PDM following the installation of patch PSS\*1\*55.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The option description below was retrieved from VA FileMan and reflects the new option added to PDM following the installation of patch PSS\*1\*47. *Other Language Translation Setup* \[PSS OTHER LANGUAGE SETUP\] option is a stand-alone option that must be assigned to the person(s) responsible for maintaining it.

## The option description below was retrieved from VA FileMan and reflects the new option added to PDM following the installation of PSS\*1\*82.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The two option descriptions below were retrieved from VA FileMan and reflect the new options added to PDM following the installation of PSS\*1\*87.

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS WARNING BUILDER</strong></p>
<p>MENU TEXT: Warning Builder TYPE: run routine</p>
<p>DESCRIPTION: This option will allow you to define a custom warning label list containing entries from both the new warning label source and the old Rx Consult file entries.</p>
<p>ROUTINE: PSSWRNB</p>
<p>UPPERCASE MENU TEXT: WARNING BUILDER</p></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>NAME: PSS WARNING MAPPING</strong></p>
<p>MENU TEXT: Warning Mapping TYPE: run routine</p>
<p>DESCRIPTION: This option is used to match an entry from the old Rx Consult file to the new commercial data source warning file to aid in using the Warning Builder (to identify local warnings that do not have an equivalent entry in the new commercial data source).</p>
<p>The user can also enter a Spanish translation for an Rx Consult file entry, if desired, but whenever possible, the new commercial data source's warnings (English or Spanish depending on the patient setting) should be used.</p>
<p>ROUTINE: EDIT^PSSWMAP</p>
<p>UPPERCASE MENU TEXT: WARNING MAPPING</p></td>
</tr>
</tbody>
</table>

## The following options were retrieved from VA FileMan and reflect the new options added to PDM following the installation of PSS\*1\*129.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: PSS LOCAL POSSIBLE DOSAGES

> MENU TEXT: Local Possible Dosages Report TYPE: run routine

> DESCRIPTION: This option provides a report that displays entries from the LOCAL POSSIBLE DOSAGE (#50.0904) Subfile of the DRUG (#50) File with missing data in DOSE UNIT (#4) Field and the NUMERIC DOSE (#5) Field. This data needs to be populated if Dosage checks are to be performed, when that Local Possible Dosage is selected for an order.

> ROUTINE: EN^PSSLDOSE

> UPPERCASE MENU TEXT: LOCAL POSSIBLE DOSAGES REPORT

> NAME: PSS DOSE UNIT REQUEST

> MENU TEXT: Request Change to Dose Unit TYPE: run routine

> DESCRIPTION: This option enables a request to be made to have a new entry added, or a current entry changed in the DOSE UNITS (#51.24) File.

> ROUTINE: DOSE^PSSMEDRQ

> UPPERCASE MENU TEXT: REQUEST CHANGE TO DOSE UNIT

> NAME: PSS MED INSTRUCTION MANAGEMENT

> MENU TEXT: Medication Instruction Management TYPE: menu

> DESCRIPTION: The Sub-Menu contains options related to the MEDICATION INSTRUCTION (#51) File.

> ITEM: PSSJU

> ITEM: PSS MED INSTRUCTION REPORT

> NAME: PSS MED INSTRUCTION REPORT

> MENU TEXT: Medication Instruction File Report TYPE: run routine

> DESCRIPTION: This option provides a report of entries from the MEDICATION INSTRUCTION (#51) File that shows whether or not data has been entered in the FREQUENCY (IN MINUTES) (#31) Field. To perform Dosage checks on medication orders, a frequency must be derived from the Schedule of the order.

> ROUTINE: EN^PSSMIRPT

> UPPERCASE MENU TEXT: MEDICATION INSTRUCTION FILE RE

> NAME: PSS MEDICATION ROUTES MGMT

> MENU TEXT: Medication Routes Management TYPE: menu

> DESCRIPTION: This Sub-Menu contains options related to Medication Routes in both the MEDICATION ROUTES (#51.2) File and the STANDARD MEDICATION ROUTES (#51.23) File.

> ITEM: PSS MEDICATION ROUTES EDIT ITEM: PSS MED ROUTE MAPPING REPORT ITEM: PSS MED ROUTE MAPPING CHANGES ITEM: PSS MEDICATION ROUTE REQUEST

> These four options are duplicated on the ENHANCED ORDER CHECKS SETUP menu

> NAME: PSS MEDICATION ROUTES EDIT

> MENU TEXT: Medication Route File Enter/Edit TYPE: run routine

> DESCRIPTION: This option provides the ability to edit data for entries in the MEDICATION ROUTES (#51.2) File.

> ROUTINE: MR^PSSDFEE

> UPPERCASE MENU TEXT: MEDICATION ROUTE FILE ENTER/ED

> NAME: PSS MED ROUTE MAPPING REPORT

> MENU TEXT: Medication Route Mapping Report TYPE: run routine

> DESCRIPTION: This option provides a report that shows the status of the current mapping from the Medication Routes (#51.2) File to the Standard Medication Routes (#51.23) File.

> ROUTINE: REP^PSSMEDRT

> UPPERCASE MENU TEXT: MEDICATION ROUTE MAPPING REPOR

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 27%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p><strong>NAME: PSS MED ROUTE MAPPING CHANGES</strong></p>
<p>MENU TEXT: Medication Route Mapping History Report TYPE: run routine</p>
<p>DESCRIPTION: This option will provide a report that shows all of the mapping changes between entries from the MEDICATION ROUTES (#51.2) File to entries in the STANDARD MEDICATION ROUTES (#51.23) File.</p>
<p>ROUTINE: DRIVER^PSSMEDCH</p>
<p>UPPERCASE MENU TEXT: MEDICATION ROUTE MAPPING HISTO</p>
<p><strong>NAME: PSS MEDICATION ROUTE REQUEST</strong></p>
<p>MENU TEXT: Request Change to Standard Medication Route TYPE: run routine</p>
<p>DESCRIPTION: This option enables a request to be made to have a new entry added, or a current entry changed in the STANDARD MEDICATION ROUTES (#51.23) File.</p>
<p>ROUTINE: REQ^PSSMEDRQ</p>
<p>UPPERCASE MENU TEXT: REQUEST CHANGE TO STANDARD MED</p>
<p><strong>NAME: PSS DRUG TEXT MANAGEMENT</strong></p>
<p>MENU TEXT: Drug Text Management TYPE: menu</p>
<p>DESCRIPTION: This Sub-Menu contains options concerning Drug Text. ITEM: PSS EDIT TEXT DISPLAY ORDER: 1</p>
<p>ITEM: PSS DRUG TEXT FILE REPORT DISPLAY ORDER: 2</p>
<p><strong>NAME: PSS SCHEDULE MANAGEMENT</strong></p>
<p>MENU TEXT: Standard Schedule Management TYPE: menu</p>
<p>DESCRIPTION: This Sub-Menu contains options needed for Schedule maintenance. ITEM: PSS SCHEDULE EDIT</p>
<p>ITEM: PSS SCHEDULE REPORT</p>
<p><strong>NAME: PSS SCHEDULE REPORT</strong></p>
<p>MENU TEXT: Administration Schedule File Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report of entries from the ADMINISTRATION SCHEDULE (#51.1) File that shows whether or not data has been entered in the FREQUENCY (IN MINUTES) (#2) Field for the entries. To perform Dosage checks on medication orders, a frequency must be derived from the Schedule of the order.</p>
<p>ROUTINE: EN^PSSSCHRP</p>
<p>UPPERCASE MENU TEXT: ADMINISTRATION SCHEDULE FILE R</p>
<p><strong>NAME: PSS ENHANCED ORDER CHECKS</strong></p>
<p>MENU TEXT: Enhanced Order Checks Setup Menu TYPE: menu</p>
<p>DESCRIPTION: This menu option contains the options needed for Pharmacy to do the appropriate setup needed to install Pharmacy Re-engineering version 0.5.</p>
<p>Version 0.5 mainly deals with the Enhanced Order Checks. ITEM: PSS MED ROUTES INITIAL MAPPING</p>
<p>ITEM: PSS MAP ONE MED ROUTE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ITEM: PSS MED ROUTE MAPPING REPORT ITEM: PSS MEDICATION ROUTES EDIT ITEM: PSS MED ROUTE MAPPING CHANGES</p>
<p>ITEM: PSS MEDICATION ROUTE REQUEST</p>
</blockquote></td>
<td><blockquote>
<p>These four options are duplicated on the MEDICATION ROUTES MANAGEMENT menu</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>ITEM: PSS LOCAL DOSAGES EDIT ALL ITEM: PSS LOCAL DOSAGES EDIT</p>
<p>ITEM: PSS LOCAL POSSIBLE DOSAGES &lt;&lt; This option is duplicated on the DOSAGES menu</p>
<p>ITEM: PSS STRENGTH MISMATCH ITEM: PSS EDIT DOSAGES</p>
<p>ITEM: PSS DOSE UNIT REQUEST &lt;&lt; This option is duplicated on the DOSAGES menu</p>
<p>ITEM: PSS MARK PREMIX SOLUTIONS ITEM: PSS IV SOLUTION REPORT ITEM: PSS SCHEDULE REPORT</p>
<p>ITEM: PSS MED INSTRUCTION REPORT</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS MED ROUTES INITIAL MAPPING</strong></p>
<p>MENU TEXT: Find Unmapped Local Medication Routes PACKAGE: PHARMACY DATA MANAGEMENT</p>
<p>DESCRIPTION: This option will loop through all entries in the MEDICATION ROUTES (#51.2) File and find entries that are marked for 'ALL PACKAGES' in the PACKAGE USE (#3) Field that are not mapped to an entry in the STANDARD MEDICATION ROUTES (#51.23) File, and prompt for the mapping.</p>
<p>ROUTINE: MATCH^PSSMEDRT</p>
<p>UPPERCASE MENU TEXT: FIND UNMAPPED LOCAL MEDICATION</p></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>NAME: PSS MAP ONE MED ROUTE</strong></p>
<p>MENU TEXT: Map Local Medication Route to Standard TYPE: run routine</p>
<p>DESCRIPTION: This options provides the ability to select an entry from the MEDICATION ROUTES (#51.2) File and map it to an entry in the STANDARD MEDICATION ROUTES (#51.23) File.</p>
<p>ROUTINE: ONE^PSSMEDRT</p>
<p>UPPERCASE MENU TEXT: MAP LOCAL MEDICATION ROUTE TO</p></td>
</tr>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS MED ROUTE MAPPING REPORT</strong></p>
<p>MENU TEXT: Medication Route Mapping Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report that shows the status of the current mapping from the Medication Routes (#51.2) File to the Standard Medication Routes (#51.23) File.</p>
<p>ROUTINE: REP^PSSMEDRT</p>
<p>UPPERCASE MENU TEXT: MEDICATION ROUTE MAPPING REPOR</p></td>
</tr>
<tr class="even">
<td><p><strong>NAME: PSS MED ROUTE MAPPING CHANGES</strong></p>
<p>MENU TEXT: Medication Route Mapping History Report TYPE: run routine</p>
<p>DESCRIPTION: This option will provide a report that shows all changes between entries from the MEDICATION ROUTES (#51.2) File the STANDARD MEDICATION ROUTES (#51.23) File.</p>
<p>ROUTINE: DRIVER^PSSMEDCH</p>
<p>UPPERCASE MENU TEXT: MEDICATION ROUTE MAPPING HISTO</p></td>
<td>of the mapping to entries in</td>
</tr>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS MEDICATION ROUTE REQUEST</strong></p>
<p>MENU TEXT: Request Change to Standard Medication Route TYPE: run routine</p>
<p>DESCRIPTION: This option enables a request to be made to have a new entry added, or a current entry changed in the STANDARD MEDICATION ROUTES (#51.23) File.</p>
<p>ROUTINE: REQ^PSSMEDRQ</p>
<p>UPPERCASE MENU TEXT: REQUEST CHANGE TO STANDARD MED</p></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>NAME: PSS LOCAL DOSAGES EDIT ALL</strong></p>
<p>MENU TEXT: Find Unmapped Local Possible Dosages TYPE: run routine</p>
<p>DESCRIPTION: This option loops through and finds entries in the LOCAL POSSIBLE DOSAGE (#50.0904) Subfile of the DRUG (#50) File without data populated in the DOSE UNIT (#4) Field and the NUMERIC DOSE (#5) Field, and will prompt for data entry into these fields. This data needs to be populated if Dosage checks are to be performed, when that Local Possible Dosage is selected for an order.</p>
<p>ROUTINE: EN^PSSLDALL</p>
<p>UPPERCASE MENU TEXT: FIND UNMAPPED LOCAL POSSIBLE D</p></td>
</tr>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS LOCAL DOSAGES EDIT</strong></p>
<p>MENU TEXT: Map Local Possible Dosages TYPE: run routine</p>
<p>DESCRIPTION: This option allows edits to the DOSE UNIT (#4) Field and the NUMERIC DOSE (#5) Field that are associated with entries from the LOCAL POSSIBLE DOSAGE (#50.0904) Subfile of the DRUG (#50) File. This data needs to be populated if Dosage checks are to be performed, when that Local Possible Dosage is selected for an order.</p>
<p>ROUTINE: EDT^PSSLDEDT</p>
<p>UPPERCASE MENU TEXT: MAP LOCAL POSSIBLE DOSAGES</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS LOCAL POSSIBLE DOSAGES</strong></p>
<p>MENU TEXT: Local Possible Dosages Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report that displays entries from the LOCAL POSSIBLE DOSAGE (#50.0904) Subfile of the DRUG (#50) File with missing data in DOSE UNIT (#4) Field and the NUMERIC DOSE (#5) Field. This data needs to be populated if Dosage checks are to be performed, when that Local Possible Dosage is selected for an order.</p>
<p>ROUTINE: EN^PSSLDOSE</p>
<p>UPPERCASE MENU TEXT: LOCAL POSSIBLE DOSAGES REPORT</p></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>NAME: PSS STRENGTH MISMATCH</strong></p>
<p>MENU TEXT: Strength Mismatch Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report that shows all entries from the DRUG (#50) File that have data in the STRENGTH (#901) Field that does not match the data in the STRENGTH (#2) Field from the match in the VA PRODUCT (#50.68) File.</p>
<p>ROUTINE: EN^PSSTRENG</p>
<p>UPPERCASE MENU TEXT: STRENGTH MISMATCH REPORT</p></td>
</tr>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS DOSE UNIT REQUEST</strong></p>
<p>MENU TEXT: Request Change to Dose Unit TYPE: run routine</p>
<p>DESCRIPTION: This option enables a request to be made to have a new entry added, or a current entry changed in the DOSE UNITS (#51.24) File.</p>
<p>ROUTINE: DOSE^PSSMEDRQ</p>
<p>UPPERCASE MENU TEXT: REQUEST CHANGE TO DOSE UNIT</p></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>NAME: PSS MARK PREMIX SOLUTIONS</strong></p>
<p>MENU TEXT: Mark PreMix Solutions TYPE: run routine</p>
<p>DESCRIPTION: This option will be used to mark entries from the IV SOLUTIONS (#52.7) File as PreMixes, by allowing editing of the PREMIX (#18) Field.</p>
<p>ROUTINE: EDIT^PSSPRUTL</p>
<p>UPPERCASE MENU TEXT: MARK PREMIX SOLUTIONS</p></td>
</tr>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS IV SOLUTION REPORT</strong></p>
<p>MENU TEXT: IV Solution Report TYPE: run routine</p>
<p>DESCRIPTION: This report will display all entries from the IV SOLUTIONS (#52.7) File, or just those entries marked as PreMixes in the PREMIX (#18) Field.</p>
<p>ROUTINE: REP^PSSPRMIX</p>
<p>UPPERCASE MENU TEXT: IV SOLUTION REPORT</p></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>NAME: PSS SCHEDULE REPORT</strong></p>
<p>MENU TEXT: Administration Schedule File Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report of entries from the ADMINISTRATION SCHEDULE (#51.1) File that shows whether or not data has been entered in the FREQUENCY (IN MINUTES) (#2) Field for the entries. To perform Dosage checks on medication orders, a frequency must be derived from the Schedule of the order.</p>
<p>ROUTINE: EN^PSSSCHRP</p>
<p>UPPERCASE MENU TEXT: ADMINISTRATION SCHEDULE FILE R</p></td>
</tr>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS MED INSTRUCTION REPORT</strong></p>
<p>MENU TEXT: Medication Instruction File Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report of entries from the MEDICATION INSTRUCTION (#51) File that shows whether or not data has been entered in the FREQUENCY (IN MINUTES) (#31) Field. To perform Dosage checks on medication orders, a frequency must be derived from the Schedule of the order.</p>
<p>ROUTINE: EN^PSSMIRPT</p>
<p>UPPERCASE MENU TEXT: MEDICATION INSTRUCTION FILE RE</p></td>
</tr>
</tbody>
</table>

## The following option was retrieved from VA FileMan and reflects the new option added to PDM following the installation of PSS\*1\*140.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 12%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 10%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p><strong>NAME: PSS MEDICATION ROUTES MGMT</strong></p>
<p>MENU TEXT: Medication Routes Management TYPE: menu</p>
<p>DESCRIPTION: This Sub-Menu contains options related to Medication Routes in both the MEDICATION ROUTES (#51.2) File and the STANDARD MEDICATION ROUTES (#51.23) File.</p>
<p>ITEM: PSS MEDICATION ROUTES EDIT ITEM: PSS MED ROUTE MAPPING REPORT ITEM: PSS MED ROUTE MAPPING CHANGES</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ITEM: PSS MEDICATION ROUTE REQUEST</p>
</blockquote></td>
<td colspan="4" rowspan="2"><blockquote>
<p>This option introduced with PSS*1*140.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ITEM: PSS DEF MED ROUTE OI RPT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS DEF MED ROUTE OI RPT</strong></p>
<p>MENU TEXT: Default Med Route For OI Report TYPE: print</p>
<p>DIC {DIP}: PS(50.7, L.: 0</p>
<p>FLDS: [PSS DEF MED ROUTE FOR OI] BY: [PSS DEF MED DHD: [PSS HDR DEF MED ROUTE]</p>
<p>UPPERCASE MENU TEXT: DEFAULT MED ROUTE FOR OI REPOR</p>
</blockquote></td>
<td>ROUTE</td>
<td>FOR</td>
<td>OI]</td>
<td></td>
</tr>
</tbody>
</table>

> The following options were retrieved from VA FileMan and reflect the new options added to PDM following the installation of patch PSS\*1\*147.

> NAME: PSS ADDITIVE/SOLUTION

> MENU TEXT: IV Additive/Solution TYPE: menu

> PACKAGE: PHARMACY DATA MANAGEMENT

> DESCRIPTION: This Sub-Menu contains options that can be used to run reports

> from the IV ADDITIVES (#52.6) File and the IV SOLUTIONS (#52.7) File. It also provides an option to edit the PREMIX (#18) Field in the IV SOLUTIONS (#52.7) File.

> ITEM: PSS IV ADDITIVE REPORT DISPLAY ORDER: 1

> ITEM: PSS IV SOLUTION REPORT DISPLAY ORDER: 2 ITEM: PSS MARK PREMIX SOLUTIONS DISPLAY ORDER: 3

> UPPERCASE MENU TEXT: IV ADDITIVE/SOLUTION

> NAME: PSS IV ADDITIVE REPORT

> MENU TEXT: IV Additive Report TYPE: run routine

> DESCRIPTION: This report will display entries from the IV ADDITIVES (#52.6) File. The display selection choices will be for all IV Additives, only IV Additives whose ADDITIVE FREQUENCY (#18) Field is set to '1 BAG/DAY', or only those IV Additives whose ADDITIVE FREQUENCY (#18) Field is null.

> ROUTINE: REP^PSSADRPT

> UPPERCASE MENU TEXT: IV ADDITIVE REPORT

> NAME: PSS IV SOLUTION REPORT

> MENU TEXT: IV Solution Report TYPE: run routine

> PACKAGE: PHARMACY DATA MANAGEMENT

> DESCRIPTION: This report will display all entries from the IV SOLUTIONS (#52.7) File, or just those entries marked as PreMixes in the PREMIX (#18) Field.

> ROUTINE: REP^PSSPRMIX

> UPPERCASE MENU TEXT: IV SOLUTION REPORT

## The following options were retrieved from VA FileMan and reflect the new options added to PDM following the installation of patch PSS\*1\*136 and PSS\*1\*117.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>NAME: PSS PEPS SERVICES</strong> MENU TEXT: PEPS Services</p>
<blockquote>
<p>TYPE: menu</p>
<p>PACKAGE: PHARMACY DATA MANAGEMENT</p>
</blockquote>
<p>ITEM: PSS CHECK VENDOR DATABASE LINK DISPLAY ORDER: 1 ITEM: PSS CHECK PEPS SERVICES SETUP DISPLAY ORDER: 2 ITEM: PSS SCHEDULE PEPS INTERFACE CK DISPLAY ORDER: 3</p>
<blockquote>
<p>UPPERCASE MENU TEXT: PEPS SERVICES</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS CHECK PEPS SERVICES SETUP</strong> MENU TEXT: Check PEPS Services Setup</p>
<blockquote>
<p><strong>TYPE: run routine</strong></p>
<p>PACKAGE: PHARMACY DATA MANAGEMENT</p>
<p>DESCRIPTION: This option provides the ability to check and validate that the link to the vendor interface used for enhanced order checking is enabled and operational. It also provides the ability to execute various order checks against the vendor database to ensure that the database is installed and reachable.</p>
<p>ROUTINE: RUNTEST^PSSHRIT</p>
<p>UPPERCASE MENU TEXT: CHECK PEPS SERVICES SETUP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p><strong>NAME: PSS CHECK VENDOR DATABASE LINK</strong> MENU TEXT: Check Vendor</p>
<blockquote>
<p>TYPE: run routine</p>
<p>PACKAGE: PHARMACY DATA MANAGEMENT ROUTINE: INTACT^PSSHRIT UPPERCASE MENU TEXT: CHECK VENDOR DATABASE LINK</p>
</blockquote></td>
<td>Database Link</td>
</tr>
<tr class="odd">
<td colspan="2"><p><strong>NAME: PSS SCHEDULE PEPS INTERFACE CK</strong></p>
<blockquote>
<p>MENU TEXT: Schedule/Reschedule Check PEPS Interface</p>
<p>TYPE: run routine PACKAGE: PHARMACY DATA MANAGEMENT</p>
<p>DESCRIPTION: This option allows you to schedule the Interface Scheduler [PSS INTERFACE SCHEDULER] option, which tests the PEPS interface by sending a PING request. If the PEPS Interface is not available, a mail message will be sent to the G.PSS ORDER CHECKS mail group.</p>
<p>ROUTINE: SCHDOPT^PSSHRIT TIMESTAMP: 61493,49257 UPPERCASE MENU TEXT: SCHEDULE/RESCHEDULE CHECK PEPS</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>NAME: PSS ENABLE/DISABLE DB LINK</strong></p>
<blockquote>
<p>MENU TEXT: Enable/Disable Vendor Database Link TYPE: run routine</p>
<p>PACKAGE: PHARMACY DATA MANAGEMENT</p>
<p>DESCRIPTION: This option provides the ability to disable/enable the link to the vendor interface used for enhanced order checking. When disabled, NO drug-drug interaction, duplicate therapy or dosing order checks will</p>
<p>be performed in Pharmacy and in Computerized Patient Record System (CPRS). ROUTINE: EN^PSSDSFDB</p>
<p>UPPERCASE MENU TEXT: ENABLE/DISABLE VENDOR DATABASE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> After installing PSS\*1\*117, your current PSS MGR menu will look as shown below. See section

## for information regarding stand-alone options that are not part of the current PSS MGR menu.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pharmacy Data Management \[PSS MGR\]

> CMOP Mark/Unmark (Single drug) \[PSSXX MARK\] ![](pss-1-155-technical-manual-security-guide-change-pages/002.png)

> Dosages…

> \[PSS DOSAGES MANAGEMENT\]

> Auto Create Dosages

> \[PSS DOSAGE CONVERSION\]

> Dosage Form File Enter/Edit \[PSS DOSAGE FORM EDIT\]

> Enter/Edit Dosages \[PSS EDIT DOSAGES\]

> Most Common Dosages Report \[PSS COMMON DOSAGES\]

> Noun/Dosage Form Report

> \[PSS DOSE FORM/ NOUN REPORT\]

> Review Dosages Report

> \[PSS DOSAGE REVIEW REPORT\]

> Local Possible Dosages Report

> \[PSS LOCAL POSSIBLE DOSAGES\]

> Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

> Drug Enter/Edit

> \[PSS DRUG ENTER/ EDIT\]

> Order Check Management

> \[PSS ORDER CHECK MANAGEMENT\]

> Request Changes to Enhanced Order Check Database \[PSS ORDER CHECK CHANGES\]

> Report of Locally Entered Interactions \[PSS REPORT LOCAL INTERACTIONS\]

> Electrolyte File (IV)

> \[PSSJI ELECTROLYTE FILE\]

> Lookup into Dispense Drug File \[PSS LOOK\]

> Medication Instruction Management ...

> \[PSS MED INSTRUCTION MANAGEMENT\]

> Medication Instruction File Add/Edit *\<\<Moved from main PSS MGR menu*

> \[PSSJU MI\]

> Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

> Medication Routes Management ...

> \[PSS MEDICATION ROUTES MGMT\]

> Medication Route File Enter/Edit *\<\<Moved from main PSS MGR menu*

> \[PSS MEDICATION ROUTES EDIT\]

> Medication Route Mapping Report

> \[PSS MED ROUTE MAPPING REPORT\]

> Medication Route Mapping History Report \[PSS MED ROUTE MAPPING CHANGES\]

> Request Change to Standard Medication Route \[PSS MEDICATION ROUTE REQUEST\]

> Default Med Route for OI Report \[PSS DEF MED ROUTE OI RPT\]

> Orderable Item Management

\[PSS ORDERABLE ITEM MANAGEMENT\]

> Edit Orderable Items

> \[PSS EDIT ORDERABLE ITEMS\]

> Dispense Drug/Orderable Item Maintenance \[PSS MAINTAIN ORDERABLE ITEMS\]

> Orderable Item/Dosages Report

> \[PSS ORDERABLE ITEM DOSAGES

> Patient Instructions Report

> \[PSS INSTRUCTIONS/ ITEMS REPORT\]

> Orderable Item Report *\<\<Moved from main PSS MGR menu*

> \[PSS ORDERABLE ITEM REPORT\]

> Formulary Information Report \[PSSNFI\]

> Drug Text Management ...

> \[PSS DRUG TEXT MANAGEMENT\]

> Drug Text Enter/Edit *\<\<Moved from main PSS MGR menu*

> \[PSS EDIT TEXT\]

> Drug Text File Report *\<\<Moved from main PSS MGR menu*

> \[PSS DRUG TEXT FILE REPORT

> Pharmacy System Parameters Edit \[PSS SYS EDIT\]

> Standard Schedule Management ... \[PSS SCHEDULE MANAGEMENT\]

> Standard Schedule Edit *\<\<Moved from main PSS MGR menu*

> \[PSS SCHEDULE EDIT\]

> Administration Schedule File Report

> *\[PSS SCHEDULE REPORT\]*

> Synonym Enter/Edit \[PSS SYNONYM EDIT\]

> Controlled Substances/PKI Reports \[PSS CS/PKI REPORTS\]

> DEA Spec Hdlg & CS Fed Sch Discrepancy \[PSS DEA VS CS FED. SCH. DISCR.\]

> Controlled Substances Not Matched to NDF \[PSS CS NOT MATCHED TO NDF\]

> CS (DRUGS) Inconsistent with DEA Spec Hdlg \[PSS CS DRUGS INCON WITH DEA\]

> CS (Ord. Item) Inconsistent with DEA Spec Hdlg \[PSS CS (OI) INCON WITH DEA\]

> Send Entire Drug File to External Interface \[PSS MASTER FILE ALL\]

IV Additive/Solution …

> \[PSS ADDITIVE/SOLUTION\]

IV Additive Report

> \[PSS IV ADDITIVE REPORT\]

> IV Solution Report

> \[PSS IV SOLUTION REPORT\]

> Mark PreMix Solutions

> \[PSS MARK PREMIX SOLUTIONS\]

> Warning Builder

> \[PSS WARNING BUILDER\]

> Warning Mapping

> \[PSS WARNING MAPPING\]

> PEPS Services

> \[PSS PEPS SERVICES\]

> Check Vendor Database Link

> \[PSS CHECK VENDOR DATABASE LINK\]

> Check PEPS Services Setup

> \[PSS CHECK PEPS SERVICES SETUP\]

> Schedule/Reschedule Check PEPS Interface \[PSS SCHEDULE PEPS INTERFACE CK\]

> After installing PSS\*1\*155, but before installing MOCHA V. 1.0 (PSS\*1\*117), your current PSS MGR menu will look as shown below. The option Auto Create Dosages \[PSS DOSAGE CONVERSION\] has been removed from the Dosages ... \[PSS DOSAGES MANAGEMENT\] menu.

> Pharmacy Data Management \[PSS MGR\]

> CMOP Mark/Unmark (Single drug) \[PSSXX MARK\] ![](pss-1-155-technical-manual-security-guide-change-pages/003.png)

> Dosages…

> \[PSS DOSAGES MANAGEMENT\]

> Dosage Form File Enter/Edit \[PSS DOSAGE FORM EDIT\]

> Enter/Edit Dosages \[PSS EDIT DOSAGES\]

> Most Common Dosages Report \[PSS COMMON DOSAGES\]

> Noun/Dosage Form Report

> \[PSS DOSE FORM/ NOUN REPORT\]

> Review Dosages Report

> \[PSS DOSAGE REVIEW REPORT\]

> Local Possible Dosages Report

> \[PSS LOCAL POSSIBLE DOSAGES\]

> Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

> Drug Enter/Edit

> \[PSS DRUG ENTER/ EDIT\]

> Drug Interaction Management

> \[PSS DRG INTER MANAGEMENT\]

> Enter/Edit Local Drug Interaction \[PSS INTERACTION LOCAL ADD\]

> Report of Locally Entered Interactions \[PSS REPORT LOCAL INTERACTIONS\]

> Electrolyte File (IV)

> \[PSSJI ELECTROLYTE FILE\]

> Lookup into Dispense Drug File \[PSS LOOK\]

> Medication Instruction Management ...

> \[PSS MED INSTRUCTION MANAGEMENT\]

> Medication Instruction File Add/Edit \[PSSJU MI\]

> Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

> Medication Routes Management ...

> \[PSS MEDICATION ROUTES MGMT\]

> Medication Route File Enter/Edit \[PSS MEDICATION ROUTES EDIT\]

> Medication Route Mapping Report

> \[PSS MED ROUTE MAPPING REPORT\]

> Medication Route Mapping History Report \[PSS MED ROUTE MAPPING CHANGES\]

> Request Change to Standard Medication Route \[PSS MEDICATION ROUTE REQUEST\]

> Default Med Route for OI Report \[PSS DEF MED ROUTE OI RPT\]

> Orderable Item Management

\[PSS ORDERABLE ITEM MANAGEMENT\]

> Edit Orderable Items

> \[PSS EDIT ORDERABLE ITEMS\]

> Dispense Drug/Orderable Item Maintenance \[PSS MAINTAIN ORDERABLE ITEMS\]

> Orderable Item/Dosages Report

> \[PSS ORDERABLE ITEM DOSAGES

> Patient Instructions Report

> \[PSS INSTRUCTIONS/ ITEMS REPORT\]

> Orderable Item Report

> \[PSS ORDERABLE ITEM REPORT\]

> Formulary Information Report \[PSSNFI\]

> Drug Text Management ...

> \[PSS DRUG TEXT MANAGEMENT\]

> Drug Text Enter/Edit \[PSS EDIT TEXT\]

> Drug Text File Report

> \[PSS DRUG TEXT FILE REPORT

> Pharmacy System Parameters Edit \[PSS SYS EDIT\]

> Standard Schedule Management ... \[PSS SCHEDULE MANAGEMENT\]

> Standard Schedule Edit \[PSS SCHEDULE EDIT\]

> Administration Schedule File Report \[PSS SCHEDULE REPORT\]

> Synonym Enter/Edit \[PSS SYNONYM EDIT\]

> Controlled Substances/PKI Reports \[PSS CS/PKI REPORTS\]

> DEA Spec Hdlg & CS Fed Sch Discrepancy \[PSS DEA VS CS FED. SCH. DISCR.\]

> Controlled Substances Not Matched to NDF \[PSS CS NOT MATCHED TO NDF\]

> CS (DRUGS) Inconsistent with DEA Spec Hdlg \[PSS CS DRUGS INCON WITH DEA\]

> CS (Ord. Item) Inconsistent with DEA Spec Hdlg \[PSS CS (OI) INCON WITH DEA\]

> Send Entire Drug File to External Interface \[PSS MASTER FILE ALL\]

> Enhanced Order Checks Setup Menu \[PSS ENHANCED ORDER CHECKS\]

> Find Unmapped Local Medication Routes \[PSS MED ROUTES INITIAL MAPPING\]

> Map Local Medication Route to Standard \[PSS MAP ONE MED ROUTE\]

> Medication Route Mapping Report

> \[PSS MED ROUTE MAPPING REPORT\]

> Medication Route File Enter/Edit \[PSS MEDICATION ROUTES EDIT\]

> Medication Route Mapping History Report \[PSS MED ROUTE MAPPING CHANGES\]

> Request Change to Standard Medication Route \[PSS MEDICATION ROUTE REQUEST\]

> Find Unmapped Local Possible Dosages \[PSS LOCAL DOSAGES EDIT ALL\]

> Map Local Possible Dosages \[PSS LOCAL DOSAGES EDIT\]

> Local Possible Dosages Report

> \[PSS LOCAL POSSIBLE DOSAGES\]

> Strength Mismatch Report

> \[PSS STRENGTH MISMATCH\]

> Enter/Edit Dosages \[PSS EDIT DOSAGES\]

> Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

> Mark PreMix Solutions

> \[PSS MARK PREMIX SOLUTIONS\]

> IV Solution Report

> \[PSS IV SOLUTION REPORT\]

> Administration Schedule File Report \[PSS SCHEDULE REPORT\]

> Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

IV Additive/Solution …

> \[PSS ADDITIVE/SOLUTION\]

IV Additive Report

> \[PSS IV ADDITIVE REPORT\]

> IV Solution Report

> \[PSS IV SOLUTION REPORT\]

> Mark PreMix Solutions

> \[PSS MARK PREMIX SOLUTIONS\]

> Warning Builder

> \[PSS WARNING BUILDER\]

> Warning Mapping

> \[PSS WARNING MAPPING\]

> After installing PSS\*1\*155 and MOCHA V. 1.0 (PSS\*1\*117), your current PSS MGR menu will look as shown below. The option Auto Create Dosages \[PSS DOSAGE CONVERSION\] has been removed from the Dosages ... \[PSS DOSAGES MANAGEMENT\] menu.

> Pharmacy Data Management \[PSS MGR\]

> CMOP Mark/Unmark (Single drug) \[PSSXX MARK\] ![](pss-1-155-technical-manual-security-guide-change-pages/004.png)

> Dosages…

> \[PSS DOSAGES MANAGEMENT\]

> Dosage Form File Enter/Edit \[PSS DOSAGE FORM EDIT\]

> Enter/Edit Dosages \[PSS EDIT DOSAGES\]

> Most Common Dosages Report \[PSS COMMON DOSAGES\]

> Noun/Dosage Form Report

> \[PSS DOSE FORM/ NOUN REPORT\]

> Review Dosages Report

> \[PSS DOSAGE REVIEW REPORT\]

> Local Possible Dosages Report

> \[PSS LOCAL POSSIBLE DOSAGES\]

> Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

> Drug Enter/Edit

> \[PSS DRUG ENTER/ EDIT\]

> Order Check Management

> \[PSS ORDER CHECK MANAGEMENT\]

> Request Changes to Enhanced Order Check Database \[PSS ORDER CHECK CHANGES\]

> Report of Locally Entered Interactions \[PSS REPORT LOCAL INTERACTIONS\]

> Electrolyte File (IV) \[PSSJI ELECTROLYTE FILE\]

> Lookup into Dispense Drug File \[PSS LOOK\]

> Medication Instruction Management ...

> \[PSS MED INSTRUCTION MANAGEMENT\]

> Medication Instruction File Add/Edit \[PSSJU MI\]

> Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

> Medication Routes Management ...

> \[PSS MEDICATION ROUTES MGMT\]

> Medication Route File Enter/Edit \[PSS MEDICATION ROUTES EDIT\]

> Medication Route Mapping Report

> \[PSS MED ROUTE MAPPING REPORT\]

> Medication Route Mapping History Report \[PSS MED ROUTE MAPPING CHANGES\]

> Request Change to Standard Medication Route \[PSS MEDICATION ROUTE REQUEST\]

> Default Med Route for OI Report \[PSS DEF MED ROUTE OI RPT\]

> Orderable Item Management

\[PSS ORDERABLE ITEM MANAGEMENT\]

> Edit Orderable Items

> \[PSS EDIT ORDERABLE ITEMS\]

> Dispense Drug/Orderable Item Maintenance \[PSS MAINTAIN ORDERABLE ITEMS\]

> Orderable Item/Dosages Report

> \[PSS ORDERABLE ITEM DOSAGES

> Patient Instructions Report

> \[PSS INSTRUCTIONS/ ITEMS REPORT\]

> Orderable Item Report

> \[PSS ORDERABLE ITEM REPORT\]

> Formulary Information Report \[PSSNFI\]

> Drug Text Management ...

> \[PSS DRUG TEXT MANAGEMENT\]

> Drug Text Enter/Edit \[PSS EDIT TEXT\]

> Drug Text File Report

> \[PSS DRUG TEXT FILE REPORT

> Pharmacy System Parameters Edit \[PSS SYS EDIT\]

> Standard Schedule Management ... \[PSS SCHEDULE MANAGEMENT\]

> Standard Schedule Edit \[PSS SCHEDULE EDIT\]

> Administration Schedule File Report \[PSS SCHEDULE REPORT\]

> Synonym Enter/Edit \[PSS SYNONYM EDIT\]

> Controlled Substances/PKI Reports \[PSS CS/PKI REPORTS\]

> DEA Spec Hdlg & CS Fed Sch Discrepancy \[PSS DEA VS CS FED. SCH. DISCR.\]

> Controlled Substances Not Matched to NDF \[PSS CS NOT MATCHED TO NDF\]

> CS (DRUGS) Inconsistent with DEA Spec Hdlg \[PSS CS DRUGS INCON WITH DEA\]

> CS (Ord. Item) Inconsistent with DEA Spec Hdlg

> \[PSS CS (OI) INCON WITH DEA\]

> Send Entire Drug File to External Interface \[PSS MASTER FILE ALL\]

> IV Additive/Solution …

> \[PSS ADDITIVE/SOLUTION\]

> IV Additive Report

> \[PSS IV ADDITIVE REPORT\]

> IV Solution Report

> \[PSS IV SOLUTION REPORT\]

> Mark PreMix Solutions

> \[PSS MARK PREMIX SOLUTIONS\]

> Warning Builder

> \[PSS WARNING BUILDER\]

> Warning Mapping

> \[PSS WARNING MAPPING\]

> PEPS Services

> \[PSS PEPS SERVICES\]

> Check Vendor Database Link

> \[PSS CHECK VENDOR DATABASE LINK\]

> Check PEPS Services Setup

> \[PSS CHECK PEPS SERVICES SETUP\]

> Schedule/Reschedule Check PEPS Interface \[PSS SCHEDULE PEPS INTERFACE CK\]

## The following routines are used by the Pharmacy Data Management package.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| PSS117EN | PSS117PO | PSS129EN | PSS147EN | PSS147PO | PSS32P3  |
|----------|----------|----------|----------|----------|----------|
| PSS32P5  | PSS350F1 | PSS50    | PSS50A   | PSS50A1  | PSS50AQM |
| PSS50ATC | PSS50B   | PSS50B1  | PSS50B2  | PSS50C   | PSS50C1  |
| PSS50CMP | PSS50D   | PSS50DAT | PSS50DOS | PSS50E   | PSS50F   |
| PSS50LAB | PSS50NDF | PSS50P4  | PSS50P66 | PSS50P7  | PSS50P7A |
| PSS50TMP | PSS50WS  | PSS51    | PSS51P1  | PSS51P15 | PSS51P1A |
| PSS51P1B | PSS51P1C | PSS51P2  | PSS51P5  | PSS52P6  | PSS52P6A |
| PSS52P6B | PSS52P7  | PSS52P7A | PSS54    | PSS55    | PSS551   |
| PSS55MIS | PSS59P7  | PSS781   | PSSADDIT | PSSADRPT | PSSAUTL  |
| PSSCHENV | PSSCHPRE | PSSCHPST | PSSCLDRG | PSSCOMMN | PSSCPRS  |
| PSSCPRS1 | PSSCREAT | PSSCSPD  | PSSCUSRQ | PSSDAWUT | PSSDDUT  |
| PSSDDUT2 | PSSDDUT3 | PSSDEE   | PSSDEE1  | PSSDEE2  | PSSDELOI |
| PSSDENT  | PSSDFEE  | PSSDGUPD | PSSDI    | PSSDIN   | PSSDOS   |
| PSSDOSCR | PSSDOSCX | PSSDOSED | PSSDOSER | PSSDOSRP | PSSDSAPA |
| PSSDSAPD | PSSDSAPI | PSSDSAPK | PSSDSAPL | PSSDSAPM | PSSDSBBP |
| PSSDSBDA | PSSDSBDB | PSSDSBPA | PSSDSBPB | PSSDSBPC | PSSDSBPD |
| PSSDSDAT | PSSDSEXC | PSSDSFDB | PSSDSPON | PSSDSPOP | PSSDTR   |
| PSSENV   | PSSENVN  | PSSFDBRT | PSSFIL   | PSSFILED | PSSFILES |
| PSSGENM  | PSSGIU   | PSSGMI   | PSSGS0   | PSSGSH   | PSSHELP  |
| PSSHFREQ | PSSHL1   | PSSHLSCH | PSSHLU   | PSSHRCOM | PSSHRENV |
| PSSHREQ  | PSSHRIT  | PSSHRPST | PSSHRQ2  | PSSHRQ21 | PSSHRQ22 |
| PSSHRQ23 | PSSHRQ2O | PSSHRVAL | PSSHRVL1 | PSSHTTP  | PSSJEEU  |
| PSSJORDF | PSSJSPU  | PSSJSPU0 | PSSJSV   | PSSJSV0  | PSSJXR   |
| PSSJXR1  | PSSJXR10 | PSSJXR11 | PSSJXR12 | PSSJXR13 | PSSJXR14 |
| PSSJXR15 | PSSJXR16 | PSSJXR17 | PSSJXR18 | PSSJXR19 | PSSJXR2  |
| PSSJXR20 | PSSJXR21 | PSSJXR22 | PSSJXR4  | PSSJXR5  | PSSJXR6  |
| PSSJXR7  | PSSJXR8  | PSSJXR9  | PSSLAB   | PSSLDALL | PSSLDEDT |
| PSSLDOSE | PSSLDOSE | PSSLOOK  | PSSMARK  | PSSMATCH | PSSMEDCH |
| PSSMEDRQ | PSSMEDRT | PSSMEDX  | PSSMIRPT | PSSMRTUP | PSSMRTUX |
| PSSMSTR  | PSSNDCUT | PSSNOUNR | PSSNTEG  | PSSOICT  | PSSOICT1 |
| PSSOPKI  | PSSOPKI1 | PSSORPH  | PSSORPH1 | PSSORUTL | PSSOUTSC |
| PSSPKIPI | PSSPKIPR | PSSPNSRP | PSSPO129 | PSSPOI   | PSSPOIC  |
| PSSPOID1 | PSSPOID2 | PSSPOID3 | PSSPOIDT | PSSPOIKA | PSSPOIM  |
| PSSPOIM1 | PSSPOIM2 | PSSPOIM3 | PSSPOIMN | PSSPOIMO | PSSPOST  |
| PSSPOST1 | PSSPOST2 | PSSPOST5 | PSSPRE   | PSSPRETR | PSSPRMIX |
| PSSPRUTL | PSSQORD  | PSSREF   | PSSREMCH | PSSSCHED | PSSSCHRP |
| PSSSOLI1 | PSSSOLIT | PSSSPD   | PSSSUTIL | PSSSYN   | PSSTRENG |
| PSSUTIL  | PSSUTIL3 | PSSUTLA1 | PSSUTLPR | PSSVIDRG | PSSVX6   |

> *(This page included for two-sided copying.)*

> 26 Pharmacy Data Management V. 1.0 September 1997 Technical Manual/Security Guide

## The PDM menu that was exported with the original PDM package has been modified to include subsequent changes and patches.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PDM menu including PSS\*1\*155, but not PSS\*1\*117 (MOCHA V. 1.0), appears below:

> Pharmacy Data Management \[PSS MGR\]

> CMOP Mark/Unmark (Single drug) \[PSSXX MARK\] ![](pss-1-155-technical-manual-security-guide-change-pages/005.png)

> Dosages…

> \[PSS DOSAGES MANAGEMENT\]

> Dosage Form File Enter/Edit \[PSS DOSAGE FORM EDIT\]

> Enter/Edit Dosages \[PSS EDIT DOSAGES\]

> Most Common Dosages Report \[PSS COMMON DOSAGES\]

> Noun/Dosage Form Report

> \[PSS DOSE FORM/ NOUN REPORT\]

> Review Dosages Report

> \[PSS DOSAGE REVIEW REPORT\]

> Local Possible Dosages Report

> \[PSS LOCAL POSSIBLE DOSAGES\]

> Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

> Drug Enter/Edit

> \[PSS DRUG ENTER/ EDIT\]

> Drug Interaction Management

> \[PSS DRG INTER MANAGEMENT\]

> Enter/Edit Local Drug Interaction \[PSS INTERACTION LOCAL ADD\]

> Report of Locally Entered Interactions \[PSS REPORT LOCAL INTERACTIONS\]

> Electrolyte File (IV)

> \[PSSJI ELECTROLYTE FILE\]

September 1997 Pharmacy Data Management V. 1.0 29

> Technical Manual/Security Guide PSS\*1\*155

> Lookup into Dispense Drug File \[PSS LOOK\]

> Medication Instruction Management ...

> \[PSS MED INSTRUCTION MANAGEMENT\]

> Medication Instruction File Add/Edit \[PSSJU MI\]

> Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

> Medication Routes Management ...

> \[PSS MEDICATION ROUTES MGMT\]

> Medication Route File Enter/Edit \[PSS MEDICATION ROUTES EDIT\]

> Medication Route Mapping Report

> \[PSS MED ROUTE MAPPING REPORT\]

> Medication Route Mapping History Report \[PSS MED ROUTE MAPPING CHANGES\]

> Request Change to Standard Medication Route \[PSS MEDICATION ROUTE REQUEST\]

> Default Med Route for OI Report \[PSS DEF MED ROUTE OI RPT\]

> Orderable Item Management

\[PSS ORDERABLE ITEM MANAGEMENT\]

> Edit Orderable Items

> \[PSS EDIT ORDERABLE ITEMS\]

> Dispense Drug/Orderable Item Maintenance \[PSS MAINTAIN ORDERABLE ITEMS\]

> Orderable Item/Dosages Report

> \[PSS ORDERABLE ITEM DOSAGES

> 30 Pharmacy Data Management V. 1.0 September 1997 Technical Manual/Security Guide

> Patient Instructions Report

> \[PSS INSTRUCTIONS/ ITEMS REPORT\]

> Orderable Item Report

> \[PSS ORDERABLE ITEM REPORT\]

> Formulary Information Report \[PSSNFI\]

> Drug Text Management ...

> \[PSS DRUG TEXT MANAGEMENT\]

> Drug Text Enter/Edit \[PSS EDIT TEXT\]

> Drug Text File Report

> \[PSS DRUG TEXT FILE REPORT

> Pharmacy System Parameters Edit \[PSS SYS EDIT\]

> Standard Schedule Management ... \[PSS SCHEDULE MANAGEMENT\]

> Standard Schedule Edit \[PSS SCHEDULE EDIT\]

> Administration Schedule File Report \[PSS SCHEDULE REPORT\]

> Synonym Enter/Edit \[PSS SYNONYM EDIT\]

> Controlled Substances/PKI Reports \[PSS CS/PKI REPORTS\]

> DEA Spec Hdlg & CS Fed Sch Discrepancy \[PSS DEA VS CS FED. SCH. DISCR.\]

> Controlled Substances Not Matched to NDF \[PSS CS NOT MATCHED TO NDF\]

> CS (DRUGS) Inconsistent with DEA Spec Hdlg \[PSS CS DRUGS INCON WITH DEA\]

> CS (Ord. Item) Inconsistent with DEA Spec Hdlg

> September 1997 Pharmacy Data Management V. 1.0 30a Technical Manual/Security Guide

> PSS\*1\*155

> \[PSS CS (OI) INCON WITH DEA\]

> Send Entire Drug File to External Interface \[PSS MASTER FILE ALL\]

> Enhanced Order Checks Setup Menu \[PSS ENHANCED ORDER CHECKS\]

> Find Unmapped Local Medication Routes \[PSS MED ROUTES INITIAL MAPPING\]

> Map Local Medication Route to Standard \[PSS MAP ONE MED ROUTE\]

> Medication Route Mapping Report

> \[PSS MED ROUTE MAPPING REPORT\]

> Medication Route File Enter/Edit \[PSS MEDICATION ROUTES EDIT\]

> Medication Route Mapping History Report \[PSS MED ROUTE MAPPING CHANGES\]

> Request Change to Standard Medication Route \[PSS MEDICATION ROUTE REQUEST\]

> Find Unmapped Local Possible Dosages \[PSS LOCAL DOSAGES EDIT ALL\]

> Map Local Possible Dosages \[PSS LOCAL DOSAGES EDIT\]

> Local Possible Dosages Report

> \[PSS LOCAL POSSIBLE DOSAGES\]

> Strength Mismatch Report

> \[PSS STRENGTH MISMATCH\]

> Enter/Edit Dosages \[PSS EDIT DOSAGES\]

> Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

> Mark PreMix Solutions

> 30b Pharmacy Data Management V. 1.0 September 1997 Technical Manual/Security Guide

> \[PSS MARK PREMIX SOLUTIONS\]

> IV Solution Report

> \[PSS IV SOLUTION REPORT\]

> Administration Schedule File Report \[PSS SCHEDULE REPORT\]

> Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

> IV Additive/Solution …

> \[PSS ADDITIVE/SOLUTION\]

> IV Additive Report

> \[PSS IV ADDITIVE REPORT\]

> IV Solution Report

> \[PSS IV SOLUTION REPORT\]

> Mark PreMix Solutions

> \[PSS MARK PREMIX SOLUTIONS\]

> Warning Builder

> \[PSS WARNING BUILDER\]

> Warning Mapping

> \[PSS WARNING MAPPING\]

> September 1997 Pharmacy Data Management V. 1.0 30c Technical Manual/Security Guide

> PSS\*1\*155

> The PDM menu up to and including PSS\*1\*155 appears below. PSS\*1\*155 was the last patch to affect a change to the PDM menu.

> After installing PSS\*1\*155 and MOCHA V. 1.0 (PSS\*1\*117), your current PSS MGR menu will look as shown below. The option Auto Create Dosages \[PSS DOSAGE CONVERSION\] has been removed from the Dosages ... \[PSS DOSAGES MANAGEMENT\] menu.

> Pharmacy Data Management \[PSS MGR\]

> CMOP Mark/Unmark (Single drug) \[PSSXX MARK\] ![](pss-1-155-technical-manual-security-guide-change-pages/006.png)

> Dosages…

> \[PSS DOSAGES MANAGEMENT\]

> Dosage Form File Enter/Edit \[PSS DOSAGE FORM EDIT\]

> Enter/Edit Dosages \[PSS EDIT DOSAGES\]

> Most Common Dosages Report \[PSS COMMON DOSAGES\]

> Noun/Dosage Form Report

> \[PSS DOSE FORM/ NOUN REPORT\]

> Review Dosages Report

> \[PSS DOSAGE REVIEW REPORT\]

> Local Possible Dosages Report

> \[PSS LOCAL POSSIBLE DOSAGES\]

> Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

> Drug Enter/Edit

> \[PSS DRUG ENTER/ EDIT\]

> Order Check Management

> \[PSS ORDER CHECK MANAGEMENT\]

> Request Changes to Enhanced Order Check Database \[PSS ORDER CHECK CHANGES\]

> Report of Locally Entered Interactions \[PSS REPORT LOCAL INTERACTIONS\]

> 30d Pharmacy Data Management V. 1.0 September 1997 Technical Manual/Security Guide

> Electrolyte File (IV)

> \[PSSJI ELECTROLYTE FILE\]

> Lookup into Dispense Drug File \[PSS LOOK\]

> Medication Instruction Management ...

> \[PSS MED INSTRUCTION MANAGEMENT\]

> Medication Instruction File Add/Edit \[PSSJU MI\]

> Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

> Medication Routes Management ...

> \[PSS MEDICATION ROUTES MGMT\]

> Medication Route File Enter/Edit \[PSS MEDICATION ROUTES EDIT\]

> Medication Route Mapping Report

> \[PSS MED ROUTE MAPPING REPORT\]

> Medication Route Mapping History Report \[PSS MED ROUTE MAPPING CHANGES\]

> Request Change to Standard Medication Route \[PSS MEDICATION ROUTE REQUEST\]

> Default Med Route for OI Report \[PSS DEF MED ROUTE OI RPT\]

> Orderable Item Management

> \[PSS ORDERABLE ITEM MANAGEMENT\]

> Edit Orderable Items

> \[PSS EDIT ORDERABLE ITEMS\]

> Dispense Drug/Orderable Item Maintenance \[PSS MAINTAIN ORDERABLE ITEMS\]

> Orderable Item/Dosages Report

> \[PSS ORDERABLE ITEM DOSAGES

> September 1997 Pharmacy Data Management V. 1.0 30e Technical Manual/Security Guide

> PSS\*1\*155

> Patient Instructions Report

> \[PSS INSTRUCTIONS/ ITEMS REPORT\]

> Orderable Item Report

> \[PSS ORDERABLE ITEM REPORT\]

> Formulary Information Report \[PSSNFI\]

> Drug Text Management ...

> \[PSS DRUG TEXT MANAGEMENT\]

> Drug Text Enter/Edit \[PSS EDIT TEXT\]

> Drug Text File Report

> \[PSS DRUG TEXT FILE REPORT

> Pharmacy System Parameters Edit \[PSS SYS EDIT\]

> Standard Schedule Management ... \[PSS SCHEDULE MANAGEMENT\]

> Standard Schedule Edit \[PSS SCHEDULE EDIT\]

> Administration Schedule File Report \[PSS SCHEDULE REPORT\]

> Synonym Enter/Edit \[PSS SYNONYM EDIT\]

> Controlled Substances/PKI Reports \[PSS CS/PKI REPORTS\]

> DEA Spec Hdlg & CS Fed Sch Discrepancy \[PSS DEA VS CS FED. SCH. DISCR.\]

> Controlled Substances Not Matched to NDF \[PSS CS NOT MATCHED TO NDF\]

> CS (DRUGS) Inconsistent with DEA Spec Hdlg \[PSS CS DRUGS INCON WITH DEA\]

> 30f Pharmacy Data Management V. 1.0 September 1997 Technical Manual/Security Guide

> CS (Ord. Item) Inconsistent with DEA Spec Hdlg \[PSS CS (OI) INCON WITH DEA\]

> Send Entire Drug File to External Interface \[PSS MASTER FILE ALL\]

IV Additive/Solution …

> \[PSS ADDITIVE/SOLUTION\]

IV Additive Report

> \[PSS IV ADDITIVE REPORT\]

> IV Solution Report

> \[PSS IV SOLUTION REPORT\]

> Mark PreMix Solutions

> \[PSS MARK PREMIX SOLUTIONS\]

> Warning Builder

> \[PSS WARNING BUILDER\]

> Warning Mapping

> \[PSS WARNING MAPPING\]

> PEPS Services

> \[PSS PEPS SERVICES\]

> Check Vendor Database Link

> \[PSS CHECK VENDOR DATABASE LINK\]

> Check PEPS Services Setup

> \[PSS CHECK PEPS SERVICES SETUP\]

> Schedule/Reschedule Check PEPS Interface \[PSS SCHEDULE PEPS INTERFACE CK\]

> September 1997 Pharmacy Data Management V. 1.0 30g Technical Manual/Security Guide

> PSS\*1\*155

> *\<This page left blank for two-sided copying.\>*

> 30h Pharmacy Data Management V. 1.0 September 1997 Technical Manual/Security Guide

## In order to mark or edit package specific fields in a DRUG file (#50) entry, the user must hold the corresponding package key. The keys are assigned for the individual packages. PDM does not export any of these keys.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Package Keys

## Outpatient Pharmacy PSORPH

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Inpatient Medications PSJU MGR

## Inpatient Medications PSJI MGR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Automatic Replenishment/Ward Stock PSGWMGR

## Drug Accountability/Inventory Interface PSAMGR Drug Accountability/Inventory Interface PSA ORDERS Controlled Substances PSDMGR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> National Drug File PSNMGR

## Consolidated Mail Outpatient Pharmacy PSXCMOPMGR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PSS\*1\*147 exports the following four security keys, that will be used by the Pharmacy Enterprise Customization System (PECS) application. Only a few users who will be granted access to the PECS application will need one or more keys assigned based on their role.

## Assignment of these keys should be by request only. The security key descriptions were retrieved from VA FileMan.
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### From: PSS*1*159 Technical Manual/Security Guide Change Pages

## For Outpatient Pharmacy & Inpatient Medication Unit Dose Orders:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Default med route will be returned from the DEFAULT MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) if it is populated, or from the POSSIBLE MED ROUTES multiple (#50.711) of the PHARMACY ORDERABLE ITEM file (#50.7) if it is populated with a single entry and the USE DOSAGE FORM MED ROUTE LIST field (#10) is set to "NO." The med route selection list will be returned with entries from the POSSIBLE MED ROUTES multiple (#50.711) if the USE DOSAGE FORM MED ROUTE LIST field (#10) is set to "NO." Otherwise, the med routes associated with the orderable item's dosage form, MED ROUTE FOR DOSAGE FORM multiple (#50.6061) of the DOSAGE FORM file (#50.606), will be returned.

## For IV Fluids Orders:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If there is only one orderable item in the IV order request, the same logic as defined above under 'For Outpatient Pharmacy & Inpatient Medication Unit Dose Orders' will be used to return the default med route from the DEFAULT MED ROUTE field (#.06) and the med route selection list from the PHARMACY ORDERABLE ITEM file (#50.7).

> If there is more than one orderable item on the IV order request, the PHARMACY ORDERABLE ITEM file (#50.7) will be checked for each orderable item for the default med route and med route selection list as defined above under 'For Outpatient Pharmacy & Inpatient Medication Unit Dose Orders.' If there is a default med route common with every orderable item, that default med route will be returned. Similarly, the list of possible med routes that are common with every orderable item will be returned.

## Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IAs can be viewed by first choosing the *DBA* option on FORUM and then the *Integration Agreement*s *Menu* option.

> Example: DBA Option

## Package Minimum version needed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> National Drug File V. 3.15

> Outpatient Pharmacy V. 6.0

> Inpatient Medications V. 4.5

> Kernel V. 8.0 (plus all patches, particularly

> XU\*8\*28)

> VA FileMan V. 21.0 (plus all patches)

> 34 Pharmacy Data Management V. 1.0 September 1997

### From: PSS*1*129 Technical Manual/Security Guide Change Pages

### Package Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Outpatient Pharmacy PSORPH

> Inpatient Medications PSJU MGR

> Inpatient Medications PSJI MGR

> Automatic Replenishment/Ward Stock PSGWMGR

> Drug Accountability/Inventory Interface PSAMGR Drug Accountability/Inventory Interface PSA ORDERS Controlled Substances PSDMGR

> National Drug File PSNMGR

> Consolidated Mail Outpatient Pharmacy PSXCMOPMGR

### PDM Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 29%" />
<col style="width: 21%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong><u>File</u> <u>Numbers</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>File Names</u></strong></p>
</blockquote></th>
<th><strong><u>DD</u></strong></th>
<th><blockquote>
<p><strong><u>RD</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>WR</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>DEL</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>LAYGO</u></strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><blockquote>
<p>50 DRUG @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>50.4 DRUG ELECTROLYTES @</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>50.606 DOSAGE FORM @ @ @ @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>50.7 PHARMACY ORDERABLE ITEM @</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>51 MEDICATION INSTRUCTION @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>51.1 ADMINISTRATION SCHEDULE @</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>51.2 MEDICATION ROUTES @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>51.23 STANDARD MEDICATION ROUTES @ Pp @ @ @</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>51.24 DOSE UNIT @ Pp @ @ @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>51.5 ORDER UNIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>51.7 DRUG TEXT @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>52.6 IV ADDITIVES @</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>52.7 IV SOLUTIONS @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>54 RX CONSULT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>55 PHARMACY PATIENT (Partial DD) @ P</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>59.7 PHARMACY SYSTEM ^ ^ ^ ^</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Non-PDM Files

<table style="width:100%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 20%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong><u>File</u> <u>Numbers</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>File Names</u></strong></p>
</blockquote></th>
<th><strong><u>DD</u></strong></th>
<th><blockquote>
<p><strong><u>RD</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>WR</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>DEL</u></strong></p>
</blockquote></th>
<th><blockquote>
<p><strong><u>LAYGO</u></strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><blockquote>
<p>200 NEW PERSON (Partial DD) # # # # #</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>9009032.3 APSP INTERVENTION TYPE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>9009032.4 APSP INTERVENTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>9009032.5 APSP INTERVENTION RECOMMENDATION</p>
</blockquote></td>
</tr>
</tbody>
</table>

![](pss-1-129-technical-manual-security-guide-change-pages/007.png)

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Administration Schedule File The ADMINISTRATION SCHEDULE file (#51.1)
> contains administration schedule names and standard dosage administration times. The name is a common abbreviation for an administration schedule (e.g., QID, Q4H, PRN). The administration time is entered in military time.
> CPRS A VistA computer software package called Computerized Patient Record System. CPRS is an application in VistA that allows the user to enter all necessary orders for a patient in different packages from a single application.
> Dispense Drug The Dispense Drug is pulled from DRUG file (#50) and usually has the strength attached to it (e.g., Acetaminophen 325 mg). Usually, the name alone without a strength attached is the Pharmacy Orderable Item name.
> Dosage Form File The DOSAGE FORM file (#50.606) contains all dosage forms and associated data that are used by Pharmacy packages and CPRS. The dosage form is used in SIG construction, default values and in the determination of the type of each dosage created for each application.
> Dose Unit File The DOSE UNIT file (#51.24) was created to accomplish the mapping to First Data Bank (FDB). All entries in this file have been mapped to an FDB Dose Unit. Although this file has not yet been standardized by Standards and Terminology Services (SRS), no local editing will be allowed. When populating the Dose Unit field for a Local Possible Dosage, selection will be from this new file.
> Drug Electrolytes File The DRUG ELECTROLYTES file (#50.4) contains the
> names of anions/cations, and their cations and concentration units.
> Drug File The DRUG file (#50) holds the information related to each drug that can be used to fill a prescription or medication order. It is pointed to from several other files and should be handled carefully, usually only by special individuals in the Pharmacy Service. Entries are not typically deleted, but rather made inactive by entering an inactive date.
> Drug Interaction File The DRUG INTERACTION file (#56) is used to store
> DRUG-DRUG interactions. The file is sent out
> with data pre-populated. The pre-populated data cannot be deleted, data can only be added, or the severity of the national data can be elevated locally.
> Drug Text File The DRUG TEXT file (#51.7) stores rapidly changing drug restrictions, guidelines, and protocols to help assure medications are being used according to defined specifications.
> IV Additives File The IV ADDITIVES file (#52.6) contains drugs that are used as Additives in the IV room. Data entered includes drug generic name, print name, drug information, synonym(s), dispensing units, cost per unit, days for IV order, usual IV schedule, administration times, electrolytes, and quick code information.
> IV Solutions File The IV SOLUTIONS file (#52.7) contains drugs that are used as primary solutions in the IV room. The solution must already exist in the DRUG file (#50) to be selected. Data in this file includes: drug generic name, print name, status, drug information, synonym(s), volume, and electrolytes.
> Local Possible Dosages Local Possible Dosages are free text dosages that are
> associated with drugs that do not meet all of the criteria for Possible Dosages.
> Medication Instruction File The MEDICATION INSTRUCTION file (#51) is used
> by Unit Dose and Outpatient Pharmacy. It contains the medication instruction name, expansion and intended use.
> Medication Routes File The MEDICATION ROUTES file (#51.2) contains
> medication route names. The user can enter an abbreviation for each route to be used at their site. The abbreviation will most likely be the Latin abbreviation for the term.
> Medication Routes/Abbreviations The MEDICATION ROUTES file (#51.2) contains the
> medication routes and abbreviations, which are selected by each Department of Veterans Affairs Medical Centers (VAMC). The abbreviation cannot be longer than five characters to fit on labels and the Medical Administration Record (MAR). The user can add new routes and abbreviations as appropriate.
> National Drug File The National Drug File provides standardization of the local drug files in all VA medical facilities.
> Standardization includes the adoption of new drug nomenclature and drug classification and links the local drug file entries to data in the National Drug File. For drugs approved by the Food and Drug Administration (FDA), VA medical facilities have access to information concerning dosage form, strength and unit; package size and type; manufacturer's trade name; and National Drug Code (NDC). The NDF software lays the foundation for sharing prescription information among medical facilities.
> Non-Formulary Drugs Drugs that are not available for use by all providers.
> Orderable Item An Orderable Item is pulled from the PHARMACY ORDERABLE ITEM file (#50.7) and usually has no strength attached to it (e.g., Acetaminophen). The name, with a strength attached, is the Dispense Drug name (e.g., Acetaminophen 325mg).
> Orderable Item File The ORDERABLE ITEM file (#101.43) is a CPRS file that provides the Orderable Items for selection within CPRS. Pharmacy Orderable Items are a subset of this file.
> Pending Order A pending order is one that has been entered by a provider through CPRS without Pharmacy finishing the order. Once Pharmacy has finished (and verified for Unit Dose only) the order, it will become active.
> Pharmacy Orderable Item The Pharmacy Orderable Item is used through CPRS to
> order Inpatient Medications and Outpatient Pharmacy prescriptions.
> Pharmacy Orderable Item File The PHARMACY ORDERABLE ITEM file (#50.7)
> contains the Order Entry name for items that can be ordered in the Inpatient Medications and Outpatient Pharmacy packages.
> Possible Dosages Dosages that have a numeric dosage and numeric Dispense Units Per Dose appropriate for administration. For a drug to have possible dosages, it must be a single ingredient product that is matched to VA PRODUCT file (#50.68). The VA PRODUCT file (#50.68) entry must have a numeric strength and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.
> Prompt A point at which the system questions the user and waits for a response.
> Standard Medication Route File The STANDARD MEDICATION ROUTE file
> (#51.23) was created to map Local Medication Routes in VistA to an FDB Route in order to perform dosage checks in PRE V.0.5. This file has been standardized by Standards and Terminology Service (STS) and is mapped to an FDB Route. It cannot be edited locally.
> Standard Schedule Standard medication administration schedules are stored in the ADMINISTRATION SCHEDULE file (#51.1).
> Units Per Dose The Units Per Dose is the number of Units (tablets, capsules, etc.) to be dispensed as a dose for an order. Fractional numbers will be accepted.
> VA Drug Class Code A drug classification system used by VA that separates
> drugs into different categories based upon their characteristics. Some cost reports can be run for VA Drug Class Codes.
> VA Product File The VA PRODUCT file (#50.68) contains a list of available drug products.

### From: PSS*1*94 Technical Manual/Security Guide Change Pages

## Revision History 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 52%" />
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
<td>08/08</td>
<td><blockquote>
<p>iii, 25, 33-34</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*94</p>
</blockquote></td>
<td><p>Added Medication Routes and Administration Scheduling sections. Added PSSSCHED routine.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>10/06</td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*112</p>
</blockquote></td>
<td><p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routines PSS55MIS and PSS50TMP to the Routine List.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>09/06</td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*108</p>
</blockquote></td>
<td><p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routine PSS551 to the Routine List.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/06</td>
<td><blockquote>
<p>i, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*90</p>
</blockquote></td>
<td><p>HIPAA NCPDP Global project. Added routines PSSDAWUT and PSSNDCUT to the Routine List.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/06</td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*106</p>
</blockquote></td>
<td><p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routine PSS781 to the Routine List.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/05</td>
<td><blockquote>
<p>i, ii, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*101</p>
</blockquote></td>
<td><p>Pharmacy Re-Engineering (PRE) Encapsulation Cycle II project. Added routines PSS55 and PSS59P7 to the Routine List.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>03/05</td>
<td><blockquote>
<p>i, ii, 24a, 25, 29-31, 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*87</p>
</blockquote></td>
<td>Laser Labels Phase II project. Added <em>Warning Builder</em> and <em>Warning Mapping</em> options descriptions and updated the menu options. Added four new routines to the routine list. Cleaned up misspelled words and such on many pages. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/04</td>
<td><blockquote>
<p>i., 25, 33</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*85</p>
</blockquote></td>
<td>Added routines and a reference to the <em>Pharmacy Re- Engineering (PRE) Application Program Interface (API) Manual</em> created for the Pharmacy Re-Engineering (PRE) project Encapsulation cycle 1.</td>
</tr>
<tr class="odd">
<td>10/04</td>
<td><blockquote>
<p>i, 24a, 25, 29-</p>
<p>31, 32d-h, 48,</p>
<p>53</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*82</p>
</blockquote></td>
<td>Updated the option description to include <em>Send Entire Drug File to External Interface</em> [PSS MASTER FILE ALL] option. Added new master file update information to the "HL7 Messaging with an External System" section. Updated routine list to include PSSMSTR. Updated the web address for the VistA Documentation Library (VDL).</td>
</tr>
<tr class="even">
<td>07/03</td>
<td><blockquote>
<p>i, 25, 31, 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*61</p>
</blockquote></td>
<td>Updated routine list to four new add PKI routines. Added new <em>Controlled Substances/PKI Reports</em> [PSS/PKI REPORTS] menu and four associated report options to the</td>
</tr>
</tbody>
</table>

> August 2008 Pharmacy Data Management V. 1.0 i

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 52%" />
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
<td></td>
<td></td>
<td></td>
<td><em>Pharmacy Data Management</em> [PSS MGR] menu.</td>
</tr>
<tr class="even">
<td>04/03</td>
<td><blockquote>
<p>i, 5, 8, 29, 35,</p>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*68</p>
</blockquote></td>
<td>Updated patch references to include PSS*1*68. Added NON-VA MED field (#8) to the PHARMACY ORDERABLE ITEM file (#50.7).</td>
</tr>
<tr class="odd">
<td>03/03</td>
<td><blockquote>
<p>i., 5, 8, 24a,</p>
<p>29, 31, 35, 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*47</p>
</blockquote></td>
<td><p>Updated patch references to include PSS*1*47. Added new field OTHER LANGUAGE INSTRUCTIONS (#7.1) to the PHARMACY</p>
<p>ORDERABLE ITEM file (#50.7) list and <em>Other Language Translation Setup</em> option description.</p></td>
</tr>
<tr class="even">
<td>11/02</td>
<td><blockquote>
<p>i, ii 5, (6)</p>
<p>23 - 25, (26)</p>
<p>29-30,(47), 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*55</p>
</blockquote></td>
<td>Renumbered front matter starting from this Revision History page. Updated Patch number. Updated Option descriptions to include <em>Drug Text File Report</em> option. Added routine PSSDTR in the Routines section. Added the <em>Drug Text File Report</em> option to the current PDM Menu in the Exported Options section.</td>
</tr>
<tr class="odd">
<td>10/02</td>
<td><blockquote>
<p>Title, i-iv, 32a-32d</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*57</p>
</blockquote></td>
<td>Updated Title Page, Revision Page and Table of Contents. A section was added for the new HL7 Messaging with an External System.</td>
</tr>
<tr class="even">
<td>09/01</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*38</p>
</blockquote></td>
<td>Added this Revision History Page. Added Patch Release changes and Pharmacy Ordering Enhancements (POE) edits. Updated manual to comply with current documentation standards.</td>
</tr>
<tr class="odd">
<td>09/97</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>Original Release of Technical Manual.</td>
</tr>
</tbody>
</table>

> ii Pharmacy Data Management V. 1.0 August 2008
