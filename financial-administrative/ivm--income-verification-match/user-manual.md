---
title: IVM Version 2 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: IVM
app_name: Income Verification Match
section: FIN
app_status: active
pkg_ns: IVM
patch_ver: 2
patch_id: IVM*2
group_key: "IVM:IVM:2"
file_numbers: []
security_keys: []
menu_options: 1
description: Public Law 101-508 permits the Department of Veterans Affairs (VA) to verify income data with the Internal Revenue Service (IRS) and Social Security Administration (SSA) for veterans receiving VA health care services whose eligibility for medical care is based on income. The Income Verification Matc
audience: 
keywords: 
  - upload
  - insurance
  - patient
  - table
  - date
  - redacted
  - contents
  - class
  - means
  - report
page_count: 0
word_count: 8708
section_count: 16
table_count: 6
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: October 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Income_Verif_Match_(IVM)/ivm_2_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Income_Verif_Match_(IVM)/ivm_2_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=44"
---

![](ivm-version-2-user-manual/001.png)

inCOME VERIFICATION MATCH(IVM)user MANUAL

October 1994

Office of Enterprise Development

Management, Enrollment and Financial Systems (MEFS)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [# Introduction](#introduction)
  - [Background](#background)
  - [Functionality](#functionality)
    - [User Interactive Functions](#user-interactive-functions)
    - [Non-interactive Functions](#non-interactive-functions)
  - [Integration](#integration)
    - [Patient Information Management System (PIMS)](#patient-information-management-system-pims)
    - [Integrated Billing (IB)](#integrated-billing-ib)
    - [Health Level 7 (HL7)](#health-level-7-hl7)
  - [Related Manuals](#related-manuals)
- [Package Management](#package-management)
- [Using the Software](#using-the-software)
  - [IVM Upload Menu](#ivm-upload-menu)
    - [Demographics Upload](#demographics-upload)
    - [Insurance Upload](#insurance-upload)
    - [Please Note:SSN Upload is no longer used in VistA. The Enrollment System Redesign HEC Legacy Replacement application now does it automatically.](#please-notessn-upload-is-no-longer-used-in-vista-the-enrollment-system-redesign-hec-legacy-replacement-application-now-does-it-automatically)
    - [IVM Address Updates Pending Review](#ivm-address-updates-pending-review)
  - [IVM Output Menu](#ivm-output-menu)
    - [Billing Transmission Report](#billing-transmission-report)
    - [IVM Case Inquiry](#ivm-case-inquiry)
    - [Means Test Comparison Report](#means-test-comparison-report)
    - [IVM Address Change Log Report](#ivm-address-change-log-report)
  - [IVM System Manager's Menu](#ivm-system-managers-menu)
    - [IVM Parameter Enter/Edit](#ivm-parameter-enteredit)
    - [Purge IVM Transmissions](#purge-ivm-transmissions)
    - [IVM Transmission Report](#ivm-transmission-report)
  - [IVM Transmission Error Processing](#ivm-transmission-error-processing)
  - [IVM Financial Query](#ivm-financial-query)
- [Glossary](#glossary)
- [Appendix A - Sample Mail Messages](#appendix-a-sample-mail-messages)
  - [Completed Purge of IVM Transmission Records](#completed-purge-of-ivm-transmission-records)
  - [IVM - Means Test Upload](#ivm-means-test-upload)
  - [IVM - Means Test Deleted](#ivm-means-test-deleted)
  - [Messages Awaiting Transmission](#messages-awaiting-transmission)
  - [Error Message From the HEC](#error-message-from-the-hec)
  - [Missing Primary Long ID Field](#missing-primary-long-id-field)
- [Appendix B - List Manager](#appendix-b-list-manager)
- [Index](#index)
Please Note: Effective May, 2001, changes to IVM documentation resulting from released patches will be described in the Revision History section. In lieu of change pages, the complete user manual will be released with the software patches associated with the changes described in this section.
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 35%" />
<col style="width: 21%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Revision Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Related Patch Number(S)</strong></th>
<th><strong>Project Manager (PM) and Author (Auth) (beginning with 1/19/05 entry)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3/20/2001</td>
<td>IVM Case Inquiry option - Revised Introduction section of to include Co-Pay Exemption Tests</td>
<td>IVM*2.0*17</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/20/2001</td>
<td>Added new option: IVM Financial Query</td>
<td>IVM*2.0*17</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/20/2001</td>
<td>Updated fonts to comply with current documentation standards where applicable</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/20/2001</td>
<td>Added Revision History section</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/20/2001</td>
<td>Moved List Manager mnemonics into a table</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/1/2003</td>
<td>Updated Demographics Upload option</td>
<td>IVM*2*79</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/11/03</td>
<td>Updated Demographics Upload option</td>
<td>IVM*2*79</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/12/03</td>
<td>Updated Revision History section</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/12/03</td>
<td>Updated Orientation section</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/12/03</td>
<td>Replaced “HEC” with “the HEC”, where appropriate</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/12/03</td>
<td>Corrected formatting of “<strong>V<em>IST</em>A”</strong> in text, where appropriate</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/12/03</td>
<td>Updated Introduction section</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/12/03</td>
<td>Updated references to Category C</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/12/03</td>
<td>Updated references to Category A</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/12/03</td>
<td>Updated headings format throughout manual</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/12/03</td>
<td>Removed outdated Preface section</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/13/03</td>
<td>Updated IVM Demographics Upload option</td>
<td>IVM*2*79</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/13/03</td>
<td>Added new option: IVM Address Updates Pending Review</td>
<td>IVM*2*79</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/12/03</td>
<td>Updated IVM Demographics Upload option</td>
<td>IVM*2*79</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/15/03</td>
<td>Updated IVM Demographics Upload option</td>
<td>IVM*2*79</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/25/04</td>
<td>Updated new Date of Death functionality in the IVM Upload/ Demographics Upload section.</td>
<td>IVM*2*56</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/23/04</td>
<td>Changed all sensitive information to generic information</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/29/04</td>
<td>Added Field #.2917 to table of non-uploadable data elements on Page 5</td>
<td>N/A</td>
<td>REDACTED, REDACTED</td>
</tr>
<tr class="even">
<td>11/15/04</td>
<td>Changed all sensitive information to conform to the agreed upon convention as set forth in SOP 192-352 Displaying Sensitive Data, dated 9/22/04</td>
<td>N/A</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/19/05</td>
<td>Updated Demographics Upload Option</td>
<td>IVM*2*102</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>10/27/05</td>
<td>Added new user option, IVM Address Change Log Report, in the IVM Output Menu section (per discussion with REDACTED)</td>
<td>IVM*2*108</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>10/27/05</td>
<td>Moved IVM Address Updates Pending Review from IVM Output Menu section to IVM Upload Menu section (per discussion with REDACTED)</td>
<td>IVM*2*108</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>4/10/06</td>
<td>Updated IVM Address Change Log Report option</td>
<td>IVM*2*106</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>4/13/06</td>
<td>Updated IVM Address Change Log Report option based on feedback and additional research</td>
<td>IVM*2*106</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>4/25/06</td>
<td>Additional updates to the IVM Address Change Log Report option</td>
<td>IVM*2*106</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED, REDACTED</p></td>
</tr>
<tr class="odd">
<td>8/3/06</td>
<td>Updated IVM Insurance Upload narrative</td>
<td>IVM*2*111</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>9/25/06</td>
<td>Updated Packagement Management section, Insurance Upload narrative</td>
<td>IVM*2*111</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>10/2/06</td>
<td>Updated Packagement Management section</td>
<td>IVM*2*111</td>
<td><p>PM: REDACTED</p>
<p>Auth: Terry Kopp</p></td>
</tr>
<tr class="even">
<td>10/18/2006</td>
<td>Updated IVM Insurance Upload narrative based on feedback</td>
<td>IVM*2*111</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>10/18/2006</td>
<td>Updated document footers to reflect correct release month and patch number</td>
<td>IVM*2*111</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>4/6/07</td>
<td>Enrollment VistA Changes Release 2 (EVC R2) - Updated Demographics Upload option</td>
<td>IVM*2*115</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>4/6/07</td>
<td>Enrollment VistA Changes Release 2 (EVC R2) - Updated IVM Address Change Log Report option narrative</td>
<td>IVM*2*115</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>4/13/07</td>
<td>Enrollment VistA Changes Release 2 (EVC R2) - Updated IVM Address Change Log Report option Detailed Report Example</td>
<td>IVM*2*115</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>6/07/08</td>
<td>Enrollment VistA Changes Release 2 (EVC R2) - Updated Demographics Upload option</td>
<td>IVM*2*115</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>6/27/08</td>
<td>Enrollment VistA Changes Release 2 (EVC R2) - Updated Demographics Upload option formatting</td>
<td>IVM*2*115</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>4/7/09</td>
<td>Enrollment VistA Changes Release 2 (EVC R2) – Deleted IVM - DEMOGRAPHIC UPLOAD for IVMpatient electronic mail notifications example from Appendix A. This bulletin will no longer be generated when VistA receives updates from the ESR system.</td>
<td>IVM*2*140</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>9/22/09</td>
<td>ESR 3.1/VOA – Updated IVM Transmission Error Processing Option. Updated IVM UPLOAD INSURANCE screen.</td>
<td>IVM*2*121</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>5/18/10</td>
<td>Marked as “obsolete” the entire <em>SSN Upload</em> section. This section will be removed for the next patch update. Additional Address fields added to the <em>Demographics Upload</em> section of the <em>IVM Upload Menu</em>.</td>
<td>IVM*2*121</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>7/5/2011</td>
<td>Updated new Date of Death functionality in the IVM Upload/ Demographics Upload section.</td>
<td>IVM*2*148</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>7/6/2011</td>
<td><p>Page 1, under User/Interactive Functions, 1<sup>st</sup> bullet:</p>
<p>Updated wording to:</p>
<p>“View/verify patient demographic and insurance information.”</p>
<p>Page 17, IVM Upload Menu</p>
<p>Removed wording: “The crossed through text below is obsolete and will be removed from the next release of this manual.”</p></td>
<td>IVM*2*148</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>7/24/2012</td>
<td>IVM*2.0*152 – Permanent Address Verification Changes – ESR 3.8. Added Residence Number Change fields to list of fields in the Demographic Upload</td>
<td>IVM*2*152</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED/ REDACTED</p></td>
</tr>
<tr class="odd">
<td>1/8/2013</td>
<td><p>IVM*2.0*152 – Permanent Address Verification Changes – ESR 3.8.</p>
<p>Updated footer date to December 2012 release date.</p></td>
<td>IVM*2*152</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>11/6/2017</td>
<td><p>IVM*2.0*P167 – Disable Home Phone data elements in IVM Demographics Upload Tool and upload them directly to Patient (#2) File: The following fields were removed from the PATIENT File (#2) table on page 5:</p>
<p>PHONE NUMBER [RESIDENCE] (#.131)</p>
<p>RESIDENCE NUMBER CHANGE DT/TM (#.1321)</p>
<p>RESIDENCE NUMBER CHANGE SITE (#.1323)</p>
<p>RESIDENCE NUMBER CHANGE SOURCE (#.1322).</p>
<p>Updated information related to phone number upload in IVM Upload Menu/Demographic Upload/Introduction (page 6).</p></td>
<td>IVM*2*167</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>12/5/2018</td>
<td>IVM*2.0*164 – New data element "Coding Accuracy Support System (CASS) Certified" added to Demographic Upload Utility (pages 5, 10, and 31).</td>
<td>IVM*2*164</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="even">
<td>01/17/2018</td>
<td><p>IVM*2.0*177 – Auto Upload Permanent Mailing Address: Removed “Uploading Address Information” paragraphs from IVM Upload Menu – Demographic Upload Section; removed address fields from uploadable fields table (page 5); added explanation of auto upload functionality in IVM*2.0*177 (pages 6 and 14); updated IVM Upload Menu</p>
<p>Demographics Upload Example (page 8).</p></td>
<td>IVM*2*177</td>
<td><p>PM: REDACTED</p>
<p>Auth: REDACTED</p></td>
</tr>
<tr class="odd">
<td>08/10/2020</td>
<td>IVM*2.0*193 – Added foreign address fields to IVM Upload Menu – Demographics Upload data table (page. 5).</td>
<td>IVM*2*193</td>
<td><p>PM: REDACTED</p>
<p>Auth: Liberty ITS TW</p></td>
</tr>
<tr class="even">
<td>09/23/2021</td>
<td>IVM*2.0*201 – Changed “Permanent Mailing Address” to “Mailing Address” (pages 6 and 16).</td>
<td>IVM*2*201</td>
<td><p>PM: REDACTED</p>
<p>Auth: Liberty ITS TW</p></td>
</tr>
</tbody>
</table>
Table of Contents

# # Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Public Law 101-508 permits the Department of Veterans Affairs (VA) to verify income data with the Internal Revenue Service (IRS) and Social Security Administration (SSA) for veterans receiving VA health care services whose eligibility for medical care is based on income. The Income Verification Match (IVM) process for Veterans Health Administration (VHA) medical facilities is centralized and performed at the HEC in Atlanta, Ga.

## Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IVM Version 2.0 provides all of the functionality required to complete the eligibility verification process. This primarily involves electronically receiving the revised VA Form 10-10F from the HEC and automatically filing the updated test in the V*IST*A Means Test module.

### User Interactive Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- View/verify patient demographic and insurance information.
- Upload verified data
- View billing/collection and Means Test activity
- Configure, monitor, and purge the IVM system

### Non-interactive Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Exchange of data, on an ad-hoc basis, between your facility and the HEC via electronic transmissions
- Scheduled transmission to the HEC of all Means Tests meeting IVM criteria via the Nightly Background Job, and IVM-related billing and collections activity

## Integration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IVM V. 2.0 provides functionality that impacts Registration, Medical Care Cost Recovery (MCCR), and IRM staff at your facility. It is highly integrated with the following packages.

### Patient Information Management System (PIMS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- PIMS demographic, Means Test, and income information is sent to the HEC
- Means Test and demographic information verified by the HEC is uploaded into PIMS files

### Integrated Billing (IB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Patient insurance information is transmitted to the HEC
- Means Test charges are created in IB for patients who become MT Copay Required when a verified Means Test from IVM is transmitted to the facility
- Insurance information identified by IVM is uploaded into IB files
- IB provides billing and collections information, for billings resulting from IVM activity, that is transmitted back to the HEC

### Health Level 7 (HL7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Provides the foundation for all communications between your facility and the HEC

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Manual                                              | Description                                                                          |
|---------------------------------------------------------|------------------------------------------------------------------------------------------|
| IVM V. 2.0 Technical Manual (includes Security section) | Technical and security information regarding operation and maintenance of the IVM system |
| IVM V. 2.0 Release Notes                                | New features and functions of the V. 2.0 software                                        |
| IVM V. 2.0 Installation Guide                           | Information necessary to install the software                                            |

# Package Management 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Means Tests that meet the IVM criteria and billing/collections information for IVM-related bills are transmitted automatically to the HEC each evening during the nightly background job. Means Tests that have been verified by the HEC and transmitted back to the facility are automatically filed into V*IST*A upon receipt.

There are two parameters included with the IVM software. These parameters, which can be edited through the IVM Parameter Enter/Edit option (by those who hold the IVM SYS security key), control whether notification messages are sent to the IVM MESSAGES mail group when demographic information is received from the HEC. If no entry is made, the default action is to generate the messages. This option may be used to inactivate the messages.

Per VHA Directive 2004-038, Modifications to VHA Class I Software, the third line of routines that are restricted or prohibited from being locally modified should be modified (as they are patched or enhanced) to read as follows:

“Per VHA Directive 2004-038, this routine should not be modified.”

# Using the Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## IVM Upload Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Demographics Upload 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ivm-version-2-user-manual/002.png) The Demographics Upload option is locked with the IVM UPLOAD security key.

Introduction

As part of the Income Verification Match process, patient demographic information is returned to VAMCs. During the course of verifying a Means Test, HEC Contact Representatives may determine that certain patient demographic and eligibility information has changed. The HEC may electronically transmit these changes to the VAMCs in the ORU~Z05 Demographic Data Transmission message. These demographic elements are classified as either UPLOADABLE (elements can be automatically uploaded to the PATIENT File \[#2\] using this option) or NON-UPLOADABLE (data or patient record is corrupt; these elements cannot be automatically uploaded to the PATIENT File \[#2\] using this option).

UPLOADABLE demographic elements will be compared to the patient demographic elements that are currently on file in V*IST*A and displayed to the user via the Demographics Upload \[IVM UPLOAD DEM\] option. This option allows the user to review these elements and choose to either upload or delete them.

NON-UPLOADABLE demographic elements will be compared to the patient demographic elements that are currently on file in V*IST*A and displayed to the user via the Demographics Upload option. This demographic information is provided to the VAMC for informational purposes only. This option allows the user to review these elements, but not automatically load them into V*IST*A. These NON-UPLOADABLE elements must be entered manually via the Load/Edit Patient Data or Register a Patient options in the PIMS Registration Menu. Be sure to verify that the data is accurate before entering it manually.

*IVM Upload Menu*

Demographics Upload

Introduction, continued

Data in the following PATIENT File (#2) fields can be uploaded when using this option.

| Field Name                 | Field Number |
|--------------------------------|------------------|
| CLAIM FOLDER LOCATION          | (#.314)          |
| CLAIM FOLDER NUMBER            | (#.313)          |
| D-COUNTRY                      | (#.34012)        |
| D-POSTAL CODE                  | (#.34014)        |
| D-PROVINCE                     | (#.34013)        |
| DATE MEDICAID LAST ASKED?      | (#.382)          |
| DATE OF BIRTH                  | (#.03)           |
| \* DATE OF DEATH               | (#.351)          |
| \* DATE OF DEATH LAST UPDATED  | (#.354)          |
| DATE RULED INCOMPETENT (VA)    | (#.291)          |
| E-COUNTRY                      | (#.3306)         |
| E-POSTAL CODE                  | (#.3308)         |
| E-PROVINCE                     | (#.3307)         |
| E2-COUNTRY                     | (#.331012)       |
| E2-POSTAL CODE                 | (#.331014)       |
| E2- PROVINCE                   | (#.331013)       |
| ELIGIBILITY STATUS             | (#.3611)         |
| ELIGIBILITY STATUS DATE        | (#.3612)         |
| ELIGIBILITY VERIF. METHOD      | (#.3615)         |
| ELIGIBLE FOR MEDICAID?         | (#.381)          |
| GUARDIAN (VA)                  | (#.2912)         |
| INSTITUTION (VA)               | (#.2911)         |
| K-COUNTRY                      | (#.221)          |
| K-POSTAL CODE                  | (#.223)          |
| K-PROVINCE                     | (#.222)          |
| K2-COUNTRY                     | (#.2101)         |
| K2-POSTAL CODE                 | (#.2103)         |
| K2-PROVINCE                    | (#.2102)         |
| PHONE (VA)                     | (#.2919)         |
| PRIMARY ELIGIBILITY CODE       | (#.361)          |
| RATED INCOMPETENT?             | (#.293)          |
| RELATIONSHIP (VA)              | (#.2913)         |
| SEX                            | (#.02)           |
| \* SOURCE OF NOTIFICATION      | (#.353)          |
| STREET ADDRESS \[LINE 1\] (VA) | (#.2914)         |
| STREET ADDRESS \[LINE 2\] (VA) | (#.2915)         |
| ZIP (VA)                       | (#.2918)         |

\*Date of Death-related fields.

*IVM Upload Menu*

Demographics Upload

Introduction, continued

With the release of IVM\*2.0\*177, all Mailing Address updates are stored directly to the PATIENT File (#2). Therefore, within 14 days of installation at the site, the IVM Upload Menu Demographics Upload will not display patient address fields.

Entering/Uploading Date of Death Information

During data entry, the date of death must be entered in one of the following formats:

- Year only
- Month and year
- Month, day, and year

If you choose not to upload date of death information from the HEC, a mail message will be sent to the DGEN ELIGIBILITY ALERT mail group to notify them that they must contact the HEC with a reason for not accepting the data. When you upload data in one of the date of death fields (Date of Death, Source of Notification, and Date of Death Last Updated), the data in all three of these fields will upload.

The date of death sent from HEC will be ignored by VistA when the date of death value from HEC (in the ORU~Z05) matches the date of death value at the VAMC. Date of death will automatically be deleted from the PATIENT File (#2) when the ORU~Z05 from the HEC contains a date of death deletion.

When any message qualifies for an automatic upload, the process will search the Demographics Upload option for any date of death entries, and take the following action on all patient records

- If the record contains date of death-related field data only, the data will be deleted and the record will be removed from the Demographics Upload option.
- If the record contains a combination of date of death-related field data plus any other field data, only the date of death-related field data will be removed, and the record will remain in the Demographics Upload option.
- If the date of death field is empty (null) and the data received from HEC contains both a date of death and Source of Notification equal to "Death Certificate on File," then the data is uploaded to VistA.
- If the date of death field is already populated in VistA and date of death data is received from HEC, the data from HEC is ignored and VistA will not create an entry in the IVM Demographic Upload tool.

List Manager

This option uses the ListManager utility which provides a series of screens that display lists of patients whose demographics information has changed, and can be viewed, uploaded, or rejected using the actions at the bottom of the screens.

Data that is on file at the VAMC is displayed under the column heading “DHCP Field Value”. Data coming from the HEC in an ORU~Z05 message is displayed under the column heading “IVM Field Value”.

In addition to the generic List Manager actions described in Appendix B of this manual, the following actions are also available when using this option:

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 27%" />
<col style="width: 56%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Short Name</strong></td>
<td><strong>Full Name</strong></td>
<td><strong>Brief Description</strong></td>
</tr>
<tr class="even">
<td colspan="3"><strong>From the IVM Demographic Screen</strong></td>
</tr>
<tr class="odd">
<td>DU</td>
<td>Display Uploadable</td>
<td><ul>
<li><p>Displays uploadable data for the selected patient on the Uploadable Demographics screen</p></li>
<li><p>Provides List Manager actions to upload or delete demographic data</p></li>
</ul></td>
</tr>
<tr class="even">
<td>VN</td>
<td>View Non Uploadable</td>
<td><ul>
<li><p>Displays non-uploadable data for the selected patient on the Uploadable Demographics screen</p></li>
<li><p>Provides List Manager action to delete demographic data</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>EH</td>
<td>Extended Help</td>
<td><ul>
<li><p>Takes you to the extended help screen</p></li>
<li><p>Provides definitions of uploadable vs. non-uploadable data</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="3"><strong>From the Uploadable Demographics Screen</strong></td>
</tr>
<tr class="odd">
<td>UF</td>
<td>Upload Demographic Fields</td>
<td>Uploads data elements to the PATIENT File(#2)</td>
</tr>
<tr class="even">
<td>DF</td>
<td>Delete Demographic Fields</td>
<td>Deletes data elements from the list on the Uploadable Demographics Screen</td>
</tr>
<tr class="odd">
<td colspan="3"><strong>From the Non-Uploadable Demographics Screen</strong></td>
</tr>
<tr class="even">
<td>DF</td>
<td>Delete Demographic Fields</td>
<td>Deletes data elements from the list on the Non-Uploadable Demographics Screen</td>
</tr>
</tbody>
</table>

  
*IVM Upload Menu *

Demographics Upload

Example

The IVM Demographic Upload screen displays a list of patients whose demographics information has changed and indicates whether there is uploadable/non-uploadable information.

<u>Uploadable Demographics Oct 19, 2018@16:18:28 Page: 1 of 1</u>

Patient: REDACTED,DECIMAL (8666) Uploadable Demographic Fields

<u>DHCP Field Name DHCP Field Value IVM Field Value</u>

1 PHONE NUMBER \[WORK\] 9726058782 (972)605-8799

Enter ?? for more actions

DU Display Uploadable VN View Non Uploadable EH Extended Help

Select Action: Quit//

*IVM Upload Menu*

### Insurance Upload 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ivm-version-2-user-manual/003.png) The Insurance Upload option is locked with the IVM UPLOAD security key.

Introduction

When patient insurance information is transmitted from the HEC to the VAMC(s), it is filed in the IVM PATIENT File (#301.5) and automatically moved to the INSURANCE BUFFER File (#355.33), without user intervention, unless an exception occurs.

This option lists only those patient insurance records received from the HEC that could not be automatically moved to the INSURANCE BUFFER File (#355.33) and require further action.

Once action has been taken on the data, a confirmation message is automatically transmitted to the HEC. The message includes the decision made at the site and, if the information was rejected, the reason the data was not uploaded.

If V*<span class="smallcaps">ist</span>*A or IVM records show a date of death on a patient, it is indicated on the screen by an asterisk. If that patient is selected, a message is displayed indicating that a date of death has been reported either by the HEC or V*<span class="smallcaps">ist</span>*A.

*IVM Upload Menu*

Insurance Upload

Example

Example 1 – Transfer IVM Insurance Policy to Insurance Module

<u>IVM INSURANCE UPLOAD Jul 28, 1994 16:24:50 Page: 1 of 1</u>

The HEC has identified insurance for the following patients:

(\*) - Indicates Death Reported Act

<u>Patient Name SSN Ins Insurance Carrier Subscriber ID</u>

1 IVMPATIENT,FIVE 000-56-0730 NO ABC INSURANCE COMPANY DFS9732

2 IVMPATIENT,SIX 000-98-8887 NO XYZ INSURANCE COMPANY 029876587

3 IVMPATIENT,SEVEN 000-77-3882 YES 123 INSURANCE COMPANY 2838B34H

4 \*IVMPATIENT,EIGHT 000-26-9525 YES INSURANCE INSURANCE COMPA 021670999

5 IVMPATIENT,NINE 000-45-6992 YES BARRY BARRY INSURANCE 00123ER45

6 IVMPATIENT,TEN 000-01-0111 NO ABC INSURANCE COMPANY DFS7865

Enter ?? for more actions

DE Display Entry EH Extended Help

Select Action: Quit// de=4 Display Entry

'Date of Death' reported for this patient in DHCP as JUN 23, 1994.

Press RETURN to continue: \<RET\>

INSURANCE POLICIES CURRENTLY ON FILE

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Insurance Co. Subscriber ID Group Holder Effective Expires

===========================================================================

No Insurance Information

INSURANCE POLICY RECEIVED FROM the HEC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Company: INSURANCE COMPANY Effective Date: FEB 3, 1992

Phone \#: (999)555-1212 Expiration Date: OCT 10, 1994

Address: Subscriber ID: 000670999

123 Anywhere St. Policy Holder: SELF

\<insurance addr line \#2\>

\<insurance addr line \#3\> Group Name: UMBRELLA GRP

Mytown, Mystate 99999 Group Number: 102

Pre-Cert. Req?: NO

Name of Insured: IVMPATIENT, EIGHT Plan Type: HEALTH MAINTENANCE ORGAN

Press RETURN to continue or '^' to return to display screen: \<RET\>*IVM Upload Menu*

Insurance Upload

Example, cont.

Select one of the following:

1 Transfer IVM Insurance Policy to Insurance Module

2 Purge IVM Insurance Policy

3 Return to Display Screen

Select Action: ??

Entering '1' at this prompt will allow the user to upload the Insurance Policy

that was received from the HEC. Entering '2' at this prompt will allow

the user to delete the Insurance Policy that was received from the HEC

Entering '3' or '^' will abort this action.

Select one of the following:

1 Transfer IVM Insurance Policy to Insurance Module

2 Purge IVM Insurance Policy

3 Return to Display Screen

Select Action: 1 Transfer IVM Insurance Policy to Insurance Module

Transferring HEC’s insurance policy to insurance module completed.

Press RETURN to continue: \<RET\>  
*IVM Upload Menu*

Insurance Upload

Example, cont.

Example 2 - Purge Insurance Policy

<u>IVM INSURANCE UPLOAD Jul 28, 1994 16:24:50 Page: 1 of 1</u>

the HEC has identified insurance for the following patients:

(\*) - Indicates Death Reported Act

<u>Patient Name SSN Ins Insurance Carrier Subscriber ID</u>

1 IVMPATIENT,FIVE 000-56-0730 NO ABC INSURANCE COMPANY DFS9732

2 IVMPATIENT,SIX 000-98-8887 NO XYZ INSURANCE COMPANY 029876587

3 IVMPATIENT,SEVEN 000-77-3882 YES 123 INSURANCE COMPANY 2838B34H

4 \*IVMPATIENT,EIGHT 000-26-9525 YES INSURANCE INSURANCE COMPA 021670999

5 IVMPATIENT,NINE 000-45-6992 YES BARRY BARRY INSURANCE 00123ER45

6 IVMPATIENT,TEN 000-01-0111 NO ABC INSURANCE COMPANY DFS7865

Enter ?? for more actions

DE Display Entry EH Extended Help

Select Action: Quit// de=4 Display Entry

'Date of Death' reported for this patient in DHCP as JUN 23, 1994.

Press RETURN to continue: \<RET\>

INSURANCE POLICIES CURRENTLY ON FILE

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Insurance Co. Subscriber ID Group Holder Effective Expires

===========================================================================

No Insurance Information

INSURANCE POLICY RECEIVED FROM the HEC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Company: INSURANCE COMPANY Effective Date: FEB 3, 1992

Phone \#: (999)555-1212 Expiration Date: OCT 10, 1994

Address: Subscriber ID: 000670999

123 Anywhere St. Policy Holder: SELF

\<insurance addr line \#2\>

\<insurance addr line \#3\> Group Name: UMBRELLA GRP

Mytown, Mystate 99999 Group Number: 102

Pre-Cert. Req?: NO

Name of Insured: IVMPATIENT, EIGHT Plan Type: HEALTH MAINTENANCE ORGAN

Press RETURN to continue or '^' to return to display screen: \<RET\>*IVM Upload Menu*

Insurance Upload

Example, cont.

Select one of the following:

1 Transfer IVM Insurance Policy to Insurance Module

2 Purge IVM Insurance Policy

3 Return to Display Screen

Select Action: 2 Purge IVM Insurance Policy

The 'Purge IVM Insurance Policy' action has been selected.

This action will cause the insurance information which has been

received from the HEC to be deleted from the system!

Please select a reason for purging the IVM insurance information.

Select reason for purging: ??

CHOOSE FROM:

1 ALREADY HAVE INSURANCE POLICY

2 DATA APPEARS TO BE INCORRECT

3 INSURANCE COMPANY CLOSED

4 POLICY PLAN TYPE IS HMO

5 POLICY PLAN TYPE IS PPO

6 POLICY COVERAGE EXPIRED

7 POLICY BENEFITS FULLY USED

8 BENEFITS NOT AVAILABLE

9 COVERAGE FOR SPOUSE ONLY

Select reason for purging: 1 ALREADY HAVE INSURANCE POLICY

Are you sure that you want to purge IVM insurance data? NO// y YES

Purging the 'Insurance Policy' received from IVM... completed.

Press RETURN to continue: \<RET\>  
*IVM Upload Menu*

Insurance Upload

Example, cont.

<u>IVM INSURANCE UPLOAD Jul 28, 1994 16:24:50 Page: 1 of 1</u>

the HEC has identified insurance for the following patients:

(\*) - Indicates Death Reported Act

<u>Patient Name SSN Ins Insurance Carrier Subscriber ID</u>

1 IVMPATIENT,FIVE 000-56-0730 NO ABC INSURANCE COMPANY DFS9732

2 IVMPATIENT,SIX 000-98-8887 NO XYZ INSURANCE COMPANY 029876587

3 IVMPATIENT,SEVEN 000-77-3882 YES 123 INSURANCE COMPANY 2838B34H

4 \*IVMPATIENT,EIGHT 000-26-9525 YES INSURANCE INSURANCE COMPA 021670999

5 IVMPATIENT,NINE 000-45-6992 YES BARRY BARRY INSURANCE 00123ER45

Enter ?? for more actions

DE Display Entry EH Extended Help

Select Action: Quit//

  
*IVM Upload Menu*

### Please Note:SSN Upload is no longer used in VistA. The Enrollment System Redesign HEC Legacy Replacement application now does it automatically.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*IVM Upload Menu*

### IVM Address Updates Pending Review 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option generates the IVM Automatic Address Upload Report. The report displays the addresses that will be automatically uploaded to the VAMC if no other action is taken within 14 days from the date they are received at the VAMC.

This report will be removed in a future release. With the release of IVM\*2.0\*177, all Mailing Address updates are stored directly to the PATIENT file. Within 14 days of installation at the site, the IVM Upload Menu Demographics Upload will not contain any addresses, so the IVM Address Updates Pending Review report will no longer return any patient rows.

The only prompt asks for a device. The output includes the following information:

- Name of the report
- Date the report was generated
- Page number
- Date the update will be automatically uploaded to the VAMC if no other action is taken
- Date the update was received at the VAMC
- Patient’s SSN
- Patient’s name

Example

IVM AUTOMATIC ADDRESS UPLOAD RPT JUN 11,2003 Page: 1

========================================================================

Auto-Upload Date Date Received SSN Patient Name

---------------- ------------- --------- ------------

Jun 23, 2003 Jun 09, 2003 000168014 IVMpatient,seventeen

Jun 24, 2003 Jun 10, 2003 000168014 IVMpatient,seventeen

\<\<END OF REPORT\>\>

## IVM Output Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Billing Transmission Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option generates a report of all IVM-related billing and collection activity that has been transmitted to the HEC. Information for each third party claim or Means Test charge is listed along with the date that the last transmission was sent to IVM. The report will also indicate whether any further transmissions will be sent to IVM.

![](ivm-version-2-user-manual/004.png)

Data from IB files are included in this report.

Example

This report will list all billing activity which has been, or will be,

transmitted to the IVM Center. This includes Means Test charges for

patients who have changed categories due to IVM-verified Means Tests,

as well as claims to insurance companies for patients who have

insurance policies identified by the IVM Center.

Please note that this output requires 132 columns. This report may not

run very quickly so you might choose to queue the report to a printer.

DEVICE: HOME// \<RET\> Decnet RIGHT MARGIN: 80// 132

Run Date: 08/11/94 8:19 am IVM BILLING TRANSMISSION REPORT Page: 1

===================================================================================================================

Bill Date Amt Amt Date Last

Patient Name SSN Ref \# Clsf Bill Type Bill From - To Generated Billed Coll Trans Tran

===================================================================================================================

IVMpatient,sev 000-03-3211 5003082 O INS CLAIM 05/13/94 05/13/94 06/29/94 356.00 0.00 07/14/94 NO

IVMpatient,eig 000-89-4444 5003086 O COPAYMENT 12/10/93 12/10/93 36.00 --N/A-- Not Sent NO

IVMpatient,nin 000-70-9989 5003080 I PER DIEM 04/29/94 06/27/94 06/29/94 600.00 --N/A-- 07/14/94 YES

5003081 I COPAYMENT 04/29/94 04/29/94 06/29/94 696.00 --N/A-- 07/14/94 YES

IVMpatient,ten 000-80-1887 5003088 O COPAYMENT 04/16/94 04/16/94 36.00 --N/A-- Not Sent NO

  
*IVM Output Menu*

### IVM Case Inquiry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option allows you to review the status of any Means Test or Co-Pay Exemption Test submitted to the HEC for verification. All Means Test and billing/collection transmissions for the case are displayed. Any uploadable data associated with the case is indicated.

![](ivm-version-2-user-manual/005.png)

The data used for this report is from the Means Test module of the PIMS software.

Example

Select PATIENT NAME: IVMpatient,test 02-08-52 000456110 NO

NSC VETERAN

\>\>\>\> Case Record is for Income Year 1993 \<\<\<\<

DEVICE: HOME// \<RET\> Decnet RIGHT MARGIN: 80// \<RET\>

IVM Case Inquiry Aug 11, 1994@08:24:17 Page: 1

--------------------------------------------------------------------------

Name: IVMpatient,test Awaiting Trans: NO

SSN: 000-45-6110 Case Status: CLOSED

Inc Year: 1993 Full Transmission Sent: 07/14/94

MT Date: 07/11/94 (MT COPAY EXEMPT)

==========================================================================

--- T H I S C A S E R E C O R D H A S B E E N C L O S E D ---

Closure Reason: CASE WAS NOT VERIFIED

Closure Source: IVM CENTER

Closure Date: Jul 19, 1994@15:29:02

==========================================================================

Means Test Transmission History:

Transmitted As

Trans Date/Time Status MT Cat Had Ins?

------------------------------------------------------------------------

Jul 14, 1994@09:29:32 RECEIVED MT COPAY EXEMPT NO

Jul 19, 1994@12:27:34 RECEIVED MT COPAY EXEMPT NO

*IVM Output Menu*

### Means Test Comparison Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This management report provides a summary of all Means Tests for two consecutive years for veterans who are MT Copay Exempt or MT Copay Required. It lists the total number of veterans in each category, the number of veterans who have changed Means Test category over the two year period, the number of new Means Tests (veterans Means Tested in the second year only) and the number of "non-returns" (veterans Means Tested in the first year only). A detailed report listing each veteran with both years' Means Test category is also available.

This report could be run regularly to judge the shift of veterans from the mandatory to discretionary category, and to estimate the number of potential cases that will be referred to the HEC for verification.

![](ivm-version-2-user-manual/006.png)

All data used for this report is from PIMS files.

Example

IVM MEANS TEST COMPARISON REPORT

This report will be used to analyze consecutive years' Means Test data

(i.e. 1991-1992). Please enter the first year for the two year period

which you would like to analyze.

Enter first means test YEAR (1986 - 1993): 1992 (1992)

Means Test YEAR 1: 1992

Means Test YEAR 2: 1993

Would you like to print patient data? NO// y YES

> **NOTE:** The output is designed to use 80 columns.

DEVICE: HOME// \<RET\> Decnet RIGHT MARGIN: 80// \<RET\>*IVM Output Menu*

Means Test Comparison Report

Example, cont.

JUL 8,1994 PAGE: 1

M E A N S T E S T C O M P A R I S O N R E P O R T

FOR YEARS: 1992 AND 1993

==============================================================================

PATIENT SSN MEANS TEST MEANS TEST

CATEGORY CATEGORY

1992 1993

IVMpatient,eleven 000-01-0101 A C

IVMpatient,twelve 000-66-9999 C

IVMpatient,thirteen 000-93-8276 A

IVMpatient,five 000-57-4321 A

IVMpatient,fourteen 000-98-4587 A

IVMpatient,fifteen 000-10-9937 A A

IVMpatient,sixteen 000-09-7714 C

JUL 8,1994 PAGE: 20

M E A N S T E S T C O M P A R I S O N R E P O R T

FOR YEARS: 1992 AND 1993

==============================================================================

SUMMARY OF MEANS TESTS FOR YEAR 1992

====================================

TOTAL CAT A: 29

TOTAL CAT C: 77

TOTAL MEANS TESTS: 106

SUMMARY OF MEANS TESTS FOR YEAR 1993

====================================

TOTAL CAT A: 36

TOTAL CAT C: 45

TOTAL MEANS TESTS: 81

TOTAL NON-RETURNS FROM 1992 TO 1993: 89

TOTAL NEW MEANS TESTS FROM 1992 TO 1993: 64

TOTAL PATIENTS WHOSE CATEGORY CHANGED FROM A TO C: 2

TOTAL PATIENTS WHOSE CATEGORY CHANGED FROM C TO A: 3

IVM Output Menu

### IVM Address Change Log Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

This option generates a report of updates made to *prior* patient addresses within a specified date range. The report may take a long time to generate; you might want to queue it to print at a later time. You can select from the following report types:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 25%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Report Type</strong></th>
<th><strong>Description</strong></th>
<th><strong>About the Report</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Summary</td>
<td>Displays all patients who had address changes in a user-selected 90-day period</td>
<td><ul>
<li><p>You can choose to sort by patient name or SSN.</p></li>
<li><p>You must enter an ending date of a 90-day period.</p></li>
<li><p>The output returns all entries in the IVM ADDRESS CHANGE LOG file (#301.7) where the date of the ADDRESS CHANGE DT/TM field (#.01) is within the 90-day period.</p></li>
<li><p>For each patient, the output includes:</p>
<ul>
<li><blockquote>
<p>Patient’s SSN</p>
</blockquote></li>
<li><blockquote>
<p>Patient’s name</p>
</blockquote></li>
<li><blockquote>
<p>Date and time of the last address update</p>
</blockquote></li>
<li><blockquote>
<p>The number of entries in the IVM ADDRESS CHANGE LOG file (#301.7)</p>
</blockquote></li>
</ul></li>
</ul>
<ul>
<li><p>At the end of the report, you will see the total number of records found meeting the criteria.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Detailed</td>
<td><p>Displays all previous addresses for an individual patient in a user-selected 90-day period</p>
<p>Note: The report does <em><strong>not</strong></em> list <em><strong>current</strong></em> addresses.</p></td>
<td><ul>
<li><p>You must select a patient.</p></li>
<li><p>You must enter an ending date of a 90-day period.</p></li>
<li><p>The output returns all entries in the IVM ADDRESS CHANGE LOG file (#301.7) where the date of the ADDRESS CHANGE DT/TM field (#.01) is within the 90-day period for the patient you selected.</p></li>
<li><p>The output includes:</p>
<ul>
<li><blockquote>
<p>Patient’s SSN</p>
</blockquote></li>
<li><blockquote>
<p>Patient’s name</p>
</blockquote></li>
<li><blockquote>
<p>Date of address update</p>
</blockquote></li>
<li><blockquote>
<p>Previous address</p>
</blockquote></li>
<li><blockquote>
<p>Bad Address Indicator (BAI)</p>
</blockquote></li>
<li><blockquote>
<p>Previous address change source</p>
</blockquote></li>
<li><blockquote>
<p>Previous address change site</p>
</blockquote></li>
</ul></li>
<li><p>At the end of the report, you will see the total number of records found meeting the criteria.</p></li>
</ul></td>
</tr>
</tbody>
</table>

![](ivm-version-2-user-manual/007.png)

The data used for this report is from the IVM ADDRESS CHANGE LOG file (#301.7).

  
IVM Output Menu

IVM Address Change Log Report

Example - Summary

IVM ADDRESS CHANGE LOG REPORT Page: 1

Jan 10, 2006 THRU Apr 10, 2006

SSN NAME LAST UPDATED \# ENTRIES

--- ---- ------------ ---------

000123214 IVMPATIENT,ONE Feb 28, 2006@11:18:19 15

000666322 IVMPATIENT,TWO Jan 31, 2006@15:13:13 2

000723555 IVMPATIENT,THREE Feb 23, 2006@19:42:21 2

000705497 IVMPATIENT,FOUR Feb 01, 2006@11:25:51 3

Total records found meeting criteria: 4

Example – Detailed

IVM ADDRESS CHANGE LOG REPORT Page: 1

Jan 11, 2006 THRU Apr 11, 2006

 

SSN NAME CHANGE DATE PRIOR ADDRESS

--- ---- ----------- --------------

000705497 IVMPATIENT,FOUR Jan 27, 2006 6222 ROYAL FOREST BLVD

COLUMBUS, OH 43202

SOURCE: VAMC

SITE: PHOENIX-RO

BAI: UNDELIVERABLE

000705497 IVMPATIENT,FOUR Jan 31, 2006 438 ROYAL FOREST BLVD

COLUMBUS, OH 43212

SOURCE: VAMC

SITE: PHOENIX-RO

000705497 IVMPATIENT,FOUR Feb 01, 2006 438 ROYAL FOREST BLVD

COLUMBUS, OH 43212

SOURCE: VAMC

SITE: PHOENIX-RO

Total records found meeting criteria: 3

## IVM System Manager's Menu 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IVM Parameter Enter/Edit 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ivm-version-2-user-manual/008.png) This option is locked with the IVM SYS security key.

Introduction

The IVM parameters control whether notification messages are sent to the IVM MESSAGES mail group when SSN and demographics information is received from the HEC. If no entry is made, the messages are generated.

Please refer to Appendix A of this manual for sample mail messages.

Example

IVM Parameter Enter/Edit

SUPPRESS SSN UPLOAD MESSAGE: ?

Enter 1 to suppress notification to facility that updated SSN data has

been received from the IVM Center. Enter 0 if facility is to be notified.

Default is 0.

CHOOSE FROM:

1 SUPPRESS MESSAGE

0 DON'T SUPPRESS MESSAGE

SUPPRESS SSN UPLOAD MESSAGE: 0 DON'T SUPPRESS MESSAGE

SUPPRESS DEMOGRAPHIC MESSAGE: 0 DON'T SUPPRESS MESSAGE

*IVM System Manager's Menu*

### Purge IVM Transmissions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ivm-version-2-user-manual/009.png) This option is locked with the IVM SYS security key.

Introduction

This option allows IRM staff to purge entries from the IVM TRANSMISSION LOG File (#301.6) that are associated with closed cases (entries in the IVM PATIENT File \[#301.5\]) from the previous Means Test year.

A notification is sent to the user indicating that the purge has completed, the total number of records checked, number of closed records found, and number of records deleted.

Please refer to Appendix A of this manual for a sample mail message.

Example

This option is used to purge data from the IVM TRANSMISSIONS File (#301.6).

Entries in this file will only be purged for corresponding case records

in the IVM PATIENT File (#301.5) which have been closed.

You may purge transmission records for an entire income year's worth of cases.

However, you must select an income year prior to the year which corresponds

to the current year's Means Tests. Since this year's Means Tests are based

on 1993 income, you must select an income year prior to 1993.

Select the Income Year for which to purge transmissions: 1992 (1992)

Is it okay to queue this job? y YES

Requested Start Time: NOW// \<RET\> (JUL 08, 1994@14:12:53)

This job has been queued. The task number is 20474.

*IVM System Manager's Menu*

### IVM Transmission Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ivm-version-2-user-manual/010.png) This option is locked with the IVM SYS security key.

Introduction

The IVM Transmission Report allows you to analyze the number of Initial or Full transmissions leaving your facility for a specific date or range. The total number of transmissions is broken down by the transmission status:

> *Transmitted* - An attempt has been made to send the transmission to the HEC. The transmission may or may not have left your facility, but it has not been acknowledged by the HEC.

> *Received* - The transmission has been successfully acknowledged by the HEC.

> *In Error* - The transmission has been acknowledged by the HEC as having contained erroneous or invalid data.

> *Re-transmitted* - A transmission with the status of "transmitted" may be retransmitted after three days. At that time, a new transmission record is created. The status of the original transmission is updated to "retransmitted."

The number of multiple transmissions is listed. If more than one transmission for an income case has been sent to the HEC (this would occur if the Means Test or demographics data for the veteran was edited), each successive transmission is considered to be a multiple transmission for a specific income case.

Summary statistics for the number of MT Copay Exempt and MT Copay Required veterans with and without active insurance are provided. A listing of the receipt date and response date for each Master Query received by the facility is also included.

*IVM System Manager's Menu*

IVM Transmission Report

Example

Select one of the following:

1 SINGLE DATE REPORT

2 DATE RANGE REPORT

Enter response: 2 DATE RANGE REPORT

Enter Start DATE: 7/1 (JUL 01, 1994)

Enter End DATE: 8/31 (AUG 31, 1994)

DEVICE: HOME// \<RET\> Decnet RIGHT MARGIN: 80// \<RET\>

=====================================================================

\| INCOME VERIFICATION MATCH - TRANSMISSIONS REPORT \|

\| \|

\|-------------------------------------------------------------------\|

\| DATE PRINTED: AUG 31, 1994 \|

=====================================================================

Date range selected: JUL 01, 1994 to AUG 31, 1994

Total number of days: 62

Total number of transmissions: 248 (4.00/day)

Without Status: 0 In Error: 0

Transmitted: 30 Re-transmitted: 33

Received: 185 Multiple Transmissions: 118 (of 248)

With Insurance Without Insurance

-------------- -----------------

Percentage MT Copay Exempt: 2.82 % 78.84 %

Percentage MT Copay Required: 0.77 % 14.11 %

\*\* M A S T E R Q U E R Y S U M M A R Y \*\*

Query Income Year Date Received Date Responded

----------------- ----------------- -----------------

1992 06/28/94 4:34 pm 06/28/94 11:32 pm

1993 07/19/94 12:35 pm 07/19/94 11:31 pm

## IVM Transmission Error Processing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The Health Eligibility Center may respond to a patient transmission by returning an error message, which means they were unable to process the transmission. The IVM Transmission Error Processing option allows you to work with lists of patients for which error messages were received in a List Manager format. This information was previously viewed through “Erroneous Data Sent to the HEC” mail messages for each individual patient.

The contents of the list are selected by a user-specified date range. The initial display shows the “New” process status and is sorted by patient name. You may use the following actions to make changes to the displayed list.

|                      |                                                                                                                                                                                                                                                                                                                                    |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change Date Range    | Change the date range of the errors being viewed.                                                                                                                                                                                                                                                                                  |
| Change List          | Change the error list being viewed. You may choose to see errors with a status of new, checked, or both.                                                                                                                                                                                                                           |
| Check Error Off List | Changes the selected error with a status of New to a status of Checked. Checked indicates the error has been viewed.                                                                                                                                                                                                               |
| Retransmit Patient   | Sets a flag to retransmit the selected patient. The transmission will take place during the nightly job.                                                                                                                                                                                                                           |
| Sort List            | Choose to sort the error list by patient name, date/time, and or error message acknowledgment received. The system allows the user the ability to change the sort consistency based upon the current functionality. In the event the user selects “no sort criteria”, the system will automatically use current default sort list. |

Example

Select Beginning Date: OCT 07, 1997// \<RET\> (OCT 07, 1997)

Select Ending Date: TODAY// \<RET\> (OCT 21, 1997)

...EXCUSE ME, JUST A MOMENT PLEASE.......

*IVM Transmission Error Processing*Example, cont.

<u>IVM Transmission Errors Oct 21, 1997 08:45:48 Page: 1 of 13</u>

Sort By: Patient Name Date Range: 10/07/97 thru 10/21/97

Error Processing Statuses: New

<u>Patient Name PT ID Date/Time ACK Received Process Status</u>

1 IVMpatient,eighteen 1555 Oct 07, 1997 13:48:29 New

Error: PATIENT NAME INVALID

2 IVMpatient,nineteen 1555 Oct 07, 1997 13:48:30 New

Error: PATIENT NAME INVALID

3 IVMpatient,twenty 1558 Oct 07, 1997 13:48:29 New

Error: PATIENT SSN INVALID

\+ \* = Patient has been flagged for transmission \>\>\>

CD Change Date Range CL Change List SL Sort List

CE Check Error Off List RP Retransmit Patient

Select Action: Next Screen// CE Check Error Off List

Select Transmission Error(s): (1-3): 1

<u>IVM Transmission Errors Oct 21, 1997 08:45:48 Page: 1 of 13</u>

Sort By: Patient Name Date Range: 10/07/97 thru 10/21/97

Error Processing Statuses: New

<u>Patient Name PT ID Date/Time ACK Received Process Status</u>

1 IVMpatient,eighteen 1555 Oct 07, 1997 13:48:29 Checked

Error: PATIENT NAME INVALID

2 IVMpatient,nineteen 1555 Oct 07, 1997 13:48:30 New

Error: PATIENT NAME INVALID

3 IVMpatient,twenty 1558 Oct 07, 1997 13:48:29 New

Error: PATIENT SSN INVALID

\+ \* = Patient has been flagged for transmission \>\>\>

CD Change Date Range CL Change List SL Sort List

CE Check Error Off List RP Retransmit Patient

Select Action: Next Screen//

## IVM Financial Query 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

The IVM Main Menu allows you to manually generate financial queries to the HEC for patients that require updated income Means Test, Copay Test, and Income Screening information. The prompts ask you to select a patient, verify that you want to send a financial query, and if you want to receive notification when a reply is received.

You cannot send a query if

- A query is already pending for the selected patient.
- No financial query is required for the selected patient. (For example, the patient is in Enrollment Priority Group 1.)

Example

This option allows queries to be sent to the Health Eligibility

Center (HEC) for patients that require updated income information.

Select PATIENT NAME: IVMpatient,t IVMpatient,t 3-26-66 105032666

NO NSC VETERAN SH

Enrollment Priority: Category: IN PROCESS End Date:

\*\*\* Patient Requires a Means Test \*\*\*

Patient's Test dated DEC 21,1998 is MT COPAY EXEMPT. The test

date is greater than 365 days old. Please update.

Enter \<RETURN\> to continue.

Financial query queued to be sent to the HEC...

Would you like to send a financial query for this patient? YES//

Do you want to be notified when a query reply is received? YES//

Failure to send query: A FINANCIAL QUERY IS CURRENTLY OPEN OR JUST SENT

# Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary contains terms and their definitions as they relate to the IVM package.
CASS Coding Accuracy Support System, software provided by the United States Postal Service to verify delivery to an address.
MT Copay Exempt veteran A patient who, as a result of Means Testing, is in the mandatory category in regard to eligibility for VA care.
MT Copay Required veteran A patient who, as a result of Means Testing, is in the discretionary category in regard to eligibility for VA care.
full data transmission A complete information profile transmitted to the HEC containing patient demographic, eligibility, Means Test, income, insurance, and enrollment information.
HEC Health Eligibility Center (formerly IVM Center)
HL7 Health Level 7 is an interface specification designed to standardize the way in which health care information is transferred between systems. IVM utilizes the V*IST*A HL7 package to assist in transporting data using this specification.
IRS Internal Revenue Service
IVM Income Verification Match. A program designed to verify income and insurance data reported by the veteran with that received from IRS (Internal Revenue Service), SSA (Social Security Administration), and other sources.
Means Test Eligibility for VA hospital care and nursing home care is divided into two categories - mandatory and discretionary. An income assessment is made to determine whether a non service-connected veteran, who is not in receipt of VA monetary benefits or otherwise exempt from income assessment, is eligible for cost-free VA medical care. This income assessment is known as "Means Testing." Patients whose income is above the defined income levels must agree to make copayments to VA for outpatient and inpatient care rendered.
SSA Social Security Administration
suggested SSN Patient or spouse SSNs returned from SSA as possible matches based on name, sex, and date of birth. These SSNs will be validated by the HEC before being returned to the field facilities.
third party claim When a party other than the patient, such as an insurance company, is billed.
Military Time Conversion Table
> STANDARD MILITARY
> 12:00 MIDNIGHT 2400 HOURS
> 11:00 PM 2300 HOURS
> 10:00 PM 2200 HOURS
> 9:00 PM 2100 HOURS
> 8:00 PM 2000 HOURS
> 7:00 PM 1900 HOURS
> 6:00 PM 1800 HOURS
> 5:00 PM 1700 HOURS
> 4:00 PM 1600 HOURS
> 3:00 PM 1500 HOURS
> 2:00 PM 1400 HOURS
> 1:00 PM 1300 HOURS
> 12:00 NOON 1200 HOURS
> 11:00 AM 1100 HOURS
> 10:00 AM 1000 HOURS
> 9:00 AM 0900 HOURS
> 8:00 AM 0800 HOURS
> 7:00 AM 0700 HOURS
> 6:00 AM 0600 HOURS
> 5:00 AM 0500 HOURS
> 4:00 AM 0400 HOURS
> 3:00 AM 0300 HOURS
> 2:00 AM 0200 HOURS
> 1:00 AM 0100 HOURS

# Appendix A - Sample Mail Messages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following are samples of the types of electronic mail notifications generated by the IVM software. You might also receive messages generated by other V*IST*A software packages, such as the notification generated by PIMS to indicate a changed SSN, or the notification of new insurance sent by IB.

*The patient’s name and last four digits of the SSN have been added to the subject line of some messages with patch number IVM\*2\*3.*

## Completed Purge of IVM Transmission Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: COMPLETED PURGE OF IVM TRANSMISSION RECORDS \[#186481\] 11 Aug 94 08:04 11 Lines

From: INCOME VERIFICATION MATCH PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

---------------------------------------------------------------------------

The purge of data from the IVM TRANSMISSIONS File (#301.6) has completed.

Job Start Date/Time: AUG 11, 1994@08:09:28

Job End Date/Time: AUG 11, 1994@08:19:26

Income Year: 1992

Total number of case file records checked: 2236

Number of closed case records found: 340

Number of IVM TRANSMISSION records deleted: 697

## IVM - Means Test Upload

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: IVM - MEANS TEST UPLOAD \[#117931\] 25 Jul 94 15:33 7 Lines

From: IVM PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

The following error occurred when an Income Verification Match verified

Means Test was being uploaded for the following patient:

NAME: IVMpatient,twenty-three

ID: 000-23-8405

ERROR: Can't find 408.12 record

Subj: IVM - MEANS TEST UPLOAD for IVMpatient (8405) \[#117931\] 25 Jul 94 15:33

11 Lines

From: IVM PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

An Income Verification Match verified Means Test has been uploaded

for the following patient:

NAME: IVMpatient,twenty-three

ID: 000-23-8405

DATE OF TEST: SEP 12, 1993

PREV CATEGORY: A

NEW CATEGORY: C

DATE/TIME OF ADJUDICATION: SEP 18,1994@11:21

The patient is now NON-EXEMPT for prescription copay.

The patient's current Means Test status is now MT COPAY REQUIRED.

The patient is MT COPAY REQUIRED and doesn't agree to pay deductible.

## IVM - Means Test Deleted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: IVM - MEANS TEST DELETED \[#190091\] 28 Sep 94 15:46 6 Lines

From: IVM PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

An Income Verification Match Means Test was deleted for the

following patient:

NAME: IVMpatient,twenty-four

ID: 000-21-0000

TEST DATE : AUG 16,1994

> **NOTE:** The original DHCP Means Test is now the primary Means Test.

## Messages Awaiting Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sent when MailMan V. 7.1 is installed at the site and a message is awaiting transmission to the HEC.

Subj: MESSAGES 'AWAITING TRANSMISSION' \[#117931\] 25 Jul 94 15:33 6 Lines

From: IVM PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

Mailman message number 435938 is awaiting transmission.

Please call the IVM Center (Atlanta, GA) to play a script

if unable to complete script from your end.

Please note that you may have other messages that are awaiting

transmission to the IVM Center.

## Error Message From the HEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: ERROR MESSAGE FROM THE IVM CENTER \[#188441\] 02 Sep 94 13:16 9 Lines

From: IVM PACKAGE in 'IN' basket. Page 1

---------------------------------------------------------------------------

An Insurance Confirmation message or a Billing/Collections Transmission

was rejected by the IVM Center with the following error:

Patient ID/SSN not in IVM database - DFN 150

Mailman Message \# of Acknowledged Transmission: 187928

If you are unable to find the source of this problem,

please contact your ISC Support Group or the IVM Center.

## Missing Primary Long ID Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: MISSING PRIMARY LONG ID FIELD \[#195643\] 22 Mar 95 07:51 5 Lines

From: IVM PACKAGE in 'IN' basket. Page 1

---------------------------------------------------------------------------

During Income Verification Match processing, the PRIMARY LONG ID field

(.363) of PATIENT File (#2) is missing for the following patient:

NAME: IVMpatient,twenty-four

DFN: 0009017

# Appendix B - List Manager 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Manager is a tool used to display a list of items in a screen format with the following functionality.

- Browse through the list
- Select items that need action
- Take action against those items
- Select other List Manager actions without leaving the option

Actions are selected by entering the name or mnemonic at the "Select Action:" prompt. Entries may be preselected in the following manner:

> DU=1 will display upload for entry 1

In addition to the various actions that are available specific to the option you are using, List Manager provides generic actions applicable to any List Manager screen. You may enter double question marks (??) at the "Select Action" prompt for a list of all actions available. The table below lists generic List Manager actions with a brief description. Entering the mnemonic is the quickest way to select an action.

|                      |              |                                                                             |
|----------------------|--------------|-----------------------------------------------------------------------------|
| Action           | Mnemonic | Description                                                             |
| Next Screen          | \+           | Move to the next screen                                                     |
| Previous Screen      | \-           | Move to the previous screen                                                 |
| Up a Line            | UP           | Move up one line                                                            |
| Down a Line          | DN           | Move down one line                                                          |
| Shift View to Right  | \>           | Move the screen to the right if the screen width is more than 80 characters |
| Shift View to Left   | \<           | Move the screen to the left if the screen width is more than 80 characters  |
| First Screen         | FS           | Move to the first screen                                                    |
| Last Screen          | LS           | Move to the last screen                                                     |
| Go to Page           | GO           | Move to any selected page in the list                                       |
| Re Display Screen    | RD           | Redisplay the current screen                                                |
| Print Screen         | PS           | Print the header and the portion of the list currently displayed            |
| Print List           | PL           | Print the list of entries currently displayed                               |
| Search List          | SL           | Find selected text in list of entries                                       |
| Auto Display(On/Off) | ADPL         | Toggle the menu of actions to be displayed/not displayed automatically      |
| Quit                 | QU           | exits the screen                                                            |

# Index 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Appendix A - Sample Mail Messages 34
Appendix B - List Manager 37
B
Billing Transmission Report 18
D
Demographics Upload 4, 5, 6, 7, 9, 10
G
Glossary 31
I
Index 38
Insurance Upload 11
Introduction 1
IVM Address Change Log Report 22, 23
IVM Address Updates Pending Review 17
IVM Case Inquiry 19
IVM Financial Query 30
IVM Output Menu 18
IVM Parameter Enter/Edit 24
IVM System Manager's Menu 24
IVM Transmission Error Processing 28
IVM Transmission Report 26
IVM Upload Menu 4, 5, 6, 7, 9, 10
M
Means Test Comparison Report 20
P
Package Management 3
Purge IVM Transmissions 25
R
Revision History ii
U
Using the Software 4
