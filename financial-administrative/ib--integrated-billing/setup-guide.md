---
title: Integrated Billing Version 2 Package Security Guide
doc_type: SG
doc_label: Security Guide
doc_layer: anchor
doc_subject: Package
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: - [General Security](#general-security) - [Legal Requirements](#legal-requirements) - [VA FileMan Access Codes](#va-fileman-access-codes) 1. Integrated Billing files may only be updated through distributed options. 2. Per VHA Directive 10-93-142 regarding security of software that affects financial
audience: 
keywords: 
  - blockquote
  - class
  - even
  - style
  - width
  - claims
  - table
  - access
  - billing
  - tracking
page_count: 0
word_count: 3268
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib20sg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib20sg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

> Department of Veterans Affairs Decentralized Hospital Computer Program

INTEGRATED BILLING PACKAGE SECURITY GUIDE

> Version 2.0 March 1994

> Information Systems Center Albany, New York

# General Security


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [General Security](#general-security)
- [Legal Requirements](#legal-requirements)
- [VA FileMan Access Codes](#va-fileman-access-codes)
1.  Integrated Billing files may only be updated through distributed options.
2.  Per VHA Directive 10-93-142 regarding security of software that affects financial systems, most of the IB routines may not be modified. The third line of routines that may not be modified will be so noted. The following routines are exempt from this requirement.
> IBD\* - Encounter Form Utilities
> IBO\*, IBCO\*, IBTO\* - Non-critical Reports
> According to the same directive, most of the IB Data Dictionaries may not be modified. The file descriptions of these files will be so noted. The files which may be modified are Encounter Form files \#357 through \#358.91.
<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Security Keys</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>IB AUTHORIZE</p>
</blockquote></td>
<td><blockquote>
<p>Holding this key allows the user to authorize</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>charges prior to sending to Accounts Receivable.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IB CLAIMS SUPERVISOR</p>
</blockquote></td>
<td><blockquote>
<p>This key should only be given to those individuals</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>who may perform supervisory Claims Tracking</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>functions, such as deleting reviews and Claims</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Tracking entries.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IB EDIT</p>
</blockquote></td>
<td><blockquote>
<p>Holding this key allows a user to create and edit</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>claims for reimbursement.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IB INSURANCE</p>
</blockquote></td>
<td><blockquote>
<p>This key should only be given to those individuals</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SUPERVISOR</p>
</blockquote></td>
<td><blockquote>
<p>who may perform supervisory insurance functions,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>such as deleting insurance companies, deleting</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>policies, and inactivating and merging insurance</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>information.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IB SUPERVISOR</p>
</blockquote></td>
<td><blockquote>
<p>Holding this key allows a user to access manage­</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ment reports and options that control billing.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IBDF IRM</p>
</blockquote></td>
<td><blockquote>
<p>This key is used to prevent access to Encounter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Form Utility options that are for IRM staff only.</p>
</blockquote></td>
</tr>
</tbody>
</table>
> XUMGR This key should be assigned to Kernel site management staff in IRM. It is required in IB to execute archive/purge options.

# Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An electronic signature code is required for users of the Manually Change Copay Exemption (Hardships) option under the Medication Copay Income Exemption Menu, and the Purge Update File and Archive Billing Data options under the Purge Menu.

# VA FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of recommended VA FileMan access codes associated with each file contained in the Integrated Billing package.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 39%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>File</p>
</blockquote></th>
<th>File</th>
<th><blockquote>
<p>DD</p>
</blockquote></th>
<th>RD</th>
<th>WR</th>
<th>DEL</th>
<th>LAYGO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><u>Number</u></p>
</blockquote></td>
<td><u>Name</u></td>
<td><blockquote>
<p><u>Access</u></p>
</blockquote></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
</tr>
<tr class="even">
<td><blockquote>
<p>36</p>
</blockquote></td>
<td>INSURANCE COMPANY</td>
<td><blockquote>
<p>#</p>
</blockquote></td>
<td></td>
<td>D</td>
<td>d</td>
<td>d</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>350</p>
</blockquote></td>
<td>INTEGRATED BILLING ACTION</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>350.1</p>
</blockquote></td>
<td>IB ACTION TYPE</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>350.2</p>
</blockquote></td>
<td>IB ACTION CHARGE</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>350.21</p>
</blockquote></td>
<td>IB ACTION STATUS</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>350.3</p>
</blockquote></td>
<td>IB CHARGE REMOVE REASONS</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>350.4</p>
</blockquote></td>
<td>BILLABLE AMBULATORY SURGICAL</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>CODE</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>350.41</p>
</blockquote></td>
<td>UPDATE BILLABLE AMBULATORY</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>SURGICAL CODE</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>350.5</p>
</blockquote></td>
<td>BASC LOCALITY MODIFIER</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>350.6</p>
</blockquote></td>
<td>IB ARCHIVE/PURGE LOG</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>350.7</p>
</blockquote></td>
<td>AMBULATORY CHECK-OFF SHEET</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>350.71</p>
</blockquote></td>
<td>AMBULATORY SURG. CHECK-OFF</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>SHEET PRINT FIELDS</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>350.8</p>
</blockquote></td>
<td>IB ERROR</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>350.9</p>
</blockquote></td>
<td>IB SITE PARAMETERS</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>351</p>
</blockquote></td>
<td>CATEGORY C BILLING CLOCK</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>351.1</p>
</blockquote></td>
<td>IB CONTINUOUS PATIENT</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>351.2</p>
</blockquote></td>
<td>SPECIAL INPATIENT BILLING CASES</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>352.1</p>
</blockquote></td>
<td>BILLABLE APPOINTMENT TYPE</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>352.2</p>
</blockquote></td>
<td>NON-BILLABLE DISPOSITIONS</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>352.3</p>
</blockquote></td>
<td>NON-BILLABLE CLINIC STOP CODES</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>352.4</p>
</blockquote></td>
<td>NON-BILLABLE CLINICS</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>353</p>
</blockquote></td>
<td>BILL FORM TYPE</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>353.1</p>
</blockquote></td>
<td>PLACE OF SERVICE</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>353.2</p>
</blockquote></td>
<td>TYPE OF SERVICE</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>354</p>
</blockquote></td>
<td>BILLING PATIENT</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>354.1</p>
</blockquote></td>
<td>BILLING EXEMPTIONS</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>354.2</p>
</blockquote></td>
<td>EXEMPTION REASON</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>354.3</p>
</blockquote></td>
<td>BILLING THRESHOLDS</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>354.4</p>
</blockquote></td>
<td>BILLING ALERTS</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>354.5</p>
</blockquote></td>
<td>BILLING ALERT DEFINITION</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>354.6</p>
</blockquote></td>
<td>IB FORM LETTER</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 43%" />
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>355.1</p>
</blockquote></th>
<th><blockquote>
<p>TYPE OF PLAN</p>
</blockquote></th>
<th><blockquote>
<p>@</p>
</blockquote></th>
<th>@</th>
<th>@</th>
<th>@</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>355.2</p>
</blockquote></td>
<td><blockquote>
<p>TYPE OF INSURANCE COVERAGE</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>355.3</p>
</blockquote></td>
<td><blockquote>
<p>GROUP INSURANCE PLAN</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>355.4</p>
</blockquote></td>
<td><blockquote>
<p>ANNUAL BENEFITS</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>355.5</p>
</blockquote></td>
<td><blockquote>
<p>INSURANCE CLAIMS YEAR TO DATE</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 39%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7">National Package Security</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><blockquote>
<p><strong>VA FileMan Access Codes, cont.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>File</p>
</blockquote></td>
<td>File</td>
<td>DD</td>
<td>RD</td>
<td>WR</td>
<td>DEL</td>
<td>LAYGO</td>
</tr>
<tr class="odd">
<td><blockquote>
<p><u>Number</u></p>
</blockquote></td>
<td><u>Name</u></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
</tr>
<tr class="even">
<td><blockquote>
<p>355.6</p>
</blockquote></td>
<td>INSURANCE RIDERS</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>355.7</p>
</blockquote></td>
<td>PERSONAL POLICY RIDERS</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>356</p>
</blockquote></td>
<td>CLAIMS TRACKING</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>356.1</p>
</blockquote></td>
<td>HOSPITAL REVIEW</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>356.11</p>
</blockquote></td>
<td>CLAIMS TRACKING REVIEW TYPE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>356.2</p>
</blockquote></td>
<td>INSURANCE REVIEW</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>356.21</p>
</blockquote></td>
<td>CLAIMS TRACKING DENIAL REASONS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>356.3</p>
</blockquote></td>
<td>CLAIMS TRACKING SI/IS CATEGORIES</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>356.399</p>
</blockquote></td>
<td>CLAIMS TRACKING/BILL</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>356.4</p>
</blockquote></td>
<td>CLAIMS TRACKING NON-ACUTE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>CLASSIFICATIONS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>356.5</p>
</blockquote></td>
<td>CLAIMS TRACKING ALOS</td>
<td>@</td>
<td></td>
<td></td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>356.6</p>
</blockquote></td>
<td>CLAIMS TRACKING TYPE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>356.7</p>
</blockquote></td>
<td>CLAIMS TRACKING ACTION</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>356.8</p>
</blockquote></td>
<td>CLAIMS TRACKING NON-BILLABLE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>REASONS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>356.9</p>
</blockquote></td>
<td>INPATIENT DIAGNOSIS</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>356.91</p>
</blockquote></td>
<td>INPATIENT PROCEDURE</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>356.93</p>
</blockquote></td>
<td>INPATIENT INTERIM DRG</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>356.94</p>
</blockquote></td>
<td>INPATIENT PROVIDERS</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>357</p>
</blockquote></td>
<td>ENCOUNTER FORM</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>357.1</p>
</blockquote></td>
<td>ENCOUNTER FORM BLOCK</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>357.2</p>
</blockquote></td>
<td>SELECTION LIST</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>357.3</p>
</blockquote></td>
<td>SELECTION</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>357.4</p>
</blockquote></td>
<td>SELECTION GROUP</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>357.5</p>
</blockquote></td>
<td>DATA FIELD</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>357.6</p>
</blockquote></td>
<td>PACKAGE INTERFACE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>357.7</p>
</blockquote></td>
<td>FORM LINE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>357.8</p>
</blockquote></td>
<td>TEXT AREA</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>357.91</p>
</blockquote></td>
<td>MARKING AREA TYPE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>357.92</p>
</blockquote></td>
<td>PRINT CONDITIONS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>358</p>
</blockquote></td>
<td>IMP/EXP ENCOUNTER FORM</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>358.1</p>
</blockquote></td>
<td>IMP/EXP ENCOUNTER FORM BLOCK</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>358.2</p>
</blockquote></td>
<td>IMP/EXP SELECTION LIST</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>358.3</p>
</blockquote></td>
<td>IMP/EXP SELECTION</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>358.4</p>
</blockquote></td>
<td>IMP/EXP SELECTION GROUP</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>358.5</p>
</blockquote></td>
<td>IMP/EXP DATA FIELD</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>358.6</p>
</blockquote></td>
<td>IMP/EXP PACKAGE INTERFACE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>358.7</p>
</blockquote></td>
<td>IMP/EXP FORM LINE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>358.8</p>
</blockquote></td>
<td>IMP/EXP TEXT AREA</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>358.91</p>
</blockquote></td>
<td>IMP/EXP MARKING AREA</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>362.1</p>
</blockquote></td>
<td>IB AUTOMATED BILLING COMMENTS</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>362.3</p>
</blockquote></td>
<td>IB BILL/CLAIMS DIAGNOSIS</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>362.4</p>
</blockquote></td>
<td>IB BILL/CLAIMS PRESCRIPTION REFILL</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>362.5</p>
</blockquote></td>
<td>IB BILL/CLAIMS PROSTHETICS</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>399</p>
</blockquote></td>
<td>BILL/CLAIMS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>399.1</p>
</blockquote></td>
<td>MCCR UTILITY</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>399.2</p>
</blockquote></td>
<td>REVENUE CODE</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

National Package Security

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 43%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>399.3</p>
</blockquote></th>
<th><blockquote>
<p>RATE TYPE</p>
</blockquote></th>
<th colspan="5">@</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>399.4</p>
</blockquote></td>
<td><blockquote>
<p>MCCR INCONSISTENT DATA ELEMENT</p>
</blockquote></td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>399.5</p>
</blockquote></td>
<td><blockquote>
<p>BILLING RATES</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>dD</p>
</blockquote></td>
<td><blockquote>
<p>d</p>
</blockquote></td>
<td>d</td>
<td>d</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>409.95</p>
</blockquote></td>
<td><blockquote>
<p>PRINT MANAGER CLINIC SETUP</p>
</blockquote></td>
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
<tr class="even">
<td><blockquote>
<p>409.96</p>
</blockquote></td>
<td><blockquote>
<p>PRINT MANAGER DIVISION SETUP</p>
</blockquote></td>
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