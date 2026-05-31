---
title: PSU*4*19 Technical Manual/Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: null
app_code: PSU
app_name: 'Pharmacy: Benefits Management'
section: CLI
app_status: active
pkg_ns: PSU
patch_ver: 4
patch_id: PSU*4*19
group_key: PSU:PSU:4
file_numbers:
- '2'
- '60'
security_keys: []
menu_options: 0
description: '> Department of Veterans Affairs Office of Information and Technology'
audience: Technical staff, IRM, system administrators
keywords: []
page_count: 0
word_count: 607
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: July 2014
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_p19_tm_cp.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_p19_tm_cp.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=91
audit_applied: '2026-05-31'
master_source: PSU*4*19 Technical Manual/Security Guide Change Pages
master_pub_date: July 2014
consolidated_from: 2 versions
prior_versions:
- PSU*4*20 Technical Manual/Security Guide Change Pages
consolidated_title: technical manual/security guide change pages
---

![](psu-4-19-technical-manual-security-guide-change-pages/001.png)

> Software Version 4.0

> Revised July 2014

> June 2005

> Department of Veterans Affairs Office of Information and Technology (OIT)

> Product Development

# Revision History 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [External Relations](#external-relations)
> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>7/2014</p>
</blockquote></td>
<td>i, 18</td>
<td><blockquote>
<p>PSU*4*19</p>
</blockquote></td>
<td><blockquote>
<p>Added new API $$CSI^ICDEX() to Section 8.1, Integration Agreements (IAs).</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/2012</p>
</blockquote></td>
<td>19</td>
<td><blockquote>
<p>PSU*4*20</p>
</blockquote></td>
<td><blockquote>
<p>Updated only the Callable Routines section on this page.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>02/2006</p>
</blockquote></td>
<td><blockquote>
<p>iii,</p>
<p>5, 9, 11,</p>
<p>15,</p>
<p>17-19,</p>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>PSU*4*3</p>
</blockquote></td>
<td><blockquote>
<p>PBM Extract Enhancements #3 project. Updated Table of Contents. Added PBM Health Level 7 (HL7) Chemistry Lab messaging functionality to applicable sections.</p>
<p>Added routines PSULRHL1, PSULRHL2, and PSULRHL3 to Routines section. Added references to HLO package to External Relations and Internal Relations sections. Added list of DBIA's to Section 8.1, Integration Agreements.</p>
<p>Added new Glossary entries for CMOP-NAT, HL7, and HLO. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>06/2005</p>
</blockquote></td>
<td>All</td>
<td></td>
<td><blockquote>
<p>Original Released PBM V. 4.0 Technical Manual</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>
> July 2014 Pharmacy Benefits Management V. 4.0 i Technical Manual / Security Guide
> PSU\*4\*19
> *(This page included for two-sided copying.)*
> ii Pharmacy Benefits Management V. 4.0 June 2005 Technical Manual / Security Guide

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PBM V. 4.0 relies (minimum) on the following external packages. This software is not included in this package and must be installed before this version of PBM is completely functional.

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Minimum Version Needed</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Adverse Reaction Tracking (ART)</td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Auto Replenishment/Ward Stock (AR/WS)</td>
<td><blockquote>
<p>2.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Controlled Substances (CS)</td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Drug Accountability</td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HLO (Health Level 7 Optimized)</td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Inpatient Medications</td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Integrated Funds Control, Accounting and Procurement (IFCAP)</td>
<td><blockquote>
<p>5.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Kernel</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Laboratory</td>
<td><blockquote>
<p>5.2</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MailMan</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>National Drug File (NDF)</td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Outpatient Pharmacy</td>
<td><blockquote>
<p>7.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Patient Care Encounter (PCE)</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Patient Information Management System (PIMS)</td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Pharmacy Data Management (PDM)</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td><blockquote>
<p>22.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Visit Tracking</td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Verified Chemistry Lab results are pushed, rather than extracted, to PBM.

> Verified Chemistry Lab results trigger the creation of an HL7 message containing data from the lab. These messages are sent to the CMOP-NAT sever, where a PBM process loads the data into flat files for export to an SQL database.

> June 2005 Pharmacy Benefits Management V. 4.0 17

> Technical Manual / Security Guide

1.  Integration Agreements (IAs)

> DBIA 3565 to subscribe to the LR7O ALL EVSEND RESULTS protocol DBIA 998 to step through ^DPT(i,"LR" go get the IEN to file \#63

> DBIA 91-A to step through ^LAB(60 to get the name of the test DBIA 3630 to call the HL7 PID builder

> DBIA 4727 to call EN^HLOCNRT

> DBIA 3646 to call API: \$\$EMPL^DGSEC4 DBIA 4658 to call API: \$\$TSTRES^LRRPU DBIA 5747 to call API: \$\$CSI^ICDEX()

> PSU\*4\*3 has Integration Agreements (IAs) with the packages listed above. <span class="mark">REDACTED</span>

> 18 Pharmacy Benefits Management V. 4.0 July 2014 Technical Manual / Security Guide

> PSU\*4\*19