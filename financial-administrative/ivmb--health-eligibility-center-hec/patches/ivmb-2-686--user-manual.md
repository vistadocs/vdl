---
title: IVMB*2*686 Geographic Means Test (GMT) User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Geographic Means Test (GMT)
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*686
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - strong
  - table
  - threshold
  - priority
  - contents
  - copay
  - required
  - class
  - veterans
  - income
page_count: 0
word_count: 1707
section_count: 7
table_count: 2
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: December 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p686_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p686_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

Health eligibility center

Atlanta, GA

geographic Means Test

(GMT)

USER Manual

IVMB\*2\*686

December 2002

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose](#purpose)
  - [Related Manuals](#related-manuals)
- [Using the GMT Menu Options](#using-the-gmt-menu-options)
  - [Accessing the GMT Menu Options](#accessing-the-gmt-menu-options)
  - [GMT Threshold Address Lookup](#gmt-threshold-address-lookup)
  - [GMT Threshold Lookup by ZIP Code or City](#gmt-threshold-lookup-by-zip-code-or-city)
- [Glossary](#glossary)
- [Appendix A – GMT Enrollment Priority / Copayment Status Matrix](#appendix-a-gmt-enrollment-priority-copayment-status-matrix)
- [Appendix B – Conversion Matrix for MT Copay Required Veterans](#appendix-b-conversion-matrix-for-mt-copay-required-veterans)
- [Index](#index)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 23, 2002, President Bush signed into law Public Law 107-135, *The Department of Veterans Affairs Health Care Programs Enhancement Act of 2001*. Section 202 of this Act requires the implementation of HUD indices to determine geographic income thresholds in support of more discrete means testing. Veterans in Priority Group 7 are eligible for treatment as a low-income family under section 3(b) of the United States Housing Act of 1973 (42 U.S.C. 1437a(b)) for the area in which such veterans reside, regardless of whether such veterans are treated as single person families under paragraph (3)(A) of such section 3(b) or as families under paragraph (3)(b). This Act also established Priority Group 8 for any veterans described in section 1710(a)(3) of titles 38 U.S.C. who are not covered by Priority Group 7. Refer to Appendix A for a GMT Enrollment Priority / Copayment Status Matrix.

Development of the GMT software is a combined effort on the part of Office of Policy and Planning (OPP), Office of Information (OI), and Chief Business Office (CBO).

A one-time conversion of Means Test Copay Required veterans who declined to provide income information, whose means test is greater than one year old or whose current income is greater than the MT threshold will occur only in the HEC Legacy system upon implementation of the GMT software. This conversion will determine whether these veterans should be placed in the new Priority Group 8 or the new GMT Copay Required means test status. The results of the conversion will be transmitted to all applicable VAMCs upon completion of the process. Refer to Appendix B of this document for a conversion matrix for MT Copay Required veterans.

During the processing of the GMT Conversion, a HEC user can monitor the progress by running the GMT Conversion Processing Report. Refer to the GMT Technical Manual for information about how to generate and use this report.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this user manual is to provide instructions for using the new user options provided by the GMT software.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- GMT Release Notes (IVMB_2_P686_RN.PDF)
- GMT Technical Manual (IVMB_2_P686_TM.PDF)
- GMT Installation Guide (IVMB_2_P686_IG.PDF)

# Using the GMT Menu Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Accessing the GMT Menu Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can access the GMT Menu Options from the DCD Contact Representative Menu.

## GMT Threshold Address Lookup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the GMT Threshold Address Lookup option to display the GMT Threshold address used to determine a specified veterans GMT address for a specific income year. You will be prompted to select a veteran and an income year.

The software returns the following information for a valid income year:

- Veteran’s Name and Social Security Number (SSN)
- Street Address
- City
- State
- Zip
- County Name

## GMT Threshold Lookup by ZIP Code or City 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the GMT Threshold Address Lookup by ZIP Code or City option to display GMT Threshold values for a valid Postal Code (a.k.a. ZIP Code). The only user prompt is “ZIP Code:”, and a response is required. You must enter a ZIP Code or a city name to generate an output, or a caret (^) to return to the menu. If you enter a city name and the software finds multiple cities with the same name, it returns a list of the cities with their corresponding ZIP Codes from which you can make your selection.

The software returns the following information for a valid ZIP Code:

- ZIP Code
- County Name
- State
- Income year in which the GMT Thresholds apply
- Federal Information Processing Standard (FIPS) \[County\] Code
- Number of family members in household
- GMT Threshold dollar amounts for up to eight members in household
- Family size adjustments information for all income limits
- The formula for determining GMT Threshold dollar amounts for households with more than eight family members

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                                                  |
|-------------|--------------------------------------------------|
| Acronym | Description                                  |
| AR          | Accounts Receivable                              |
| FIPS        | Federal Information Processing Standard          |
| GMT         | Geographic Means Test                            |
| HUD         | U.S. Department of Housing and Urban Development |
| IB          | Integrated Billing                               |
| MT          | Means Test                                       |
| PIMS        | Patient Information Management System            |
| VAMC        | Veterans Administration Medical Center           |
| OPP         | Office of Policy and Planning                    |
| HAS         | Health Administration Service                    |
| OI          | Office of Information                            |

# Appendix A – GMT Enrollment Priority / Copayment Status Matrix 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 21%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="6"><strong>GMT Enrollment Priority / Copayment Matrix</strong></td>
</tr>
<tr class="even">
<td><p><strong>Income vs.</strong></p>
<p><strong>Thresholds</strong></p></td>
<td><strong>Estate vs. Net Worth Threshold</strong></td>
<td><strong>Veteran’s Enrollment Priority</strong></td>
<td><strong>Exceptions to Veteran’s Enrollment Priority</strong></td>
<td><strong>*Copayment Status</strong></td>
<td><strong>Comment</strong></td>
</tr>
<tr class="odd">
<td>Less than MT</td>
<td><p>Less than Net Worth Threshold</p>
<p>($80K)</p></td>
<td>Priority 5</td>
<td>If Catastrophically Disabled, Priority 4</td>
<td>MT Copay Exempt</td>
<td></td>
</tr>
<tr class="even">
<td>Less than MT</td>
<td><p>Greater than Net Worth Threshold</p>
<p>($80K)</p></td>
<td>Priority 7</td>
<td><ul>
<li><p>If exposed to Agent Orange, Ionizing Radiation, or Environmental Contaminants, Priority 6.</p></li>
<li><p>If Catastrophically Disabled, Priority 4</p></li>
</ul></td>
<td>GMT Copay Required</td>
<td><p>Pending Adjudication</p>
<p><strong>Note: In this rule, GMT threshold is greater than MT threshold</strong></p></td>
</tr>
<tr class="odd">
<td>Less than MT</td>
<td><p>Greater than Net Worth Threshold</p>
<p>($80K)</p></td>
<td>Priority 8</td>
<td><ul>
<li><p>If exposed to Agent Orange, Ionizing Radiation, or Environmental Contaminants, Priority 6.</p></li>
<li><p>If Catastrophically Disabled, Priority 4</p></li>
</ul></td>
<td>MT Copay Required</td>
<td><p>Pending Adjudication</p>
<p><strong>Note: In this rule, GMT threshold is less than MT threshold</strong></p></td>
</tr>
<tr class="even">
<td><p>Greater than MT</p>
<p>Less than GMT</p></td>
<td>Not applicable</td>
<td>Priority 7</td>
<td><ul>
<li><p>If exposed to Agent Orange, Ionizing Radiation, or Environmental Contaminants, Priority 6.</p></li>
<li><p>If Catastrophically Disabled, Priority 4</p></li>
</ul></td>
<td>GMT Copay Required</td>
<td></td>
</tr>
<tr class="odd">
<td><p>Greater than MT</p>
<p>Greater than GMT</p></td>
<td>Not applicable</td>
<td>Priority 8</td>
<td><ul>
<li><p>If exposed to Agent Orange, Ionizing Radiation, or Environmental Contaminants, Priority 6.</p></li>
<li><p>If Catastrophically Disabled, Priority 4</p></li>
</ul></td>
<td>MT Copay Required</td>
<td></td>
</tr>
</tbody>
</table>

\*GMT copayment = regular outpatient MT copayment rate and 20% of current inpatient MT copayment rate

# Appendix B – Conversion Matrix for MT Copay Required Veterans 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 25%" />
<col style="width: 20%" />
<col style="width: 34%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="4"><strong>Conversion Matrix for MT Copay Required Veterans</strong></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Current Status</strong></td>
<td colspan="2"><strong>Post Implementation Status</strong></td>
</tr>
<tr class="odd">
<td><p><strong>Enrollment</strong></p>
<p><strong>Priority</strong></p>
<p><strong>Group</strong></p></td>
<td><strong>Income Less Than GMT</strong></td>
<td><strong>Enrollment Priority Group</strong></td>
<td><strong>MT Copay Status</strong></td>
</tr>
<tr class="even">
<td>4</td>
<td>Yes</td>
<td>4</td>
<td>GMT Copay Required</td>
</tr>
<tr class="odd">
<td>4</td>
<td>No</td>
<td>4</td>
<td>MT Copay Required</td>
</tr>
<tr class="even">
<td>6</td>
<td>Yes</td>
<td>6</td>
<td>GMT Copay Required</td>
</tr>
<tr class="odd">
<td>6</td>
<td>No</td>
<td>6</td>
<td>MT Copay Required</td>
</tr>
<tr class="even">
<td>7</td>
<td>Yes</td>
<td>7</td>
<td><p>GMT Copay Required</p>
<p><strong>Only if MT is within past year &amp; GMT is greater than MT threshold</strong></p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Yes</td>
<td>8</td>
<td><p>MT Copay Required</p>
<p><strong>Only if MT is greater than 365 days</strong></p></td>
</tr>
<tr class="even">
<td>7</td>
<td>No</td>
<td>8</td>
<td>MT Copay Required</td>
</tr>
<tr class="odd">
<td>7</td>
<td><ul>
<li><p>Declines to provide financial information</p></li>
<li><p>Agrees to Pay Copayments</p></li>
</ul></td>
<td>8</td>
<td>MT Copay Required</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Net Worth determination on all veterans providing income</strong></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Income</td>
<td>Net Worth</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Less than MT</td>
<td>Greater than $80K</td>
<td>7</td>
<td><p>GMT Copay Required</p>
<p><strong>If GMT threshold is greater than MT threshold</strong></p></td>
</tr>
<tr class="odd">
<td>Less than MT</td>
<td>Greater than $80K</td>
<td>8</td>
<td><p>MT Copay Required</p>
<p><strong>If GMT threshold is less than MT threshold</strong></p></td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Accessing the GMT Menu Options 2
Appendix A – GMT Enrollment Priority / Copayment Status Matrix 4
Appendix B – Conversion Matrix for MT Copay Required Veterans 5
G
Glossary 3
GMT Threshold Address Lookup 2
GMT Threshold Lookup by ZIP Code or City 2
I
Introduction 1
O
Overview 1
P
Purpose 1
R
Related Manuals 1
U
Using the GMT Menu Options 2
