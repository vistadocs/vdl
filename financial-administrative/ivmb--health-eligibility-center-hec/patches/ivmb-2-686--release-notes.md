---
title: IVMB*2*686 Geographic Means Test (GMT) Release Notes
doc_type: RN
doc_label: Release Notes
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
  - priority
  - table
  - threshold
  - contents
  - veterans
  - group
  - enrollment
  - copay
  - required
page_count: 0
word_count: 3732
section_count: 15
table_count: 4
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: December 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p686_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p686_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

Health eligibility center

Atlanta, GA

Geographic Means Test

(GMT )

Release Notes

IVMB\*2\*686

December 2002

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose of this Manual](#purpose-of-this-manual)
  - [Related Documents](#related-documents)
  - [Acronyms and Definitions](#acronyms-and-definitions)
  - [HUD Indices (a.k.a. Geographic Means Test \[GMT\] Thresholds)](#hud-indices-aka-geographic-means-test-gmt-thresholds)
  - [GMT Copay Required Status](#gmt-copay-required-status)
  - [New User Options for GMT Threshold Lookups](#new-user-options-for-gmt-threshold-lookups)
  - [Modify Enrollment Priority Group 7](#modify-enrollment-priority-group-7)
  - [Create Enrollment Priority Group 8](#create-enrollment-priority-group-8)
  - [Reset the Enrollment Group Threshold (EGT)](#reset-the-enrollment-group-threshold-egt)
  - [Changes to Category A and Category C References](#changes-to-category-a-and-category-c-references)
- [Technical Release Notes](#technical-release-notes)
  - [Patch Installation Sequence](#patch-installation-sequence)
    - [Z05, Demographic Data Transmission](#z05-demographic-data-transmission)
    - [Z07, Full Data Transmission from VAMC to HEC](#z07-full-data-transmission-from-vamc-to-hec)
    - [Z10, Income Test Data Transmission from HEC to VAMC](#z10-income-test-data-transmission-from-hec-to-vamc)
  - [One-time Conversion](#one-time-conversion)
  - [Conversion Report](#conversion-report)
- [Appendix A – GMT Enrollment Priority / Copayment Status Matrix](#appendix-a-gmt-enrollment-priority-copayment-status-matrix)
- [Appendix B – Conversion Matrix for MT Copay Required Veterans](#appendix-b-conversion-matrix-for-mt-copay-required-veterans)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 23, 2002, President Bush signed into law Public Law 107-135, *The Department of Veterans Affairs Health Care Programs Enhancement Act of 2001*. Section 202 of this Act requires the implementation of HUD indices to determine geographic income thresholds in support of more discrete means testing. Veterans in Priority Group 7 are eligible for treatment as a low-income family under section 3(b) of the United States Housing Act of 1973 (42 U.S.C. 1437a(b)) for the area in which such veterans reside, regardless of whether such veterans are treated as single person families under paragraph (3)(A) of such section 3(b) or as families under paragraph (3)(b). This Act also established Priority Group 8 for any veterans described in section 1710(a)(3) of titles 38 U.S.C. who are not covered by Priority Group 7. Refer to Appendix A for a GMT Enrollment Priority / Copayment Status Matrix.

Development of the GMT software is a combined effort on the part of Office of Policy and Planning (OPP), Office of Information (OI), and Chief Business Office (CBO).

A one-time conversion of Means Test Copay Required veterans who declined to provide income information, whose means test is greater than one year old or whose current income is greater than the MT threshold will occur only in the HEC Legacy system upon implementation of the GMT software. This conversion will determine whether these veterans should be placed in the new Priority Group 8 or the new GMT Copay Required means test status. The results of the conversion will be transmitted to all applicable VAMCs upon completion of the process. Refer to Appendix B of this document for a conversion matrix for MT Copay Required veterans.

During the processing of the GMT Conversion, a HEC user can monitor the progress by running the GMT Conversion Processing Report. Refer to the GMT Technical Manual for information about how to generate and use this report.

## Purpose of this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to provide high-level user and technical information about Enrollment-related GMT functionality.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- GMT User Manual (IVMB_2_P686_UM.PDF)
- GMT Technical Manual (IVMB_2_P686_TM.PDF)
- GMT Installation Guide (IVMB_2_P686_IG.PDF)

## Acronyms and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Acronyms

|             |                                                  |
|-------------|--------------------------------------------------|
| Acronym | Description                                  |
| AI          | Address Indexing                                 |
| AR          | Accounts Receivable                              |
| CBO         | Chief Business Office                            |
| EGT         | Enrollment Group Threshold                       |
| FIPS        | Federal Information Processing Standard          |
| GMT         | Geographic Means Test                            |
| HUD         | U.S. Department of Housing and Urban Development |
| IB          | Integrated Billing                               |
| MT          | Means Test                                       |
| NVS         | National V*IST*A Support                 |
| PIMS        | Patient Information Management System            |
| VAMC        | Veterans Administration Medical Center           |
| OPP         | Office of Policy and Planning                    |
| OI          | Office of Information                            |
Definitions
|                   |                                                                                                                             |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Term          | Definition                                                                                                              |
| Disenrollment     | Voluntary request from veteran to discontinue enrollment in the VA Health Care system                                       |
| GMT Thresholds    | a.k.a. HUD Indices. Geographical income level thresholds set yearly by the U.S. Department of Housing and Urban Development |
| MT Thresholds     | Income threshold levels set yearly within the VA for the purpose of establishing benefit levels for veterans                |
| HEC Legacy System | M-based database currently in use                                                                                           |

#### # User Release Notes

## HUD Indices (a.k.a. Geographic Means Test \[GMT\] Thresholds)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 23, 2002, President Bush signed into law H.R. 3477, The Department of Veterans Affairs Health Care Programs Enhancement Act of 2001. Section 202 of this Act requires the implementation of U.S. Department of Housing and Urban Development (HUD) Indices to determine geographic income thresholds in support of more discrete means testing. A new GMT copayment status will identify veterans who qualify for a reduced inpatient copayment rate. The effective date of the regulation to support this legislation is October 1, 2002. Like traditional Means Test thresholds, the GMT thresholds will be applied in a retrospective manner (i.e., HUD Indices published in Calendar Year 2002 will be used for Means Tests performed in Calendar Year 2003). Information about HUD income limits is available on the Data Sets Page of the HUD User Web Site at <http://www.huduser.org/datasets/il.html>.

The HUD Indices will be uploaded into V*IST*A annually, along with the traditional means test threshold values, in a patch released in December of each year. They will be activated on January 1<sup>st</sup> of each year. The indices from previous years will be stored indefinitely in both V*IST*A and HEC systems. For information about the implementation of HUD Indices, refer to the GMT Installation Guide and GMT Technical Manual.

## GMT Copay Required Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new Means Test Status (GMT Copay Required) identifies veterans who qualify for a reduced inpatient copayment rate ( 20% of the current inpatient copayment rate). The outpatient copayment rate stays the same. In areas where the GMT threshold is less than or equal to the MT threshold, all veterans required to pay copayments will be billed the full MT copayments as appropriate. Refer to Section 3.2.2 of the Geographic Means Testing SRS for detailed information about the GMT Copayment Required Status business rules and the logic that supports the business rules. Refer to Appendix A of this document for a matrix of the GMT Enrollment Priority / Copayment Status business rules.

The following veterans are subject to the GMT copayment when the GMT threshold is greater than the MT threshold:

- Veterans whose income is less than or equal to the MT threshold and whose estate value is greater than or equal to the net worth threshold (pending adjudication)
- Veterans whose income is greater than the MT threshold, but less than or equal to the GMT threshold

## New User Options for GMT Threshold Lookups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new user options are created with implementation of the HEC GMT software. Refer to the HEC GMT User Manual for information about how to use these options.

- GMT Threshold Lookup by Zip Code returns GMT threshold information based on a user-specified Zip Code. The user is prompted to enter a Zip Code. The output includes county name, state, year, Zip Code, FIPS Code, number in household, and GMT threshold dollar amount.
- GMT Threshold Address Lookup returns GMT address information for a user-specified veteran within a specified income year. The user is prompted to select a veteran and to select an income year. The output includes the following GMT address information for the selected veteran during the specified income year: SSN, street address, city, state, zip code, and county.

## Modify Enrollment Priority Group 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enrollment Priority Group 7 will be modified to include the following groups of veterans. *<u>In areas where the GMT Threshold is equal to or less than the MT Threshold, there will be no Enrollment Priority Group 7 veterans; those areas will have Enrollment Priority Group 8 veterans only.</u>* Refer to Section 3.2.3 of the GMT SRS for detailed information about the business rules for modifying Enrollment Priority Group 7. Refer to Appendix A of this document for a GMT Enrollment Priority / Copayment Matrix.

- Veterans whose income is greater than the MT Threshold and less than or equal to the GMT Threshold, and are not eligible for placement in a higher priority group
- Veterans whose income is less than or equal to the MT Threshold, but whose net worth (total assets minus debt) is greater than or equal to the Net Worth (Property) Threshold (currently set at \$80K) and are not eligible for placement in a higher priority group
- Veterans included in Priority Group 7 will be divided into the following sub-categories:
  - Group 7a: Noncompensable 0% service-connected veterans who were in an enrolled status on a specified date announced in a Federal Register document and who subsequently do not request disenrollment
  - Group 7c: Non-service-connected veterans who are in an enrolled status on a specific date announced in a Federal Register document and who subsequently do not request disenrollment

## Create Enrollment Priority Group 8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GMT software creates a new Enrollment Priority Group 8 that includes the following veterans. *<u>If the GMT Threshold is equal to or less than the MT Threshold in any locale, there will be no Priority Group 7 veterans for that locale; it will have Priority Group 8 veterans only.</u>* Refer to Section 3.1.5 of the GMT SRS for detailed information about the business rules for creating Enrollment Priority Group 8. Refer to Appendix A of this document for a GMT Enrollment Priority / Copayment Matrix.

- Veterans whose income is greater than the MT threshold and greater than the GMT Threshold
- Veterans who decline to provide income information and who agree to make MT copayments
- Veterans whose income exceeds the MT Threshold and who live in a location where the GMT Threshold is less than or equal to the MT Threshold
- Veterans included in Priority Group 8 will be divided into the following sub-categories:
  - Group 8a: Noncompensable 0% service-connected veterans who were in an enrolled status on a specified date announced in a <u>Federal Register</u> document and who subsequently do not request disenrollment
  - Group 8c: Non-service-connected veterans who are in an enrolled status on a specific date announced in a <u>Federal Register</u> document and who subsequently do not request disenrollment

## Reset the Enrollment Group Threshold (EGT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The GMT software will automatically reset the Enrollment Group Threshold (EGT) to from the current 7c to the new 8c, where it will remain until a new EGT is regulated.

## Changes to Category A and Category C References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although this does not affect the GMT functionality, all user viewable references to Category A and Category C means test statuses in enrollment-related software have been modified to reflect the following changes:

Category A (Cat A) is now MT Copay Exempt

Category C (Cat C) is now MT Copay Required

# Technical Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The following table illustrates the mandatory sequence for installing GMT patches. All of the GMT patches will be released with an Emergency status. *<u>It is imperative that sites install the patches in the sequence shown by the dates specified.</u>* V*IST*A patch installations will be monitored by NVS. For detailed installation information about the GMT V*IST*A Enrollment patches, refer to the V*IST*A GMT Installation Guide. For detailed information about the GMT HEC patch installation, refer to the HEC GMT Installation Guide.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 24%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 10%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Patches</strong></th>
<th><p><strong>Release to</strong></p>
<p><strong>NVS</strong></p></th>
<th><p><strong>National</strong></p>
<p><strong>Release to</strong></p>
<p><strong>Field</strong></p></th>
<th colspan="2"><p><strong>Compliance</strong></p>
<p><strong>Date</strong></p></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p><strong>IB Part 1</strong></p>
<p>IB*2.0*179</p></td>
<td><strong>9/20/02</strong></td>
<td><strong>9/25/02</strong></td>
<td colspan="2"><strong>9/30/02</strong></td>
<td>Effective Date: 10/1/02</td>
</tr>
<tr class="even">
<td>2</td>
<td><p><strong>AI Kernel</strong></p>
<p>XU*8*246</p>
<p><em><strong>The following patches are being released in HOST file DG_53_P454.KID:</strong></em></p>
<p><strong>Enrollment V<em>IST</em>A Part 1</strong></p>
<p>DG *5.3*454</p>
<p>IVM*2*58</p>
<p><strong>PIMS</strong></p>
<p>DG*5.3*466</p>
<p>SD*5.3*258</p></td>
<td><strong>11/25/02</strong></td>
<td><strong>12/2/2002</strong></td>
<td colspan="2"><strong>12/4/2002</strong></td>
<td><ol type="1">
<li><p>Release Kernel patch first; sites must install before PIMS &amp; Enrollment patches.</p></li>
<li><p>Release PIMS &amp; Enrollment patches in HOST file DG_53_P454.KID.</p></li>
<li><p>NVS sends patches to Hines Anonymous directory 11/29 and monitors replication to Albany &amp; SLC servers 11/30 – 12/1.</p></li>
<li><p>Project Implementation Team will contact sites not in compliance on 12/5/02.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>3</td>
<td><p><strong>HEC Legacy</strong></p>
<p>IVMB*2*686</p></td>
<td><strong>N/A</strong></td>
<td><p><strong>Release to HEC Production</strong></p>
<p><strong>12/9/02</strong></p></td>
<td colspan="2"><strong>12/11/02</strong></td>
<td>Monitor in HEC production 12/9-10-11</td>
</tr>
<tr class="even">
<td>4</td>
<td><p><em><strong>The following files are being released in HOST file EAS_1_P13.KID:</strong></em></p>
<p><strong>Enrollment V<em>IST</em>A Part 2</strong></p>
<p>EAS*1*13</p>
<p>DG*5.3*456</p>
<p>IVM*2*62</p>
<p><strong>IB Part 2</strong></p>
<p>IB*2.0*183</p>
<p>PRCA*4.5*181</p></td>
<td><strong>12/5/02</strong></td>
<td><strong>12/16/02</strong></td>
<td colspan="2"><strong>12/19/02</strong></td>
<td><ol type="1">
<li><p>Release PIMS &amp; Enrollment patches in HOST file EAS_1_P13.KID.</p></li>
<li><p>NVS sends patches to Hines Anonymous directory 12/13 and monitors replication to Albany &amp; SLC servers 12/13 – 12/14.</p></li>
<li><p>Project Implementation Team will contact sites not in compliance on 12/20/02.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>5</td>
<td colspan="6"><em><strong>All patches listed in Steps 1 – 4 above must be operational at sites on 1/03/03</strong></em></td>
</tr>
<tr class="even">
<td><strong>6</strong></td>
<td><p>IVM*2*67</p>
<p>DG*5.3*481</p>
<p>IB*2.0*202</p></td>
<td>Approximately 2 weeks after conversion completion (date TBD)</td>
<td colspan="2">TBD</td>
<td>TBD</td>
<td>Clean up patches to remove code no longer used after GMT conversion completes. Patches will be released in a HOST file.</td>
</tr>
</tbody>
</table>

#### ## Address Indexing (AI)

#### #### Address Indexing is a sub-project of GMT that provides:

#### Address changes to support GMT

#### Creates two new files to standardize the FIPS County Code 

#### Postal Code File (#5.12) (stores all known Postal Codes as well as other associated information related to the Postal Code)

#### County Code File (#5.13) (contains all known US County FIPS codes according to the USGS, HUD, and USPS)

#### Provides an automated process that matches the veteran’s address (FIPS county code) against the GMT thresholds

#### Modifies the HL7 Z05 receiver process to accept the FIPS county code

#### Modifies the HL7 Z07 builder to send the FIPS county code

#### Enhanced address functionality

#### Zip code linkage

#### Add changed address functionality

#### Changes to HL7 messages (see HL7 Messaging Changes section of this document)

#### ## HL7 Messaging Changes

### Z05, Demographic Data Transmission 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added FIPS County Code to the receiver process to support address indexing

### Z07, Full Data Transmission from VAMC to HEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added GMT Copayment Status to the ZMT Segment of the Z07 message and builder process
- Added Hardship Reason field to the ZMT Segment of the Z07 message and builder process
- Added RF1 segment to ORU~Z07 & ORF~Z07
- Send FIPS County Code to HEC to support address indexing

### Z10, Income Test Data Transmission from HEC to VAMC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added GMT Copayment Status to the ZMT Segment.
- Added Hardship Reason field to the ZMT Segment.

## One-time Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A one-time conversion of Means Test Copay Required veterans who declined to provide income information, whose means test is greater than one year old or whose current income is greater than the MT threshold will occur only in the HEC Legacy system upon implementation of the GMT software. This conversion will determine whether these veterans should be placed in the new Priority Group 8 or the new GMT Copay Required means test status. The results of the conversion will be transmitted to all applicable VAMCs upon completion of the process. Refer to Appendix B of this document for a conversion matrix for MT Copay Required veterans.

## Conversion Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the processing of the GMT Conversion, a HEC user can monitor the progress by running the GMT Conversion Processing Report, which will provide the following cumulative totals. Refer to the HEC GMT Technical Manual for information about how to generate and use this report. Refer to Appendix B of this document for a conversion matrix for MT Copay Required veterans.

- Converted while Pending Adjudication
- Converted to Exempt due to Net Worth
- Converted to GMT Copay Required due to Income
- Converted to GMT Copay Required due to Net Worth
- Converted to Priority Group 5
- Converted to Priority Group 7
- Converted to Priority Group 8
- Converted to Priority Group 8 due to Income
- Converted to Priority Group 8 due to lapsed MT
- Converted to Priority Group 8 - Declines to give info

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