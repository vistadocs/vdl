---
title: SD*5.3*589 Mental Health Treatment Coordinator (MHTC) Reporting Capability Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Mental Health Treatment Coordinator (MHTC) Reporting Capability
app_code: PCMM
app_name: Primary Care Management Module
section: CLI
app_status: active
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*589
group_key: "PCMM:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - report
  - health
  - mental
  - pcmm
  - strong
  - patient
  - team
  - table
  - mhtc
  - class
page_count: 0
word_count: 3039
section_count: 6
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_p589_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_p589_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=95"
---

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/001.png)

Primary Care Management Module (PCMM)

Mental Health Treatment Coordinator (MHTC) Reporting Capability

RELEASE NOTES

Patch SD\*5.3\*589

December 2012

Revision History

\*\*Revision history along with this note to be cleared prior to publishing on VDL, first line to contain the month and year of which the patch was approved for National Release along with a description of, “Initial Release”.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 21%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Description (Patch # if applicable)</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>Oct 2012</td>
<td><blockquote>
<p>Initial Release</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>Dec 2012</td>
<td><blockquote>
<p>Updated Stop code information. Added note after scope</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

TABLE OF CONTENTS

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Scope](#scope)
- [Description of Functionality](#description-of-functionality)
- [Installation and Implementation](#installation-and-implementation)
- [Technical Information](#technical-information)
  - [New Routine Summary](#new-routine-summary)
  - [Data Dictionaries (DDs)](#data-dictionaries-dds)
  - [Options](#options)
- [References](#references)
- [Acronyms and Definitions](#acronyms-and-definitions)
  - [Acronyms](#acronyms)
  - [Definitions](#definitions)
The purpose of this document is to describe the enhancements to the Mental Health Treatment Coordinator (MHTC) functionality in support of the Improve Veteran Mental Health (IVMH) initiative for Deliverable 2. It addresses the critical need to identify quickly in a patient’s chart the Mental Health Treatment Coordinator (MHTC) so that information regarding the Veteran’s mental health care is accessible to coordinate care more quickly and effectively.  MHTC functionality consists of three patches.  The initial patch, SD\*5.3\*575, introduces new Mental Health (MH) positions and provides the capability to establish MH teams within the Primary Care Management Module (PCMM).  The second patch, OR\*3.0\*340, passes that information over to Computerized Patient Record System (CPRS) from PCMM for displaying the data in a patient’s record. The patch described in these release notes, introduces the reporting capability for MHTCs.  The changes impact not only PCMM coordinators and mental health professionals, but also all others providing services to Veterans who are seen in Mental Health who need to coordinate the Veteran’s care, such as nurses, physicians, ward clerks, etc.

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch SD\*5.3\*589 has been developed to deliver a reporting capability to Mental Health service in support of the Identification of Principal Mental Health Provider (IPMHP) project. One new report will be available for identifying Mental Health patients in need of a Mental Health Treatment Coordinator. There will be three other reports created that will be modeled after current PCMM reports tailored to Mental Health.

> **NOTE:** These Mental Health reports pull data based upon current PCMM GUI team setup parameters.  SUBSCRIPT errors may occur if a team was not created with a Team Purpose.  Examples of SUBSCRIPT errors that maybe encountered include:

\<SUBSCRIPT\>MHTEAM+5^SCMCMHU1 ^SD(403.47,"")

\<SUBSCRIPT\>GETALL+12^SCMCMHU1 ^SD(403.47,"")

To rectify these errors, review the team setup and enter an appropriate team purpose.

# Description of Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch will introduce four reports, which will establish the MHTC Reporting capability. These reports are accessible through the PCMM VistA environment. They will be accessible through the user’s secondary menu options. There will be no changes to the existing functionality for accessing the reports. The below screen capture displays the MH report menu as it will display in the PCMM VistA environment.

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/002.png)

*<u>MH Clinician’s Patient Report</u>*: This report will display the number of patients assigned to each MH provider on a team. It will display both a summary report on the number of patients assigned to each provider on a mental health team and a detail report for each provider and will have a similar look and feel of the current PCMM Practitioner’s Patient report.

The MH Clinician’s Patient Report will:

- Provide the user the ability to select specific entries or ‘All’ for the search criteria of the data displayed within the report:
1.  Institution/Division
2.  MH Team
3.  Role
4.  Clinician/Provider
- Offer output sort options as displayed below:
  1.  Division, Team, Clinician
  2.  Division, Practitioner, Team
  3.  Practitioner, Associated Clinic

*The sort options will not be available if the user selects to print Summary only and chooses for the output to be in a delimited format. A user will only be offered the delimited output option if they choose Print Summary Only.*

- The summary report will display the following columns:
  1.  Clinician
  2.  Position
  3.  Team
  4.  Patient Assigned
- The detail report will display the following columns:
  1.  Clinician
  2.  Patient Name
  3.  Patient ID (Patient’s SSN – 5 leading X’s followed by last 4 of SSN)
  4.  Primary Eligibility
  5.  Last Appointment
  6.  Next Appointment
  7.  Clinic

> *  
> Sample: MH Clinician’s Patients Detail Report*

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/003.png)

> *Sample: MH Clinician’s Patients Summary Report*

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/004.png)

*<u>MH Encounter Report</u>*: This report will display all patients with the specified number of qualifying MH encounters within the specified date range who do not have a MHTC identified in PCMM. It enables the user to select an Institution, a date range, and the number of outpatient encounters (default = 3). The report will display a list of patients in descending order from the earliest encounter to the most recent encounter within the date range selected. The MH Encounter Report will display only one encounter per day and will only count one encounter per day towards the number of encounters selected by the user. This report should be exported to an excel spreadsheet for readability. It is a new PCMM Vista report.

The MH Encounter Report will:

- Allow the user to enter in the below criteria for generating the report:
1.  Institution (s)
2.  Date range
3.  Number of outpatient encounters (default will be three, maximum will be ten)
- Display all patients who are seen with the selected number of outpatient encounters during the specified date range
- Not include patients already assigned a MHTC
- Display patients already assigned to a MH Team
- Display patients in descending order from the earliest encounter to the most recent
- Display only one encounter per day which will be counted toward the number of encounters selected by user
- Display the columns of the following data:
1.  Patient Name
2.  SSN (last 4)
3.  Days since last encounter
4.  Encounter
    1.  Clinic Name
    2.  Location of encounter
    3.  Future Appointment date/location

*<u>NOTE:</u>* This report takes a while to run. It is recommended to queue and run this report during off-peak times. Additional recommendation is to utilize a spooler to speed up the run-time of this report.

> *Sample: MH Encounter Report*

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/005.png)

*<u>MH Historical Patient Assignment Detail Report</u>*: This report will display the history of a patient’s Mental Health assignments. It will mirror the existing PCMM VistA report, Historical Patient Assignment Detail (PAD).

The MH Historical Patient Assignment Detail Report will:

- Allow the user to enter in the below criteria for the report:
1.  Patient Name
2.  Date Range
- Display the following data along the top of the report:
1.  Patient Name
2.  SSN
3.  Date of Birth
4.  Age
5.  Sex
- Display the columns of populated data:
1.  Assignment
2.  Active
3.  Inactive
4.  Assigned by/date

> *Sample: Historical Patient Assignment Detail Report (page 1)*

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/006.png)

> *  
> Sample: Historical Patient Assignment Detail Report (page 2)*

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/007.png)

> *Sample: Historical Patient Assignment Detail Report (page 3)*

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/008.png)

> *  
> Sample: Historical Patient Assignment Detail Report (page 4)*

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/009.png)

*<u>MH Historical Team Assignment Summary Report</u>*: This report will display the MH Team Assignment history. It will display a count of team and team position assignments within a given date range. There are two main parts to this report; the first part of the report shows the “Summary of Team and Team Position Assignments”. The second part of the report shows the “Team Assignments without Active Position Assignments” displays a list of patients who have been assigned to a mental health team in PCMM but have not been assigned to any position (including non-MHTC) on that team within the date range specified. A third part of the report, “Position Assignments Without Active Team Assignments” displays patients who are assigned to a position but not a team during the date range specified. The third part of the report usually will not display because PCMM should not allow a patient to be assigned to a position without a team assignment.

The MH Historical Team Assignment Summary Report will:

- Provide the ability for a user to select a date range
- Provide additional criteria for the user to report on a specific or all Institution(s) and Team(s)
- Display the following data in part 1 of the summary report:
  1.  MH Team
  2.  MAX Pts.
  3.  MH Team Assignment
  4.  Open Slots
  5.  Patients w/o a MHTC Assignment
  6.  Patient w/o a MH Team Assignment
- Display a summary of patients without an active position assignment within part 2 of the summary report providing the below data for each patient listed:
  1.  Division
  2.  Team
  3.  Patient Name
  4.  SSN (5 leading X’s followed by last 4)
  5.  Active Date
  6.  Inactive Date

> *Sample: MH Historical Team Assignment Summary Report: Summary of Team and Team Position Assignments report*

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/010.png)

> *Sample: MH Historical Team Assignment Summary Report: Team Assignments Without Active Position Assignments report*

![](sd-5-3-589-mental-health-treatment-coordinator-mhtc-reporting-capability-release/011.png)

# Installation and Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific information pertaining to the installation of this patch can be found in the patch description for SD\*5.3\*589.

Pre-conditions for installation of this patch require the installation of SD\*5.3\*575 prior to installation of SD\*5.3\*589.

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Routine Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The below are new routines included in this patch:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th><strong>Current Logic</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SCMCMHE</td>
<td><p><em><strong>Related Options:</strong></em> SCMC MH PCMM ENCOUNTER RPT</p>
<p><em><strong>Current Logic:</strong></em> This report will allow for the identification of patients who need a MH assignment. This will be done using DSS Identifiers to determine if a patient has been seen in a MH clinic.</p></td>
</tr>
<tr class="even">
<td>SCMCMHPP</td>
<td><p><em><strong>Related Option:</strong></em> SCMC MH PCMM CLINICIAN PAT RPT</p>
<p><em><strong>Current Logic:</strong></em> This report identifies the size and constituents of a Mental Health Clinician within PCMM.</p></td>
</tr>
<tr class="odd">
<td>SCMCMHP2</td>
<td><p><em><strong>Related Option:</strong></em> SCMC MH PCMM CLINICIAN PAT RPT</p>
<p><em><strong>Current Logic:</strong></em> This report identifies the size and constituents of a Mental Health Clinician within PCMM.</p></td>
</tr>
<tr class="even">
<td>SCMCMHHP</td>
<td><p><em><strong>Related Option:</strong></em> SCMC MH PCMM HIST PAT RPT</p>
<p><em><strong>Current Logic:</strong></em> This report is a history of Mental Health patient assignments within PCMM.</p></td>
</tr>
<tr class="odd">
<td>SCMCMHHT</td>
<td><p><em><strong>Related Option:</strong></em> SCMC MH PCMM HIST TEAM SUMMARY</p>
<p><em><strong>Current Logic:</strong></em> This report will display Mental Health PCMM Team Assignment history. The report is a summary of the assignment history.</p></td>
</tr>
<tr class="even">
<td>SCMCMHU1</td>
<td><p><em><strong>Related Option:</strong></em> SCMC MH PCMM CLINICIAN PAT RPT</p>
<p><em><strong>Current Logic:</strong></em> This report identifies the size and constituents of a Mental Health Clinician within PCMM.</p></td>
</tr>
</tbody>
</table>

## Data Dictionaries (DDs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The below is a new data dictionary included in this patch:

| File Name & Number       | File Documentation                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MH PCMM STOP CODES (#404.61) | File contains a list of Mental Health Stop Codes used when running the SCMC MH PCMM ENCOUNTER RPT. Stop Codes can be added or removed using the National Release Module process. Please refer to the [PCMM MHTC User Manual](http://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/pcmmmhtcug.doc) to obtain further information on this file to include information on how the file will be maintained. |

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The below are new options included in this patch:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option Name</strong></th>
<th><strong>Option Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Mental Health PCMM Reports Menu</td>
<td><p>Mental Health PCMM report Menu to display the below menu options:</p>
<p>MH Clinician’s Patient Report</p>
<p>MH Encounter Report</p>
<p>MH Historical Patient Assignment Detail Report</p>
<p>MH Historical Team Assignment Summary Report</p></td>
</tr>
<tr class="even">
<td>MH Clinician’s Patient (SCMC MH PCMM CLINICAN PAT RPT)</td>
<td>This report identifies the size and constituents of a Mental Health Clinician within PCMM.</td>
</tr>
<tr class="odd">
<td>MH Encounter Report (SCMC MH PCMM ENCOUNTER RPT)</td>
<td>This report will allow for the identification of patients who need a MH assignment. This will be done using DSS Identifiers to determine if a patient has been seen in a MH clinic.</td>
</tr>
<tr class="even">
<td>MH Historical Patient Assignment Detail Report (SCMC MH PCMM HIST PAT RPT)</td>
<td>This report identifies the size and constituents of a Mental Health Clinician within PCMM.</td>
</tr>
<tr class="odd">
<td><p>MH Historical Team Assignment Summary Report (SCMC MH PCMM HIST TEAM</p>
<p>SUMMARY)</p></td>
<td>This report will display Mental Health PCMM Team Assignment history. The report is a summary of the assignment history.</td>
</tr>
</tbody>
</table>

# References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The below references provide additional information on MHTC functionality as discussed throughout this document.
- [PCMM MHTC User Guide](http://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/pcmmmhtcug.pdf)
- [Release Notes: SD\*5.3\*575](http://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_575rn.pdf)
- [Release Notes: OR\*3.0\*340](http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_340rn.pdf)
- [Requirements Specification Document](http://vaww.oed.portal.va.gov/projects/idprincipalmentalhealthprovider/Library/Forms/AllItems.aspx?RootFolder=%2fprojects%2fidprincipalmentalhealthprovider%2fLibrary%2fProject%20Increments%2fIncrement%203%2fDeliverable%20Documents&FolderCTID=0x0120004E6C5FC18A6A2740B5A2AD7D5F4EE0C1&View=%7bFC569A35%2d2490%2d47AE%2d925F%2dC9CBCFAE7C46%7d)

# Acronyms and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                      |
|---------|-----------------------------------------------------------------|
| CPRS    | Computerized Patient Record System                              |
| DSS     | Decision Support Systems, also called Clinic Stop Codes         |
| IPMHP   | Identification of Principal Mental Health Provider              |
| IVMH    | Improve Veteran Mental Health                                   |
| MH      | Mental Health                                                   |
| MHTC    | Mental Health Treatment Coordinator                             |
| PAD     | Patient Assignment Detail                                       |
| PCMM    | Primary Care Management Module                                  |
| RSD     | Requirements Specification Document                             |
| SDD     | Software Design Document                                        |
| SSN     | Social Security Number                                          |
| VA      | Department of Veterans Affairs                                  |
| VHA     | Veterans Health Administration                                  |
| VistA   | Veterans Health Information Systems and Technology Architecture |

## Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Computerized Patient Record System (CPRS)</td>
<td>An integrated, comprehensive suite of clinical applications in VistA that work together to create a longitudinal view of the veteran's Electronic Medical Record (EMR). CPRS comes in both the GUI and character-based formats. CPRS capabilities include a Real Time Order Checking System, a Notification System to alert clinicians of clinically significant events, Consult/Request tracking and a Clinical Reminder System. CPRS provides access to most components of the patient chart.</td>
</tr>
<tr class="even">
<td>Encounter</td>
<td>An encounter is a contact between patient and a provider who has primary responsibility for assessing and treating the patient. A patient may have multiple encounters per visit. Outpatient encounters include scheduled appointments and walk-in unscheduled visits. A clinician’s telephone communication with a patient may be represented by a separate visit entry. If the patient is seen in an outpatient clinic while an inpatient, this is treated as a separate encounter.</td>
</tr>
<tr class="odd">
<td>Institution</td>
<td>A Department of Veterans Affairs (VA) facility assigned a number by headquarters, as defined by Directive 97-058. An entry in the INSTITUTION file (#4) that represents the Veterans Health Administration (VHA). There are a wide variety of facility types in the INSTITUTION file, including medical centers, clinics, domiciliaries, administrative centers, Veterans Integrated Service Networks (VISNs), and so forth.</td>
</tr>
<tr class="even">
<td>Mental Health Clinician</td>
<td><p>A clinician who provides mental health care as defined by their privileges or scope of practice. Disciplines that represent Mental Health Clinician include Psychologist, Physician Assistant, Nurse, Psychiatrist, etc. When referenced in PCMM, a “Mental Health Clinician” refers to those disciplines listed in the roles defined in section “3.2.1 PCMM Requirements” of the ID PMHP SSD.</p>
<p>Note: Whether a particular Mental Health Clinician can serve as a MHTC is determined by their license, education and/or certification as defined in the OMHS Uniform Mental Health Services Handbook.</p></td>
</tr>
<tr class="odd">
<td>MH Treatment Coordinator (MHTC)</td>
<td><p>The liaison between the patient and the mental health system at a VA site. There is only one MHTC per patient and they are the key coordinator for behavioral health services care.</p>
<p>For more information about the MHTC responsibilities, see VHA Handbook 1160.1, "Uniform Mental Health Services in VA Medical Centers and Clinics," pp. 3-4. <strong>Note:</strong> In the handbook, the MHTC was originally referred to as the Principal Mental Health Provider.</p></td>
</tr>
<tr class="even">
<td>PCMM Coordinator</td>
<td><p>The person who performs PCMM administrative tasks at a VA site and assigns a patient to a primary care team and a primary care provider.</p>
<p><strong>Note</strong>: Assignment of the MHTC in PCMM will require coordination with the facility PCMM Coordinator. Local policies will determine exact processes for assignment of the MHTC in the PCMM package.</p></td>
</tr>
<tr class="odd">
<td>Primary Care Management Module (PCMM)</td>
<td>A VistA application that allows input of facility- and panel-specific data, and allows national roll up of this data for tracking, case finding, and comparison purposes.</td>
</tr>
<tr class="even">
<td>Position</td>
<td>A name assigned by site to describe/define a Role in PCMM. Positions are displayed in several tables on the PCMM GUI.</td>
</tr>
<tr class="odd">
<td>Primary Care Provider (PCP)</td>
<td>A physician, nurse practitioner, or physician assistant who provides ongoing, comprehensive primary care as defined by their privileges or scope of practice and licensure to a panel of assigned patients. NOTE: Physicians in Fellowship programs may be PCPs if they are Board Eligible.</td>
</tr>
<tr class="even">
<td>Role</td>
<td>A field in PCMM that denotes a function or task of a staff member involved with the implementation, maintenance and continued success of primary care and mental health care. Roles are displayed in several tables on the PCMM GUI. Sites are not allowed to edit the Role fields via FileMan without the direction of Dynamic Host Configuration Protocol (DHCP) Customer Support.</td>
</tr>
<tr class="odd">
<td>Scope</td>
<td>The sum of products and services to be provided as a project.</td>
</tr>
<tr class="even">
<td>Team</td>
<td>A group of staff members organized in PCMM for a certain purpose (i.e., Primary Care, Mental Health).</td>
</tr>
</tbody>
</table>