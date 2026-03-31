---
title: IVMB*2*895 Post MPI Enumeration Support Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Post MPI Enumeration Support
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*895
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - client
  - enumeration
  - table
  - icns
  - project
  - strong
  - master
  - contents
  - site
  - patient
page_count: 0
word_count: 994
section_count: 4
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p895_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p895_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

Health eligibility center

Atlanta, GA

Post MPI Enumeration Support

Release Notes

IVMB\*2\*895

September 2006

Management, Enrollment, Financial Systems

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose of this Manual](#purpose-of-this-manual)
  - [Acronyms and Definitions](#acronyms-and-definitions)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

First, some background.

Duplicate Integration Control Numbers (ICNs) are being identified on the HEC Legacy system as a result of the site-by-site patient enumeration process currently in progress at the VA treatment facilities which operate the VistA application. The Post MPI Enumeration Support is the second in a series of Enrollment Maintenance projects pertaining to the MPI enumeration activities that are necessary for the data migration effort for the Enrollment System Re-design project (ESR 3.0). ESR will replace the HEC Legacy application and database, as the central enrollment and eligibility system of record.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Project Sequence</strong></th>
<th><p><strong>Project Name</strong></p>
<p><strong>(Patch Number)</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>Cleansing ICN for MPI Enumeration</p>
<p>(IVMB*2*876, Completed Feb 2006)</p></td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td><p><strong>Post MPI Enumeration Support</strong></p>
<p><strong>(IVMB*2*895)</strong></p></td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Examine/Correct ICN Discrepancies</p>
<p>(IVMB*2.0*898 and IVMB*2.0*899)</p></td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Modify Duplicate Merge to Use ICN</p>
<p>(IVMB*2*888)</p></td>
</tr>
</tbody>
</table>

The Cleansing ICN for MPI Enumeration project (patch IVM\*2.0\*876, released in February 2006) deleted the Integration Control Number (ICN), ICN Checksum and CMOR for each patient record in the IVM Master Client file (#300.12). This set up the environment where it would allow the IVM Master Client file (#300.12) to be refreshed, or populated anew, with more accurate ICNs which have been assigned through the MPI Enumeration project (sent from VistA to the HEC and residing in the IVM Client Income file (#300.13) ) and are in agreement between all VistA sites of record. The Cleansing ICN for MPI Enumeration project also disabled the automatic upload of the Integration Control Number (ICN), ICN Checksum and CMOR into the IVM Master Client file (#300.12) from the HL7 ORU~Z07 Full Data Transmission received from the VistA sites. This ensured that discrepant data was resolved and not propagated.

This Post MPI Enumeration Support project (IVMB\*2.0\*895) is a follow-up patch (to IVMB\*2\*876) that will repopulate the ICN for patients in the IVM CLIENT MASTER file (#300.12) at the HEC.

## Purpose of this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to provide high-level user and technical information about enhancements to enrollment-related functionality in the HEC Legacy system.

## Acronyms and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Acronyms

|             |                                                                 |
|-------------|-----------------------------------------------------------------|
| Acronym | Description                                                 |
| API         | Application Program Interface                                   |
| CIRN        | Clinical Information Resources Network                          |
| CMOR        | Coordinating Master of Record                                   |
| HEC         | Health Eligibility Center                                       |
| ICN         | Integration Control Number                                      |
| MPI         | Master Patient Index                                            |
| VA          | Veterans Administration                                         |
| VHA         | Veterans Health Administration                                  |
| VistA       | Veterans Health Information Systems and Technology Architecture |
Definitions
|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Term          | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Checksum          | A checksum is a simple error-detection scheme in which each transmitted message is accompanied by a numerical value based on the number of set bits in the message. The receiving station then applies the same formula to the message and checks to make sure the accompanying numerical value is the same. If it’s the same, the receiver can conclude that the message was probably not corrupted. If not, the receiver can assume the message has been garbled. |
| Mailman           | The Kernel module that provides a mechanism for handling electronic communication, whether it is user-oriented mail messages, automatic firing of bulletins or initiation of server-handled data transmissions.                                                                                                                                                                                                                                                     |
| Kernel            | Kernel provides shared services for VistA applications, resulting in reduced development costs and a common user interface. In addition, it provides system management tools for managing and securing VistA computer systems. Kernel also provides a portability layer between the underlying operating system and application code.                                                                                                                               |
| HEC Legacy System | M-based database currently in use                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Taskman           | Taskman is an API utility within the Kernel that allows scheduling background jobs to run automatically in the VistA environment (a.k.a. Task Manager).                                                                                                                                                                                                                                                                                                             |

#### # New Features, Functions, and Enhancements

This project provides the functionality to address both the reconciliation of duplicate (or matching) ICNs in the HEC Legacy application and the identification of discrepant, or non-matching, ICNs. This project executes functionality that allows the patient records in the IVM Master Client file (#300.12) to receive an Integration Control Number, an ICN Checksum, and a CIRN Master of Record (CMOR) value when the IVM Client Income file (#300.13) data show duplicate or matching ICNs and other defined criteria have been met.

An automatic email bulletin generates the number of records that were processed by the data clean-up activity.

The project also implements report-generation mechanisms. When the patient records in the IVM Master Client file (#300.12) do not receive an Integration Control Number, an ICN Checksum, or a CMOR value because the IVM Client Income file (#300.13) data showed discrepant site information, the patient information and the discrepant information are listed for resolution activities. The new report option is labeled as DQ ICN RECONCILIATION RPT.

The features of the Post MPI Enumeration Support project include the following:

1.  <u>Data Clean-up</u> – Automatically updates the unique Integration Control Number (ICN), the ICN Checksum, and the CMOR in the IVM Master Client file (#300.12) when all site-transmitted ICNs are in agreement (i.e.: match) and other defined business rules are satisfied. Provides the ability to re-execute the data clean-up routine(s).
2.  <u>Automatic Bulletin Generation</u> – Reports/emails the statistics from the data clean-up activity. The bulletin is sent to the user initiating the data clean-up activity. A mockup may be viewed in the SRS (*see*Error! Reference source not found.).
3.  <u>Data Storage</u> – Stores the appropriate patient identifying information for those patient records where all the site-transmitted ICNs are <u>not</u> in agreement (i.e.: discrepant or Null) or where the site-transmitted ICNs <u>are</u> in agreement, but the associated IVM Client Income (#300.13) SSNs are <u>not</u> in agreement with the IVM Master Client (#300.12) SSN for the patient.
4.  <u>Report Generation and User Interface Changes</u> – Provides a new menu option to access an on-demand report of the patient records where the site transmitted ICNs are <u>not</u> in agreement (i.e.: discrepant or Null) or where the site transmitted ICNs <u>are</u> in agreement, but the associated IVM Client Income (#300.13) SSNs are <u>not</u> in agreement with the IVM Master Client (#300.12) SSN for the patient.

> This new option is labeled as DQ ICN RECONCILIATION RPT. The results may be viewed on the user’s screen or sent to a printer. The report may be sorted alphabetically by Patient Name (Last Name, First Name, MI) or by Social security Number. Additionally, the report may be generated for one, some or all of the following Discrepancy Types:

- 1-Active Site(s) with Null ICN(s)
- 2-ICNs Do Not Match (No Null ICN(s))
- 3-SSNs Do Not Match (ICNs Match)
- 4-No Active Site(s)
5.  <u>Disable Existing Person Merge HEC Legacy Options</u> – Disables existing person merge application options pertaining to the veteran, until the completion of the *Modify Duplicate Merge to Use ICN* project (IVMB\*2\*888, the fourth in the series of Enrollment Maintenance projects pertaining to the MPI enumeration activities), to prevent incorrect ICN assignments in the IVM Master Client file (#300.12).