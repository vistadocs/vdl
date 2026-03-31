---
title: PSS*1*117/136 Technical Manual/Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: 
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*117
group_key: "PSS:PSS:1"
file_numbers: []
security_keys: []
menu_options: 9
description: - [Version 1.0](#version-10) - [Revision History](#revision-history) - [Implementation and Maintenance](#implementation-and-maintenance) - [File List](#file-list) - [Routines](#routines) - [Exported Options](#exported-options) - [Protocols](#protocols) - [Bulletins](#bulletins) - [HL7 Messaging with
audience: 
keywords: 
  - blockquote
  - strong
  - class
  - colspan
  - table
  - even
  - style
  - width
  - contents
  - pharmacy
page_count: 0
word_count: 9473
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p136_and_p117_tm_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p136_and_p117_tm_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

> ![](pss-1-117-136-technical-manual-security-guide-change-pages/001.png)

PHARMACY DATA MANAGEMENT

> TECHNICAL MANUAL/ SECURITY GUIDE

## Version 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> September 1997

> (Revised April 2011)

> Department of Veterans Affairs Product Development

# Revision History 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Version 1.0](#version-10)
- [Revision History](#revision-history)
- [Implementation and Maintenance](#implementation-and-maintenance)
    - [File List](#file-list)
- [Routines](#routines)
    - [Exported Options](#exported-options)
    - [Protocols](#protocols)
    - [Bulletins](#bulletins)
    - [HL7 Messaging with an External System](#hl7-messaging-with-an-external-system)
    - [Package Requirements](#package-requirements)
- [Security Guide](#security-guide)
    - [Security Management](#security-management)
    - [Mail Groups](#mail-groups)
    - [Alerts](#alerts)
    - [Bulletins](#bulletins-1)
    - [Remote Systems](#remote-systems)
    - [Archiving/Purging](#archivingpurging)
    - [Contingency Planning](#contingency-planning)
    - [Interfacing](#interfacing)
    - [Electronic Signatures](#electronic-signatures)
    - [Menus](#menus)
    - [Security Keys](#security-keys)
    - [File Security](#file-security)
> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.
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
<p>04/11</p>
</blockquote></td>
<td><blockquote>
<p><a href="#revision-history">i</a>-iv, 5, 8, removed 8a-b, 13, 24f-g,</p>
<p>added 24h-l, 25,</p>
<p>28, added 28a-b for paging sense, 29, 30,</p>
<p>renumbered 31a-b to be 30a-b for paging sense, 31, 32, 32a,</p>
<p>35, 45-49, 51,</p>
<p>55-59, added</p>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*117and PSS*1*136</p>
</blockquote></td>
<td><blockquote>
<p>Added reference to latest patch info, PSS*1*117 and PSS*1*136;</p>
<p>Added new files VENDOR DISABLE/ENABLE (#59.73) and VENDOR INTERFACE DATA</p>
<p>(#59.74) to <strong>File List</strong> and <strong>File Security</strong> sections. Updated <strong>Options Descriptions</strong> to include the new options available after the installation of PSS*1*136 and PSS*1*117</p>
<p>Updated <strong>Routines</strong> list</p>
<p>Added new options <em>PEPS Services</em> [PSS PEPS SERVICES<em>], Check PEPS Services Setup</em> [PSS CHECK PEPS SERVICES SETUP], <em>Check Vendor</em></p>
<p><em>Database Link</em> [PSS CHECK VENDOR DATABASE LINK], and <em>Schedule/Reschedule Check PEPS Interface</em> [PSS SCHEDULE PEPS INTERFACE CK], and updated menus where they appear (<strong>Exported Options</strong>)</p>
<p>Added a <strong>Bulletins</strong> section to both Technical Manual and Security Guide and defined terms in <strong>Glossary</strong> Updated <strong>Package Requirements</strong> section</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04/11</p>
</blockquote></td>
<td><blockquote>
<p>i-iii, 5, 6,</p>
<p>8a-b, 33</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*153</p>
</blockquote></td>
<td><blockquote>
<p>Renamed the MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) to</p>
<p>be DEFAULT MED ROUTE. Provided the ability to print the POSSIBLE MED ROUTES multiple on the <em>Default Med Route For OI Report</em> [PSS DEF MED ROUTE OI RPT] option.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>02/11</p>
</blockquote></td>
<td><blockquote>
<p>i, 25</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*151</p>
</blockquote></td>
<td><blockquote>
<p>Added PSSDSAPA routine to the Routine List. Released with CPRS version 28.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>02/11</p>
</blockquote></td>
<td><blockquote>
<p>i, 33-34</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*142</p>
</blockquote></td>
<td><blockquote>
<p>Added functionality to denote the default med route for IV orders in the selection list in CPRS if all of the orderable items on the order have the same default med route defined. Released with CPRS version 28.</p>
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
<th><strong>Revised Pages</strong></th>
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
<p>i-iii, 5, 8,</p>
<p>24f, 25, 29-</p>
<p>30, 31b- 32,</p>
<p>32a-32h, 45-</p>
<p>50</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*147</p>
</blockquote></td>
<td><blockquote>
<p>Updated patch references to include PSS*1*147. Described files, fields, options and routines added/modified as part of this patch.</p>
<p><mark>REDACTED</mark> REFCQ920</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/09</p>
</blockquote></td>
<td><blockquote>
<p>i-ii, 5, 8</p>
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
<td>iii, 25, 33-34</td>
<td><blockquote>
<p>PSS*1*94</p>
</blockquote></td>
<td><blockquote>
<p>Added Medication Routes and Administration Scheduling sections. Added PSSSCHED routine. <mark>REDACTED</mark></p>
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
<tr class="even">
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
<tr class="even">
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
<p>Added routines and a reference to the <em>Pharmacy Re- Engineering (PRE) Application Program Interface (API) Manual</em> created for the Pharmacy Re- Engineering (PRE) project Encapsulation cycle 1.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10/04</p>
</blockquote></td>
<td><blockquote>
<p>i, 24a, 25,</p>
<p>29-31, 32d-</p>
<p>h, 48, 53</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*82</p>
</blockquote></td>
<td><blockquote>
<p>Updated the option description to include <em>Send Entire Drug File to External Interface</em> [PSS MASTER FILE ALL] option. Added new master file update information to the “HL7 Messaging with an External System” section. Updated routine list to include PSSMSTR. Updated the web address for the VistA Documentation Library (VDL).</p>
</blockquote></td>
</tr>
<tr class="even">
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
<tr class="odd">
<td><blockquote>
<p>04/03</p>
</blockquote></td>
<td><blockquote>
<p>i, 5, 8, 29,</p>
<p>35, 48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*68</p>
</blockquote></td>
<td><blockquote>
<p>Updated patch references to include PSS*1*68. Added NON-VA MED field (#8) to the PHARMACY ORDERABLE ITEM file (#50.7).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/03</p>
</blockquote></td>
<td><blockquote>
<p>i., 5, 8, 24a,</p>
<p>29, 31, 35,</p>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*47</p>
</blockquote></td>
<td><blockquote>
<p>Updated patch references to include PSS*1*47. Added new field OTHER LANGUAGE INSTRUCTIONS (#7.1) to the PHARMACY</p>
<p>ORDERABLE ITEM file (#50.7) list and <em>Other Language Translation Setup</em> option description.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11/02</p>
</blockquote></td>
<td><blockquote>
<p>i, ii 5, (6)</p>
<p>23 - 25, (26)</p>
<p>29-30,(47),</p>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>PSS*1*55</p>
</blockquote></td>
<td><blockquote>
<p>Renumbered front matter starting from this Revision History page. Updated Patch number. Updated Option descriptions to include <em>Drug Text File Report</em> option. Added routine PSSDTR in the Routines section. Added the <em>Drug Text File Report</em> option to the current PDM Menu in the Exported Options section.</p>
</blockquote></td>
</tr>
<tr class="even">
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
<tr class="odd">
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
<tr class="even">
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
> *(This page included for two-sided copying.)*

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PHARMACY ORDERABLE ITEM file (#50.7) must be built prior to the installation of Outpatient Pharmacy V. 7.0 and Inpatient Medications V. 5.0. The PHARMACY ORDERABLE ITEM file (#50.7) will be similar to the PRIMARY DRUG file (#50.3) used by Inpatient Medications V. 4.5. The main difference is that each entry in the PHARMACY ORDERABLE ITEM file (#50.7) has an associated Dosage Form that will always print next to the name. The PHARMACY ORDERABLE ITEM file (#50.7) will be duplicated in the ORDERABLE ITEM file (#101.43) that will reside in CPRS V. 1.0. Any update to the PHARMACY ORDERABLE ITEM file (#50.7) will automatically update the corresponding entry in the ORDERABLE ITEM file (#101.43). The NAME field (#.01) and the DOSAGE FORM field (#.02) values in the PHARMACY ORDERABLE ITEM file (#50.7) will print on Outpatient Pharmacy reports, profiles, Inpatient Medication reports, MAR labels etc., in place of the Primary Drug Name.

> The PHARMACY ORDERABLE ITEM file (#50.7) includes the following fields. These fields reflect the package content up to and including the release of patch PSS\*1\*117.

>  These fields were necessary for the initial installation but were deleted following later patches.

> \* These fields were not exported with the initial installation but were added with later patches.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 40%" />
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
<p><strong>1.1.1.1 NAME</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is the name of the Pharmacy</p>
<p>Orderable Item. It is a free text field that can be up to 40 characters in length.</p>
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
<p>This is a pointer to the DOSAGE FORM file (#50.606). This is a required field and</p>
<p>will always print next to the Pharmacy Orderable Item name.</p>
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
<p>This field will be set to 1 to indicate that the Pharmacy Orderable Item entry is pointed to by either the IV ADDITIVES file (#52.6), or the IV SOLUTIONS file (#52.7). If this field is not set to 1, it</p>
<p>indicates that the entry is pointed to from the DRUG file (#50).</p>
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
<p>This is a free text field used to calculate a default value for the "STOP DATE"</p>
<p>prompt of the order.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>.06</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>DEFAULT MED ROUTE</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a pointer to the MEDICATION ROUTES file (#51.2). If a MED ROUTE</p>
<p>is entered here, it will be used as the default value during order entry when this</p>
<p>drug is selected.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>.07</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>SCHEDULE TYPE</strong></p>
</blockquote></td>
<td><blockquote>
<p>This field is a set of codes and will be used as a default value when selecting this drug</p>
<p>in order entry.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 40%" />
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
<p><strong>.08</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>SCHEDULE</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a free text field and will be used as</p>
<p>a default value during order entry when this drug is selected.</p>
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
<p>This is a set of codes with 1 (one)</p>
<p>indicating that the Orderable Item is a supply.</p>
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
<p>This multiple will contain all the associated synonyms for the Pharmacy</p>
<p>Orderable Item.</p>
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
<p>If CHANGE TYPE OF ORDER FROM</p>
<p>OERR field (#20.412) in the PHARMACY SYSTEM file (#59.7) parameter in Inpatient Mediations package is set, this field will be asked to user. This field will indicate corresponding Orderable Items to choose from and which package (UD or</p>
<p>IV) to finish the order.</p>
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
<p>If CHANGE TYPE OF ORDER FROM</p>
<p>OERR field (#20.412) in the PHARMACY SYSTEM file (#59.7) parameter in Inpatient Mediations package is set, this field will be asked to user. This field will indicate corresponding Orderable Items to choose from and which package (UD or IV) to finish the order.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>*5</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>FORMULARY STATUS</strong></p>
</blockquote></td>
<td><blockquote>
<p>This field will designate the formulary status of the Orderable Item. The non- formulary status will be displayed to the provider next to the selectable list of Orderable Item(s) during CPRS order entry (List Manager and GUI). This field is not editable. The software controls it. An Orderable Item will only be marked as</p>
<p>non-formulary if there are no active Dispense Drugs that are formulary drugs matched to the item.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>*6</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>OI-DRUG TEXT ENTRY (multiple)</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 40%" />
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
<p>The text in this field shall be presented as a default for the Patient Instructions prompt in the Outpatient Pharmacy package when entering orders, if the Dispense Drug selected is matched to this Pharmacy Orderable Item. This text will also be presented during the</p>
<p>Outpatient Medication order entry process through CPRS, and the CPRS user can then determine whether or not these Instructions should be part of the order.</p>
<p>For all words entered in this field, the software will check for expansions for each word in the MEDICATION INSTRUCTION file (#51) and expand the</p>
<p>word accordingly.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>7.1</strong></p>
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
<p>This field indicates whether the Pharmacy Orderable Item is selectable as a Non-VA Med (either an herbal supplement, an over- the-counter (OTC) medication, or a prescription drug not dispensed by the</p>
<p>VA). This field is not editable.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 40%" />
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
<p><strong>9</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>ASSOCIATED IMMUNIZATION</strong></p>
</blockquote></td>
<td><blockquote>
<p>This field is added by the Immunizations Documentation by BCMA application. A mapping relationship is created between the PHARMACY ORDERABLE ITEM</p>
<p>file (#50.7) and the pointed-to immunization so that a record can be created in the V IMMUNIZATION file (#9000010.11) corresponding to the</p>
<p>BCMA administration of an immunization.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>*10</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>USE DOSAGE FORM MED ROUTE LIST</strong></p>
</blockquote></td>
<td><blockquote>
<p>This flag governs the source of the medication routes that will be used during medication order entry. If this field is set to YES, the optional list of med routes will be derived from the Dosage Form file (#50.606) associated to the orderable item. Otherwise, it will be derived from the Possible Med Routes Sub-file (#50.711)</p>
<p>associated to the orderable item.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>*11</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>POSSIBLE MED ROUTES</strong></p>
<p><strong>(multiple)</strong></p>
</blockquote></td>
<td><blockquote>
<p>If the DEFAULT MED ROUTE field (#.06) is populated then that value will be returned as the default value. If the DEFAULT MED ROUTE field (#.06) is</p>
<p>not populated and the POSSIBLE MED ROUTES multiple (#11) is populated with a single entry and the USE DOSAGE FORM MED ROUTE LIST field (#10) is</p>
<p>set to "NO", the single entry will be returned as the default value.</p>
<p>If the DEFAULT MED ROUTE (#.06)</p>
<p>field is not populated and the POSSIBLE MED ROUTES multiple (#11) is populated with more than one entry and the USE DOSAGE FORM MED ROUTE</p>
<p>LIST field (#10) is set to "NO", no value will be returned as the default value.</p>
<p>The med routes selection list in CPRS will be populated with entries in all the medication routes associated with the orderable item's dosage form if the USE DOSAGE FORM MED ROUTE LIST</p>
<p>field (#10) is set to "YES", otherwise from the POSSIBLE MED ROUTES multiple</p>
<p>(#11).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>*11</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.01</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>POSSIBLE MED ROUTES</strong></p>
</blockquote></td>
<td><blockquote>
<p>POINTER TO MEDICATION ROUTES</p>
<p>FILE (#51.2) (Multiply asked)</p>
</blockquote></td>
</tr>
</tbody>
</table>

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
<col style="width: 10%" />
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
<p><strong>UPDATE</strong></p>
<p><strong>DD</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>DATA COMES USER</strong></p>
<p><strong>WITH FILE OVERRIDE</strong></p>
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
<td colspan="2"><blockquote>
<p>DRUG TEXT</p>
</blockquote></td>
<td colspan="3">FULL</td>
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
<td colspan="2"><blockquote>
<p>IV ADDITIVES</p>
</blockquote></td>
<td colspan="3">FULL</td>
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
<td colspan="2"><blockquote>
<p>IV SOLUTIONS</p>
</blockquote></td>
<td colspan="3">FULL</td>
<td></td>
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>54</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>RX CONSULT</p>
</blockquote></td>
<td colspan="3">FULL</td>
<td><blockquote>
<p>(SCREEN)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
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
<tr class="even">
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
<tr class="odd">
<td colspan="4"><blockquote>
<p>59.73 VENDOR DISABLE/ENABLE</p>
</blockquote></td>
<td colspan="2">FULL</td>
<td colspan="4"><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
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

> The following non-PDM files are exported with the PDM package.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File#</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>NAME</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>UPDATE</strong></p>
<p><strong>DD</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DATA COMES</strong></p>
<p><strong>WITH FILE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>USER</strong></p>
<p><strong>OVERRIDE</strong></p>
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

> *(This page included for two-sided copying.)*

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS LOCAL POSSIBLE DOSAGES</strong></p>
<p>MENU TEXT: Local Possible Dosages Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report that displays entries from the LOCAL POSSIBLE DOSAGE (#50.0904) Subfile of the DRUG (#50) File with missing data in DOSE UNIT (#4) Field and the NUMERIC DOSE (#5) Field. This data needs to be populated if Dosage checks are to be performed, when that Local Possible Dosage is selected for an order.</p>
<p>ROUTINE: EN^PSSLDOSE</p>
<p>UPPERCASE MENU TEXT: LOCAL POSSIBLE DOSAGES REPORT</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS STRENGTH MISMATCH</strong></p>
<p>MENU TEXT: Strength Mismatch Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report that shows all entries from the DRUG (#50) File that have data in the STRENGTH (#901) Field that does not match the data in the STRENGTH (#2) Field from the match in the VA PRODUCT (#50.68) File.</p>
<p>ROUTINE: EN^PSSTRENG</p>
<p>UPPERCASE MENU TEXT: STRENGTH MISMATCH REPORT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS DOSE UNIT REQUEST</strong></p>
<p>MENU TEXT: Request Change to Dose Unit TYPE: run routine</p>
<p>DESCRIPTION: This option enables a request to be made to have a new entry added, or a current entry changed in the DOSE UNITS (#51.24) File.</p>
<p>ROUTINE: DOSE^PSSMEDRQ</p>
<p>UPPERCASE MENU TEXT: REQUEST CHANGE TO DOSE UNIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS MARK PREMIX SOLUTIONS</strong></p>
<p>MENU TEXT: Mark PreMix Solutions TYPE: run routine</p>
<p>DESCRIPTION: This option will be used to mark entries from the IV SOLUTIONS (#52.7) File as PreMixes, by allowing editing of the PREMIX (#18) Field.</p>
<p>ROUTINE: EDIT^PSSPRUTL</p>
<p>UPPERCASE MENU TEXT: MARK PREMIX SOLUTIONS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS IV SOLUTION REPORT</strong></p>
<p>MENU TEXT: IV Solution Report TYPE: run routine</p>
<p>DESCRIPTION: This report will display all entries from the IV SOLUTIONS (#52.7) File, or just those entries marked as PreMixes in the PREMIX (#18) Field.</p>
<p>ROUTINE: REP^PSSPRMIX</p>
<p>UPPERCASE MENU TEXT: IV SOLUTION REPORT</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS SCHEDULE REPORT</strong></p>
<p>MENU TEXT: Administration Schedule File Report TYPE: run routine</p>
<p>DESCRIPTION: This option provides a report of entries from the ADMINISTRATION SCHEDULE (#51.1) File that shows whether or not data has been entered in the FREQUENCY (IN MINUTES) (#2) Field for the entries. To perform Dosage checks on medication orders, a frequency must be derived from the Schedule of the order.</p>
<p>ROUTINE: EN^PSSSCHRP</p>
<p>UPPERCASE MENU TEXT: ADMINISTRATION SCHEDULE FILE R</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
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
<col style="width: 32%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
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
<td rowspan="2"><blockquote>
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
<td colspan="3"><blockquote>
<p><strong>NAME: PSS DEF MED ROUTE OI RPT</strong></p>
<p>MENU TEXT: Default Med Route For OI Report TYPE: print</p>
<p>DIC {DIP}: PS(50.7, L.: 0</p>
<p>FLDS: [PSS DEF MED ROUTE FOR OI] BY: [PSS DEF MED ROUTE FOR OI] DHD: [PSS HDR DEF MED ROUTE]</p>
<p>UPPERCASE MENU TEXT: DEFAULT MED ROUTE FOR OI REPOR</p>
</blockquote></td>
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

> The following options were retrieved from VA FileMan and reflect the new options added to PDM following the installation of patch PSS\*1\*136 and PSS\*1\*117.

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>NAME: PSS PEPS SERVICES</strong> MENU TEXT: PEPS Services</p>
<p>TYPE: menu</p>
<p>PACKAGE: PHARMACY DATA MANAGEMENT</p>
<p>ITEM: PSS CHECK VENDOR DATABASE LINK DISPLAY ORDER: 1 ITEM: PSS CHECK PEPS SERVICES SETUP DISPLAY ORDER: 2 ITEM: PSS SCHEDULE PEPS INTERFACE CK DISPLAY ORDER: 3</p>
<p>UPPERCASE MENU TEXT: PEPS SERVICES</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS CHECK PEPS SERVICES SETUP</strong> MENU TEXT: Check PEPS Services Setup</p>
<p><strong>TYPE: run routine</strong></p>
<p>PACKAGE: PHARMACY DATA MANAGEMENT</p>
<p>DESCRIPTION: This option provides the ability to check and validate that the link to the vendor interface used for enhanced order checking is enabled and operational. It also provides the ability to execute various order checks against the vendor database to ensure that the database is installed and reachable.</p>
<p>ROUTINE: RUNTEST^PSSHRIT</p>
<p>UPPERCASE MENU TEXT: CHECK PEPS SERVICES SETUP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>NAME: PSS CHECK VENDOR DATABASE LINK</strong> MENU TEXT: Check Vendor</p>
<p>TYPE: run routine</p>
<p>PACKAGE: PHARMACY DATA MANAGEMENT ROUTINE: INTACT^PSSHRIT UPPERCASE MENU TEXT: CHECK VENDOR DATABASE LINK</p>
</blockquote></td>
<td>Database Link</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS SCHEDULE PEPS INTERFACE CK</strong></p>
<p>MENU TEXT: Schedule/Reschedule Check PEPS Interface</p>
<p>TYPE: run routine PACKAGE: PHARMACY DATA MANAGEMENT</p>
<p>DESCRIPTION: This option allows you to schedule the Interface Scheduler [PSS INTERFACE SCHEDULER] option, which tests the PEPS interface by sending a PING request. If the PEPS Interface is not available, a mail message will be sent to the G.PSS ORDER CHECKS mail group.</p>
<p>ROUTINE: SCHDOPT^PSSHRIT TIMESTAMP: 61493,49257 UPPERCASE MENU TEXT: SCHEDULE/RESCHEDULE CHECK PEPS</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>NAME: PSS ENABLE/DISABLE DB LINK</strong></p>
<p>MENU TEXT: Enable/Disable Vendor Database Link TYPE: run routine</p>
<p>PACKAGE: PHARMACY DATA MANAGEMENT</p>
<p>DESCRIPTION: This option provides the ability to disable/enable the link to the vendor interface used for enhanced order checking. When disabled, NO drug-drug interaction, duplicate therapy or dosing order checks will</p>
<p>be performed in Pharmacy and in Computerized Patient Record System (CPRS). ROUTINE: EN^PSSDSFDB</p>
<p>UPPERCASE MENU TEXT: ENABLE/DISABLE VENDOR DATABASE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> After installing PSS\*1\*117, your current PSS MGR menu will look as shown below. See section 2.7.1 for information regarding stand-alone options that are not part of the current PSS MGR menu.

> Pharmacy Data Management \[PSS MGR\]

> CMOP Mark/Unmark (Single drug) \[PSSXX MARK\] ![](pss-1-117-136-technical-manual-security-guide-change-pages/002.png)

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

> \[PSS ORDERABLE ITEM MANAGEMENT\]

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

IV Solution Report

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

> *\<This page left blank for two-sided copying.\>*

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
<p>PSS117EN</p>
</blockquote></th>
<th><blockquote>
<p>PSS117PO</p>
</blockquote></th>
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
</tr>
</thead>
<tbody>
<tr class="odd">
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
<td><blockquote>
<p>PSS50ATC</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>PSS50CMP</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<td><blockquote>
<p>PSS350F1</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>PSS50P7A</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<td><blockquote>
<p>PSS51P1A</p>
</blockquote></td>
</tr>
<tr class="even">
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
<p>PSS52P6</p>
</blockquote></td>
<td><blockquote>
<p>PSS52P6A</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<td><blockquote>
<p>PSS551</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSS55MIS</p>
</blockquote></td>
<td><blockquote>
<p>PSS59P7</p>
</blockquote></td>
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
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSCHENV</p>
</blockquote></td>
<td><blockquote>
<p>PSSCHPRE</p>
</blockquote></td>
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
</tr>
<tr class="even">
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
<p>PSSDAWUT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDDUT</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<td><blockquote>
<p>PSSDELOI</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>PSSDOS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSDOSCR</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSCX</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSED</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSER</p>
</blockquote></td>
<td><blockquote>
<p>PSSDOSRP</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSAPA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSDSAPD</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSAPI</p>
</blockquote></td>
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
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSDSBDA</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSBDB</p>
</blockquote></td>
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
</tr>
<tr class="even">
<td><blockquote>
<p>PSSDSDAT</p>
</blockquote></td>
<td><blockquote>
<p>PSSDSFDB</p>
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
<p>PSSDSEXC</p>
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
<p>PSSFDBRT</p>
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
</tr>
<tr class="even">
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
<p>PSSGSH</p>
</blockquote></td>
<td><blockquote>
<p>PSSHELP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSHFREQ</p>
</blockquote></td>
<td><blockquote>
<p>PSSHLSCH</p>
</blockquote></td>
<td><blockquote>
<p>PSSHLU</p>
</blockquote></td>
<td><blockquote>
<p>PSSHL1</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRCOM</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRENV</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>PSSHRQ21</p>
</blockquote></td>
<td><blockquote>
<p>PSSHRQ22</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<td><blockquote>
<p>PSSHTTP</p>
</blockquote></td>
<td><blockquote>
<p>PSSJEEU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSJORDF</p>
</blockquote></td>
<td><blockquote>
<p>PSSJSPU</p>
</blockquote></td>
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
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSJXR1</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR10</p>
</blockquote></td>
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
</tr>
<tr class="even">
<td><blockquote>
<p>PSSJXR15</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR16</p>
</blockquote></td>
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
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSJXR20</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR21</p>
</blockquote></td>
<td><blockquote>
<p>PSSJXR22</p>
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
</tr>
<tr class="even">
<td><blockquote>
<p>PSSJXR7</p>
</blockquote></td>
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
<p>PSSLDALL</p>
</blockquote></td>
<td><blockquote>
<p>PSSLDEDT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSLDOSE</p>
</blockquote></td>
<td><blockquote>
<p>PSSLDOSE</p>
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
</tr>
<tr class="even">
<td><blockquote>
<p>PSSMEDRQ</p>
</blockquote></td>
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
<p>PSSMRTUP</p>
</blockquote></td>
<td><blockquote>
<p>PSSMRTUX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSMSTR</p>
</blockquote></td>
<td><blockquote>
<p>PSSNDCUT</p>
</blockquote></td>
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
</tr>
<tr class="even">
<td><blockquote>
<p>PSSOPKI</p>
</blockquote></td>
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
<p>PSSORUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSSOUTSC</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<td><blockquote>
<p>PSSPOIC</p>
</blockquote></td>
</tr>
<tr class="even">
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
<td><blockquote>
<p>PSSPOIM</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<td><blockquote>
<p>PSSPOST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSPOST1</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOST2</p>
</blockquote></td>
<td><blockquote>
<p>PSSPOST5</p>
</blockquote></td>
<td><blockquote>
<p>PSSPRE</p>
</blockquote></td>
<td><blockquote>
<p>PSSPRETR</p>
</blockquote></td>
<td><blockquote>
<p>PSSPRMIX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSPRUTL</p>
</blockquote></td>
<td><blockquote>
<p>PSSQORD</p>
</blockquote></td>
<td><blockquote>
<p>PSSREF</p>
</blockquote></td>
<td><blockquote>
<p>PSSREMCH</p>
</blockquote></td>
<td><blockquote>
<p>PSSSCHED</p>
</blockquote></td>
<td><blockquote>
<p>PSSSCHRP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSSSOLI1</p>
</blockquote></td>
<td><blockquote>
<p>PSSSOLIT</p>
</blockquote></td>
<td><blockquote>
<p>PSSSPD</p>
</blockquote></td>
<td><blockquote>
<p>PSSSUTIL</p>
</blockquote></td>
<td><blockquote>
<p>PSSSYN</p>
</blockquote></td>
<td><blockquote>
<p>PSSTRENG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSSUTIL</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTLA1</p>
</blockquote></td>
<td><blockquote>
<p>PSSUTLPR</p>
</blockquote></td>
<td><blockquote>
<p>PSSVIDRG</p>
</blockquote></td>
<td><blockquote>
<p>PSSVX6</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> *\<This page left blank for two-sided copying.\>*

### Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Stand-Alone Options

> All of the PDM options are designed to stand alone and can be accessed without first accessing the top- level menu.

> The following stand-alone menus are not part of the PSS MGR main menu. They can be added to the main menu to provide a customized menu. They are accessible to whomever is designated to access KERNEL options to customize a menu.

> Other Language Translation Setup \[PSS OTHER LANGUAGE SETUP\]

> Dispense Drug Fields \[PSSJU DRG\]

> Dispense Drug/ATC Set Up \[PSSJU DRUG/ATC SET UP\]

> Drug Inquiry (IV)

> \[PSSJI DRUG INQUIRY\]

> Edit Cost Data \[PSSJU DCC\]

> EDit Drug Cost (IV)

> \[PSSJI EDIT DRUG COST\]

> Electrolyte File (IV)

> \[PSSJI ELECTROLYTE FILE\]

> MARk/Unmark Dispense Drugs For Unit Dose \[PSSJU MARK UD ITEMS\]

> PRimary Solution File (IV) \[PSSJI SOLN\]

> And last but not least, below is a stand-alone option that exists ONLY as a way for technical personnel to turn on/off the database connection *if required* for debugging. Normally it is enabled and the Vendor Database updates are performed centrally in Austin and Martinsburg, not at the individual sites. This option is rarely used. It is NOT exported as part of the main PDM menu \[PSS MGR\]:

> Enable/Disable Vendor Database Link \[PSS ENABLE/DISABLE DB LINK\]

> *\<This page left blank for two-sided copying.\>*

#### Menus

> The original PDM menu that would be seen following the initial setup of the PDM package is displayed below. The options needed to build and maintain the PHARMACY ORDERABLE ITEM file (#50.7) will be under the Pharmacy Data Management menu, and will appear as follows.

> Pharmacy Data Management \[PSS MGR\]

> Primary/VA Generic Orderable Item Report \[PSS PRIMARY/VA GENERIC REPORT\]

> VA Generic Orderable Item Report

> \[PSS VA GENERIC DRUG REPORT\]

> Create Pharmacy Orderable Items

> \[PSS CREATE ORDERABLE ITEMS\]

> Manually Match Dispense Drugs

> \[PSS PRE-RELEASE MANUAL MATCH\]

> Orderable Item Matching Status

> \[PSS ORDERABLE ITEM STATUS\]

> CMOP Mark/Unmark (Single drug) ![](pss-1-117-136-technical-manual-security-guide-change-pages/003.png) \[PSSXX MARK\]

> Drug Enter/Edit

> \[PSS DRUG ENTER/EDIT\]

> Drug Interaction Management...

> \[PSS DRG INTER MANAGEMENT\]

> Enter/Edit Local Drug Interaction

> \[PSS INTERACTION LOCAL ADD\]

> Edit Drug Interaction Severity

> \[PSS INTERACTION SEVERITY\]

> Electrolyte File (IV)

> \[PSSJI ELECTROLYTE FILE\]

> Lookup into Dispense Drug File \[PSS LOOK\]

> Med. Route/Instructions Table Maintenance \[PSS MED. ROUTE/INSTRUCTIONS\]

> Medication Instruction File Add/Edit \[PSSJU MI\]

> Orderable Item Management...

> \[PSS ORDERABLE ITEM MANAGEMENT\]

> Edit Orderable Items

> \[PSS EDIT ORDERABLE ITEMS\]

> Dispense Drug/Orderable Item Maintenance

> \[PSS MAINTAIN ORDERABLE ITEMS\]

> Additive/Solutions, Orderable Items \[PSS ADDITIVE/SOLUTIONS\]

> Orderable Item Report

> \[PSS ORDERABLE ITEM REPORT\]

> Primary Drug Edit

> \[PSS PRIMARY DRUG EDIT\]

> Pharmacy System Parameters Edit \[PSS SYS EDIT\]

> Standard Schedule Edit

> \[PSS SCHEDULE EDIT\]

> ![](pss-1-117-136-technical-manual-security-guide-change-pages/004.png)Locked: PSXCMOPMGR

> Without the PSXCMOPMGR key, the *CMOP Mark/Unmark (Single drug)* option will not appear on your menu.

> The PDM menu that was exported with the original PDM package has been modified to include subsequent changes and patches.

> The PDM menu up to and including PSS\*1\*117 appears below. PSS\*1\*117 was the last patch to affect a change to the PDM menu.

> Pharmacy Data Management \[PSS MGR\]

> CMOP Mark/Unmark (Single drug) \[PSSXX MARK\] ![](pss-1-117-136-technical-manual-security-guide-change-pages/005.png)

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

> \[PSS ORDERABLE ITEM MANAGEMENT\]

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

IV Solution Report

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

### Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: PSS EXT MFU CLIENT

> DESCRIPTION: This protocol will be used as the ACK from the external interface for a MFN_M01 message.

> NAME: PSS EXT MFU SERVER

> DESCRIPTION: This protocol will be used to send even notification and data when new drugs are added to the DRUG file (#50) and when certain fields are updated in the same file. This information will be sent to the automated dispensing machines through HL7 V.2.4 formatted messages.

> NAME: PSS HUI DRUG UPDATE

> DESCRIPTION: This protocol will be used to send event notification and data when new drugs are added to the Drug file (#50) and when certain fields are updated in same file.

> NAME: PSS MED ROUTE RECEIVE

> DESCRIPTION: This protocol processes updates to the Standard Medication Routes (#51.23) File.

### Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: PSS FDB INTERFACE

> SUBJECT: ORDER CHECK DATABASE DOWN RETENTION DAYS: 3

> PRIORITY?: YES

> NAME: PSS FDB INTERFACE RESTORED SUBJECT: ORDER CHECK DATABASE IS BACK UP RETENTION DAYS: 3

> PRIORITY?: YES

### HL7 Messaging with an External System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Protocol

> A new protocol, PSS HUI DRUG UPDATE, is exported and has been created to generate HL7 messages when new drugs are added to the DRUG file (#50) and existing entries are updated. This protocol is exported with the text “DELETE ONLY TO SEND DRUG UPDATE MESSAGES” in the DISABLE field (#2) of the PROTOCOL file (#101). To activate the sending of these HL7 messages, the text from the DISABLE field (#2) of the PROTOCOL file (#101) must be deleted and at least one receiving protocol added as a subscriber. The drug data elements included in the HL7 message are defined in the table below.

#### HL7 Drug Message Segment Definition Table

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
<p>If “1” true</p>
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
<p>DEA SPECIAL HDLG</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>How drug is dispense based on DEA codes</p>
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
<p>If ‘1’ true</p>
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

### Package Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The initial PDM module relies on, at least, the following external packages to run effectively.

#### Package Minimum version needed

> National Drug File V. 3.15

> Outpatient Pharmacy V. 6.0

> Inpatient Medications V. 4.5

> Kernel V. 8.0 (plus all patches, particularly XU\*8\*28)

> VA FileMan V. 21.0 (plus all patches)

> The PDM module up to and including the release of PSS\*1\*68 relies on, at least, the following external packages to run effectively.

#### Package Minimum version needed

> National Drug File V. 4.0

> Outpatient Pharmacy V. 7.0

> Inpatient Medications V. 5.0

> Kernel V. 8.0

> VA FileMan V. 22.0

> The PDM module up to and including the release of PSS\*1\*136 relies on, at least, the following external packages to run effectively:

#### Package Minimum version needed

> HealtheVet Web Services Client (HWSC) V. 1.0 VistaLink V. 1.6

> *(This page included for two-sided copying.)*

# Security Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *(This page included for two-sided copying.)*

### Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PDM package does not contain any VA FileMan security codes except for programmer security (@) on the data dictionaries for the PDM files. Security with respect to standard options in the module is implemented by carefully assigning options to users and by the use of security keys.

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PSS\*1\*147 creates a new mail group called PSS ORDER CHECKS. The mail group description below was retrieved from VA FileMan. The IRM Pharmacy support and Pharmacy ADPACs (and backups) should at a minimum be added to this mail group.

### Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no alerts in the PDM package.

### Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Bulletins are 'Super' messages. Each Bulletin has a text and a subject just like a normal message. But embedded within either the subject or the text can be variable fields that can be filled in with parameters. There is also a standard set of recipients in the form of a Mail Group that is associated with the bulletin.

> Bulletins are processed by MailMan either because of either a special type of cross reference or a direct call in a routine. The interface for the direct call is described in the documentation on programmer entry points. FileMan sets up code that will issue a bulletin automatically when the special cross reference type is created. In either case the parameters that go into the text and/or the subject make each bulletin unique.

> NAME: PSS FDB INTERFACE

> SUBJECT: ORDER CHECK DATABASE DOWN RETENTION DAYS: 3

> PRIORITY?: YES

> NAME: PSS FDB INTERFACE RESTORED SUBJECT: ORDER CHECK DATABASE IS BACK UP RETENTION DAYS: 3

> PRIORITY?: YES

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PDM does not transmit data to any remote system or facility.

### Archiving/Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no archiving and purging functions necessary with the PDM package.

### Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites utilizing the PDM package should develop a local contingency plan to be used in the event of product problems in a live environment. The facility contingency plan must identify the procedure for maintaining functionality provided by this package in the event of system outage. Field station Information Security Officers (ISOs) may obtain assistance from their Regional Information Security Officer (RISO).

### Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no specialized products embedded within or required by the PDM package.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No electronic signatures are utilized in the PDM package.

### Menus

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

> \* These items are for pre-release only and will be deleted with the installation of subsequent Pharmacy Data Management patches.

> The PDM menu up to and including the release of PSS\*1\*136 and PSS\*1\*117 appears below. PSS\*1\*136 and PSS\*1\*117 were the last patches to affect a change to the PDM menu.

> ![](pss-1-117-136-technical-manual-security-guide-change-pages/006.png)*CMOP Mark/Unmark (Single drug) Dosages ...*

> *Auto Create Dosages Dosage Form File Enter/Edit Enter/Edit Dosages*

> *Most Common Dosages Report Noun/Dosage Form Report Review Dosages Report*

> *Local Possible Dosages Report Request Change to Dose Unit*

> *Drug Enter/Edit*

> *Order Check Management ...*

> *Request Changes to Enhanced Order Check Database Report of Locally Entered Interactions*

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

> *Controlled Substances/PKI Reports*

> *DEA Spec Hdlg & CS Fed Sch Discrepancy Controlled Substances Not Matched to NDF CS (DRUGS) Inconsistent with DEA Spec Hdlg*

> *CS (Ord. Item) Inconsistent with DEA Spec Hdlg Send Entire Drug File to External Interface*

> *IV Additive/Solution IV Additive Report IV Solution Report*

> *Mark PreMix Solutions Warning Builder*

> *Warning Mapping PEPS Services*

> *Check Vendor Database Link Check PEPS Services Setup*

> *Schedule/Reschedule Check PEPS Interface*

> ![](pss-1-117-136-technical-manual-security-guide-change-pages/007.png) Locked: PSXCMOPMGR

> Without the PSXCMOPMGR key, the *CMOP Mark/Unmark (Single drug)* option will not appear on your menu.

![](pss-1-117-136-technical-manual-security-guide-change-pages/008.png)

![](pss-1-117-136-technical-manual-security-guide-change-pages/009.png)

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to mark or edit package specific fields in a DRUG file (#50) entry, the user must hold the corresponding package key. The keys are assigned for the individual packages. PDM does not export any of these keys.

#### Package Keys

> Outpatient Pharmacy PSORPH

> Inpatient Medications PSJU MGR

> Inpatient Medications PSJI MGR

> Automatic Replenishment/Ward Stock PSGWMGR

> Drug Accountability/Inventory Interface PSAMGR Drug Accountability/Inventory Interface PSA ORDERS Controlled Substances PSDMGR

> National Drug File PSNMGR

> Consolidated Mail Outpatient Pharmacy PSXCMOPMGR

> Patch PSS\*1\*147 exports the following four security keys, that will be used by the Pharmacy Enterprise Customization System (PECS) application. Only a few users who will be granted access to the PECS application will need one or more keys assigned based on their role.

> Assignment of these keys should be by request only. The security key descriptions were retrieved from VA FileMan.

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Information about all files, including these, can be obtained by using the VA FileMan to generate a list of file attributes.

#### PDM Files

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
<tr class="odd">
<td colspan="7"><blockquote>
<p>59.73 VENDOR DISABLE/ENABLE @ @ @ @ @</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>59.74 VENDOR INTERFACE DATA @ @ @ @ @</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Non-PDM Files

<table>
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

![](pss-1-117-136-technical-manual-security-guide-change-pages/010.png)

> <span id="_TOC_250000" class="anchor"></span>Glossary

> Administration Schedule File The ADMINISTRATION SCHEDULE file (#51.1)

> contains administration schedule names and standard dosage administration times. The name is a common abbreviation for an administration schedule (e.g., QID, Q4H, PRN). The administration time is entered in military time.

> CPRS A VistA computer software package called Computerized Patient Record System. CPRS is an application in VistA that allows the user to enter all necessary orders for a patient in different packages from a single application.

> DATUP Functionality that allows the Pharmacy Enterprise Customization System (PECS) to send out custom and standard commercial-off-the-shelf (COTS) vendor database changes to update the two centralized databases at Austin and Martinsburg.

> Dispense Drug The Dispense Drug is pulled from DRUG file (#50) and usually has the strength attached to it (e.g., Acetaminophen 325 mg). Usually, the name alone without a strength attached is the Pharmacy Orderable Item name.

> Dosage Form File The DOSAGE FORM file (#50.606) contains all dosage forms and associated data that are used by Pharmacy packages and CPRS. The dosage form is used in SIG construction, default values and in the determination of the type of each dosage created for each application.

> Dose Unit File The DOSE UNIT file (#51.24) was created to accomplish the mapping to First Data Bank (FDB). All entries in this file have been mapped to an FDB Dose Unit. Although this file has not yet been standardized by Standards and Terminology Services (SRS), no local editing will be allowed. When populating the Dose Unit field for a Local Possible Dosage, selection will be from this new file.

> Drug Electrolytes File The DRUG ELECTROLYTES file (#50.4) contains the

> names of anions/cations, and their cations and concentration units.

> Drug File The DRUG file (#50) holds the information related to each drug that can be used to fill a prescription or medication order. It is pointed to from several other files and should be handled carefully, usually only by special individuals in the Pharmacy Service. Entries are not typically deleted, but rather made inactive by entering an inactive date.

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

> MOCHA Medication Order Check Healthcare Application.

> National Drug File The National Drug File provides standardization of the local drug files in all VA medical facilities.

> Standardization includes the adoption of new drug nomenclature and drug classification and links the local drug file entries to data in the National Drug File. For drugs approved by the Food and Drug Administration (FDA), VA medical facilities have access to information concerning dosage form, strength and unit; package size and type; manufacturer’s trade name; and National Drug Code (NDC). The NDF software lays the foundation for sharing prescription information among medical facilities.

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

> Standard Medication Route File The STANDARD MEDICATION ROUTE file

> (#51.23) was created to map Local Medication Routes in VistA to an FDB Route in order to perform dosage checks in PRE V.0.5. This file has been standardized by Standards and Terminology Service (STS) and is mapped to an FDB Route. It cannot be edited locally.

> Standard Schedule Standard medication administration schedules are stored in the ADMINISTRATION SCHEDULE file (#51.1).

> Units Per Dose The Units Per Dose is the number of Units (tablets, capsules, etc.) to be dispensed as a dose for an order. Fractional numbers will be accepted.

> VA Drug Class Code A drug classification system used by VA that separates

> drugs into different categories based upon their characteristics. Some cost reports can be run for VA Drug Class Codes.

> VA Product File The VA PRODUCT file (#50.68) contains a list of available drug products.

> *(This page included for two-sided copying.)*