---
title: TMP VistA Patch 863 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: TMP VistA Patch 863
app_code: TMP
app_name: Telehealth Management Platform
section: CLI
app_status: active
pkg_ns: TMP
patch_ver: 5.3
patch_id: TMP*5.3*863
group_key: "TMP:TMP:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: The Telehealth Management Program (TMP) integrates with Veterans Health Information Systems and Technology Architecture (VistA) to schedule, cancel or update appointments in support of Telehealth services provided by the VHA. When an appointment is made or canceled on TMP, a message is sent to VistA
audience: 
keywords: 
  - stop
  - code
  - clinic
  - telehealth
  - provider
  - number
  - update
  - table
  - clinics
  - report
page_count: 0
word_count: 8738
section_count: 1
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/SD_5_3_P863_MAN_UM.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/SD_5_3_P863_MAN_UM.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=231"
---

Department of Veterans AffairsScheduling PackageTelehealth Management Platform (TMP) VistA

> USER MANUAL

![](tmp-vista-patch-863-user-manual/001.png)

February 2024Version 5.3Revision History

| Date      | Version | Description                | Author |
|---------------|-------------|--------------------------------|------------|
| February 2024 | 1.08        | Changes of SD\*5.3\*863 patch  |            |
| October 2023  | 1.07        | Changes of SD\*5.3\*859 patch  |            |
| May 2023      | 1.06        | Changes of SD\*5.3\*832 patch  |            |
| April 2023    | 1.05        | Changes of SD\*5.3\*821 patch  |            |
| June 2022     | 1.04        | Changes of SD\*5.3\*817 patch  |            |
| April 2022    | 1.03        | Changes of SD\*5.3\*812 patch  |            |
| October 2021  | 1.02        | Changes of SD\*5.3\*780 patch  |            |
| August 2021   | 1.01        | Changes of SD\*5.3\*779 patch  |            |
| May 2021      | 1.0         | Initial version for submission |            |

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Contents](#contents)
- [Introduction](#introduction)
- [VistA Telehealth User Options - Management Toolbox](#vista-telehealth-user-options-management-toolbox)
- [Option Overview](#option-overview)
- [Telehealth Inquires \[SD TELE INQ\]](#telehealth-inquires-sd-tele-inq)
- [Telehealth Stop Code Add/Edit \[SD TELE STOP CODE\]](#telehealth-stop-code-addedit-sd-tele-stop-code)
- [VistA-Telehealth Clinic Update \[SD TELE CLN UPDATE\]](#vista-telehealth-clinic-update-sd-tele-cln-update)
- [Provider Add/Edit \[SD PROVIDER ADD/EDIT\]](#provider-addedit-sd-provider-addedit)
- [Default Provider Bulk Update \[SD DEFAULT PROVIDER UPDATE\]](#default-provider-bulk-update-sd-default-provider-update)
- [Clinics Missing Station Number Report \[SD MISSING STATION NUMBER\]](#clinics-missing-station-number-report-sd-missing-station-number)
- [Display Clinic Availability Report \[SD DISPLAY AVAIL REPORT\]](#display-clinic-availability-report-sd-display-avail-report)
- [Clinics With Institutional Discrepancy \[SD INSTITUTION DISCREPANCY\]](#clinics-with-institutional-discrepancy-sd-institution-discrepancy)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Telehealth Management Program (TMP) integrates with Veterans Health Information Systems and Technology Architecture (VistA) to schedule, cancel or update appointments in support of Telehealth services provided by the VHA. When an appointment is made or canceled on TMP, a message is sent to VistA to update the VistA files with the appointment information. This information is then viewable in VistA Scheduling Options, Computerized Patient Record System (CPRS), Vista Scheduling Enhancements (VSE) Virtual Care Manager (VCM), VA Online Scheduling (VAOS) and other scheduling applications across the VHA. The integration with VistA is bi-directional and so Telehealth related appointments scheduled directly on VistA are also transmitted to TMP.

# VistA Telehealth User Options - Management Toolbox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Telehealth Management Toolbox menu is a utility that pulls together several different tasks in VistA into one location for the Telehealth user to execute the following menu options. The Telehealth Management Toolbox menu can be found under the *Scheduling Manager’s Menu* \[SDMGR\]:

Example: Scheduling Manager’s Menu and Telehealth Management Toolbox menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>ACR Ambulatory Care Reporting Menu ...</p>
<p>AM Appointment Management</p>
<p>CONS Consult/Request Tracking User Menu ...</p>
<p>SDRR Recall Reminder Main Menu ...</p>
<p>Appointment Menu ...</p>
<p>Automated Service Connected Designation Menu ...</p>
<p>Outputs ...</p>
<p>Supervisor Menu ...</p>
<p><mark>Telehealth Management Toolbox ...</mark></p>
<p>VistA Scheduling GUI Resource Mgmt Report Data</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Option Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main options included in this menu are listed below. To the left of the option name is the shortcut synonym that the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>INQ</p>
</blockquote></td>
<td><blockquote>
<p><em>Telehealth Inquiries</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p><em>Telehealth Stop Code Add/Edit</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CLN</p>
</blockquote></td>
<td><blockquote>
<p><em>VistA-Telehealth Clinic Update</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PR</p>
</blockquote></td>
<td><blockquote>
<p><em>Provider Add/Edit</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DEF</p>
</blockquote></td>
<td><blockquote>
<p><em>Default Provider Bulk Update</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MSN</p>
</blockquote></td>
<td><blockquote>
<p><em>Clinics Missing Station Number Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DISP</p>
</blockquote></td>
<td><blockquote>
<p><em>Display Clinic Availability Report</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Telehealth Inquires \[SD TELE INQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to inquire using the Clinic, Medical Center Division, Institution, Patient, List Telehealth Stop Codes, and Telehealth Stop Code Lookup.

Example 1: Inquire by Clinic

The Clinic Query allows you to view information from several different files into a single query.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Scheduling Manager's Menu &lt;TEST ACCOUNT&gt; Option: TELEhealth Management Toolbox</p>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>SID Clinics With Institutional Discrepancy</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>You have PENDING ALERTS</p>
<p>Enter "VA to jump to VIEW ALERTS option</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: INQ Telehealth Inquiries</p>
<p>Telehealth Inquiries</p>
<p>Select one of the following:</p>
<p>C Clinic</p>
<p>M Medical Center Division</p>
<p>I Institution</p>
<p>P Patient Information</p>
<p>N Patient ICN</p>
<p>L List Telehealth Stop Codes</p>
<p>S Telehealth Stop Code Lookup</p>
<p>SN Station Number (Time Sensitive)</p>
<p>R Clinic Schedule Queuing Report</p>
<p>Search Option or (Q)uit: Clinic</p>
<p>Select CLINIC: `1107 RAVI 692 - 442 ABIDE,JILLIAN R</p>
<p>================================================================================</p>
<p>Clinic : 1107-RAVI 692 - 442</p>
<p>Default Provider : 520636139-ABRAMEK,SYLVESTER S 11/03/2023@14:37</p>
<p>Provider : 520641089-ABIDE,JILLIAN R &lt;&lt; Default &gt;&gt;</p>
<p>Medical Division : 3-FORT COLLINS</p>
<p>Institution :</p>
<p>Station Number :</p>
<p>Instit.(derived) : 421-FORT COLLINS VA CLINIC</p>
<p>Station (derived) : 442GC</p>
<p>Stop Code : 148-DERMATOLOGY (304)</p>
<p>Credit Stop Code : 400-RT CLIN VID TH PAT SITE (690)</p>
<p>CHAR4 : BLUY-PRIMARY CARE BLUE Y</p>
<p>Country : 1-USA</p>
<p>Location Timezone : 8-MOUNTAIN</p>
<p>Timezone Exception:</p>
<p>Overbooks per day : 1</p>
<p>Spec Instructions : OVERBOOK PER DR. JOHNSON ONLY</p>
<p>SCHEDULE NEW PATIENTS FOR 60 MINUTES 60 CHARACTER IS A LIMIT</p>
<p>SCHEDULE NEW PATIENTS FOR 60 MINUTES 80 CHARACTER IS</p>
<p>ANOTHER LIMIT</p>
<p>================================================================================</p>
<p>Select CLINIC:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example 2: Inquire by Medical Center Division

The Medical Center Division Query allows the user to view all Divisions in the current VistA system and the details of each selected as they pertain to Telehealth.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>INQ</strong> Telehealth Inquiries</p>
<p>Telehealth Inquiries</p>
<p>Select one of the following:</p>
<p>C Clinic</p>
<p>M Medical Center Division</p>
<p>I Institution</p>
<p>P Patient Information</p>
<p>N Patient ICN</p>
<p>L List Telehealth Stop Codes</p>
<p>S Telehealth Stop Code Lookup</p>
<blockquote>
<p>SN Station Number (Time Sensitive)</p>
<p>R Clinic Schedule Queuing Report</p>
</blockquote>
<p>Search Option or (Q)uit: <strong>M</strong> Medical Center Division</p>
<p>Select MEDICAL CENTER DIVISION NAME:</p>
<p>Medical Division :</p>
<p>Facility Number :</p>
<p>Institution :</p>
<p>Select MEDICAL CENTER DIVISION NAME: <strong>^</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example 3: Inquire by Institution

The Institution Query allows the user to view the INSTITUTION file (#44), which is a National Filed that is the same in each VistA system, and the details of each selected as they pertain to Telehealth.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>INQ</strong> Telehealth Inquiries</p>
<p>Telehealth Inquiries</p>
<p>Select one of the following:</p>
<p>C Clinic</p>
<p>M Medical Center Division</p>
<p>I Institution</p>
<p>P Patient Information</p>
<p>N Patient ICN</p>
<p>L List Telehealth Stop Codes</p>
<p>S Telehealth Stop Code Lookup</p>
<blockquote>
<p>SN Station Number (Time Sensitive)</p>
<p>R Clinic Schedule Queuing Report</p>
</blockquote>
<p>Search Option or (Q)uit: <strong>I</strong> Institution</p>
<p>Select INSTITUTION NAME: CENTRAL OFFICE CO</p>
<p>===============================================================================</p>
<p>Name : 101-CENTRAL OFFICE</p>
<p>City :</p>
<p>State :</p>
<p>District :</p>
<p>VA region IEN :</p>
<p>Location Timezone : 2-EASTERN</p>
<p>Timezone Exception:</p>
<p>Country : 1-USA</p>
<p>Station # :</p>
<p>Facility DEA #: :</p>
<p>Facility Exp. date:</p>
<p>Association : 1-VISN Parent: 1-</p>
<p>Association : 2-PARENT FACILITY Parent: 2-</p>
<p>===============================================================================</p>
<p>Select INSTITUTION NAME: <strong>^</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example 4: Inquire by Patient

The Patient Information Query allows the user to view the Patient filed in the current VistA system and the details of each selected as they pertain to Telehealth.

Select one of the following:

C Clinic

M Medical Center Division

I Institution

P Patient Information

N Patient ICN

L List Telehealth Stop Codes

S Telehealth Stop Code Lookup

SN Station Number (Time Sensitive)

R Clinic Schedule Queuing Report

Search Option or (Q)uit: P Patient Information

Select Patient: XXXXX,XXXXX XXXXX,XXXXX X-X-XX XXXXXXXXX

0 NO NSC VETERAN

\>\>\> Active Patient Record Flag(s):

\<BEHAVIORAL\> CATEGORY I

Do you wish to view active patient record flag details? Yes// n (No)

Enrollment Priority: Category: NOT ENROLLED End Date: 11/02/2010

\*\*\* Patient Requires a Means Test \*\*\*

Primary Means Test Required from AUG 23,2019

Enter \<RETURN\> to continue.

===============================================================================

Number (IEN) : XXXX

Name : XXXXXXX,XXXXXXX X

Sex : XXXX

Date of Birth : XX-XX-XXXX

SSN : XXX-XX-XXXX

DOD Number : XXXXX

Full ICN : XXXXXXXXXXXXXXX

Integrated Control: XXXXXXXXXXX

ICN Checksum : XXXXX

Full ICN History : XXXXXXXXXXXXXXX

XXXXXXXXXXXXXXX

Deceased Date :

PATIENT'S SERVICE CONNECTION AND RATED DISABILITIES:

Service Connected: No

Primary Eligibility Code: NSC

No Service Connected Disabilities Listed

===============================================================================

Select Patient: X \*SENSITIVE\*

\*SENSITIVE\* YES SC VETERAN C

\*\*\*WARNING\*\*\*

\*\*\*RESTRICTED RECORD\*\*\*

Enrollment Priority: GROUP 1 Category: ENROLLED End Date:

Combat Vet Status: EXPIRED End Date: 04/26/2017

===============================================================================

Number (IEN) : XXXXXXXXX

Name : XXXXXXXXX,XXXX XXXXXX

Sex : XXXX

Date of Birth : XX-XX-XXXX

SSN : XXX-XX-XXXX

DOD Number : XXXXXXXXX

Full ICN : XXXXXXXXXXXXXXX

Integrated Control:

ICN Checksum :

Full ICN History : NO ICN HISTORY

Deceased Date :

\*\*\*\*\*\*\*\*\*\* THIS PATIENT IS 50% OR GREATER SERVICE-CONNECTED \*\*\*\*\*\*\*\*\*\*

PATIENT'S SERVICE CONNECTION AND RATED DISABILITIES:

SC Percent: 90%

LABYRINTHITIS (SC - 10%)

HEMORRHAGE OF THE BRAIN (SC - 0%)

TINNITUS (SC - 10%)

LUMBOSACRAL OR CERVICAL STRAIN (SC - 10%)

PARALYSIS OF SCIATIC NERVE (SC - 10%)

FACIAL SCARS (SC - 0%)

POLYCYTHEMIA VERA (SC - 10%)

SCARS (SC - 0%)

ASTHMA,BRONCHIAL (SC - 30%)

PARALYSIS OF MEDIAN NERVE (SC - 10%)

NEUROSIS, GEN ANX DIS (SC - 50%)

LUMBOSACRAL OR CERVICAL STRAIN (SC - 10%)

ECZEMA (SC - 10%)

2ND DEGREE BURNS (SC - 0%)

MIGRAINE HEADACHES (SC - 0%)

Primary Eligibility Code: SERVICE CONNECTED 50% to 100%

===============================================================================

Example 5: List Telehealth Stop Codes

The List Telehealth Stop Codes Query allows the user to view the current contents of the SD TELE HEALTH STOP CODE FILE (#40.6).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>INQ</strong> Telehealth Inquiries</p>
<p>Telehealth Inquiries</p>
<p>Select one of the following:</p>
<p>C Clinic</p>
<p>M Medical Center Division</p>
<p>I Institution</p>
<p>P Patient Information</p>
<p>N Patient ICN</p>
<p>L List Telehealth Stop Codes</p>
<p>S Telehealth Stop Code Lookup</p>
<p>SN Station Number (Time Sensitive)</p>
<blockquote>
<p>R Clinic Schedule Queuing Report</p>
</blockquote>
<p>Search Option or (Q)uit: <strong>L</strong> List Stop codes</p>
<p>===============================================================================</p>
<p>Stop Code: 103 &gt; TELEPHONE TRIAGE</p>
<p>Stop Code: 104 &gt; PULMONARY FUNCTION</p>
<p>Stop Code: 105 &gt; X-RAY &amp; FLUORO (XR &amp; RF)</p>
<p>Stop Code: 106 &gt; EEG</p>
<p>Stop Code: 107 &gt; EKG</p>
<p>Stop Code: 108 &gt; LABORATORY</p>
<p>Stop Code: 109 &gt; NUC MED &amp; PET (NM &amp; PET)</p>
<p>Stop Code: 110 &gt; INTERVENT RAD CLINIC (IR)</p>
<p>Stop Code: 111 &gt; TELE-PATHOLOGY</p>
<p>Stop Code: 115 &gt; ULTRASOUND (US)</p>
<p>Stop Code: 116 &gt; RESPIRATORY THERAPY</p>
<p>Stop Code: 117 &gt; NURSING (2ND ONLY)</p>
<p>Stop Code: 118 &gt; HOME TREATMENT SERVICES</p>
<p>Stop Code: 119 &gt; CNH FOLLOW-UP</p>
<p>Stop Code: 120 &gt; HEALTH SCREENING</p>
<p>Stop Code: 121 &gt; COMMUNITY RES CARE</p>
<p>Stop Code: 123 &gt; NUTRITION/DIETETICS-INDIVIDUAL</p>
<p>Stop Code: 124 &gt; NUTRITION/DIETETICS-GROUP</p>
<p>Stop Code: 125 &gt; SOCIAL WORK SERVICE</p>
<p>Stop Code: 126 &gt; EVOKED POTENTIAL</p>
<p>Stop Code: 128 &gt; PROLONGED VIDEO-EEG MONITORING</p>
<p>Stop Code: 130 &gt; EMERGENCY DEPT</p>
<p>Stop Code: 131 &gt; URGENT CARE CLINIC</p>
<p>Stop Code: 135 &gt; POST-DEPLOY INTGRTD CARE</p>
<p>Stop Code: 136 &gt; TELE POST DEPLOY PT SITE</p>
<p>Stop Code: 137 &gt; TELE POST DEPLOY PROV SITE</p>
<p>Stop Code: 139 &gt; HEALTH/WELLBEING SRVS</p>
<p>Stop Code: 142 &gt; WOUND TREAT &amp; OSTOMY CARE</p>
<p>Stop Code: 143 &gt; SLEEP STUDY</p>
<p>Stop Code: 145 &gt; MYOCARD PERF STUDIES</p>
<p>Stop Code: 147 &gt; TELEPHONE/ANCILLARY</p>
<p>Stop Code: 148 &gt; TELEPHONE/DIAGNOSTIC</p>
<p>Stop Code: 149 &gt; RADIATION ONCOLOGY</p>
<p>Stop Code: 150 &gt; COMPUTERIZED TOMOGRAPHY (CT)</p>
<p>Stop Code: 151 &gt; MAGNETIC RESONANCE IMAGING/MRI</p>
<p>Stop Code: 153 &gt; INTERVENT RAD PROCEDURE (IR)</p>
<p>Stop Code: 156 &gt; HBPC - PSYCHOLOGIST</p>
<p>Stop Code: 157 &gt; HBPC - PSYCHIATRIST</p>
<p>Stop Code: 158 &gt; BRACHYTHERAPY TREATMENT</p>
<p>Stop Code: 159 &gt; CIH TREATMENT</p>
<p>Stop Code: 160 &gt; CLINICAL PHARMACY</p>
<p>Stop Code: 162 &gt; MEDICAL FOSTER HOME</p>
<p>Stop Code: 165 &gt; BEREAVEMENT COUNSELING</p>
<p>Stop Code: 166 &gt; CHAPLAIN SERVICE - INDIVIDUAL</p>
<p>Stop Code: 167 &gt; CHAPLAIN SERVICE - GROUP</p>
<p>Stop Code: 168 &gt; CHAPLAIN SERVICE - COLLATERAL</p>
<p>Stop Code: 169 &gt; TELEPHONE/CHAPLAIN</p>
<p>Stop Code: 170 &gt; HBPC - PHYSICIAN</p>
<p>Stop Code: 171 &gt; HBPC Nursing (RN / LP)</p>
<p>Stop Code: 172 &gt; HBPC PHYSIC EXTND(NP,CNS,PA)</p>
<p>Stop Code: 173 &gt; HBPC - SOCIAL WORKER</p>
<p>Stop Code: 174 &gt; HBPC - THERAPIST</p>
<p>Stop Code: 175 &gt; HBPC - DIETITIAN</p>
<p>Stop Code: 176 &gt; HBPC - CLINICAL PHARMACIST</p>
<p>Stop Code: 177 &gt; HBPC - OTHER</p>
<p>Stop Code: 178 &gt; TELEPHONE HBPC</p>
<p>Stop Code: 179 &gt; RT CLIN VID CARE HOME</p>
<p>Stop Code: 180 &gt; DENTAL</p>
<p>Stop Code: 181 &gt; TELEPHONE/DENTAL</p>
<p>Stop Code: 182 &gt; TELEPHONE CASE MANAGEMENT</p>
<p>Stop Code: 183 &gt; PEER SPECIALIST</p>
<p>Stop Code: 184 &gt; CARE/CASE MANAGER</p>
<p>Stop Code: 185 &gt; NURSE PRACTITIONER</p>
<p>Stop Code: 186 &gt; PHYSICIAN ASSISTANT</p>
<p>Stop Code: 187 &gt; CLINICAL NURSE SPECIALIST</p>
<p>Stop Code: 188 &gt; FELLOW/RESIDENT</p>
<p>Stop Code: 189 &gt; S&amp;F HOME NON VA PROV SITE</p>
<p>Stop Code: 190 &gt; ADULT DAY HEALTH CARE</p>
<p>Stop Code: 191 &gt; COMMUNITY ADHC FOLLOWUP</p>
<p>Stop Code: 192 &gt; CAREGIVER SUPPORT PROGRAM</p>
<p>Stop Code: 195 &gt; POLYTRMA TRNSIT REHAB IND</p>
<p>Stop Code: 196 &gt; POLYTRMA TRNSIT REHAB GRP</p>
<p>Stop Code: 197 &gt; POLYTRAUMA/TBI IND</p>
<p>Stop Code: 198 &gt; POLYTRAUMA/TBI GRP</p>
<p>Stop Code: 199 &gt; TELEPHONE POLYTRAUMA/TBI</p>
<p>Stop Code: 201 &gt; PM&amp;RS PHYSICIAN</p>
<p>Stop Code: 202 &gt; RECREATION THERAPY SERVICE</p>
<p>Stop Code: 203 &gt; AUDIOLOGY</p>
<p>Stop Code: 204 &gt; SPEECH-LANGUAGE PATHOLOGY</p>
<p>Stop Code: 205 &gt; PHYSICAL THERAPY</p>
<p>Stop Code: 206 &gt; OCCUPATIONAL THERAPY</p>
<p>Stop Code: 209 &gt; VIST COORDINATOR</p>
<p>Stop Code: 210 &gt; SPINAL CORD INJURY</p>
<p>Stop Code: 211 &gt; PM&amp;RS AMP CLINIC</p>
<p>Stop Code: 212 &gt; EMG - ELECTROMYOGRAM</p>
<p>Stop Code: 214 &gt; KINESIOTHERAPY</p>
<p>Stop Code: 215 &gt; SCI HOME CARE PROGRAM</p>
<p>Stop Code: 216 &gt; TELEPHONE/REHAB AND SUPPORT</p>
<p>Stop Code: 217 &gt; BROS (BLIND REHAB O/P SPEC)</p>
<p>Stop Code: 218 &gt; BLIND REHAB CENTER</p>
<p>Stop Code: 220 &gt; VISOR &amp; ADVANCED BLIND REHAB</p>
<p>Stop Code: 221 &gt; TELEPHONE VIST</p>
<p>Stop Code: 224 &gt; TELEPHONE SCI</p>
<p>Stop Code: 225 &gt; SCI TELEHEALTH VIRTUAL</p>
<p>Stop Code: 229 &gt; TELEPHONE/BLIND REHAB PROGRAM</p>
<p>Stop Code: 230 &gt; PM&amp;RS DRIVER TRAINING</p>
<p>Stop Code: 231 &gt; CARDIO-PULM REHAB</p>
<p>Stop Code: 240 &gt; PM&amp;R ASSIST TECH CLINIC</p>
<p>Stop Code: 241 &gt; WHEELCHAIR &amp; ADVAN MOBILITY</p>
<p>Stop Code: 250 &gt; REHAB SRVCS GROUP</p>
<p>Stop Code: 301 &gt; GENERAL INTERNAL MEDICINE</p>
<p>Stop Code: 302 &gt; ALLERGY IMMUNOLOGY</p>
<p>Stop Code: 303 &gt; CARDIOLOGY</p>
<p>Stop Code: 304 &gt; DERMATOLOGY</p>
<p>Stop Code: 305 &gt; ENDOCRINOLOGY</p>
<p>Stop Code: 306 &gt; DIABETES CLINIC</p>
<p>Stop Code: 307 &gt; GASTROENTEROLOGY</p>
<p>Stop Code: 308 &gt; HEMATOLOGY</p>
<p>Stop Code: 309 &gt; HYPERTENSION</p>
<p>Stop Code: 310 &gt; INFECTIOUS DISEASE</p>
<p>Stop Code: 311 &gt; CIED DEVICES</p>
<p>Stop Code: 312 &gt; PULMONARY/CHEST</p>
<p>Stop Code: 313 &gt; RENAL/NEPHROL(EXCEPT DIALYSIS)</p>
<p>Stop Code: 314 &gt; RHEUMATOLOGY/ARTHRITIS</p>
<p>Stop Code: 315 &gt; NEUROLOGY</p>
<p>Stop Code: 316 &gt; ONCOLOGY/TUMOR</p>
<p>Stop Code: 317 &gt; ANTI-COAGULATION CLINIC</p>
<p>Stop Code: 318 &gt; GERI PROB CONSULT CLINIC</p>
<p>Stop Code: 321 &gt; GI ENDOSCOPY</p>
<p>Stop Code: 322 &gt; COMP WOMEN'S HLTH</p>
<p>Stop Code: 323 &gt; PRIMARY CARE/MEDICINE</p>
<p>Stop Code: 324 &gt; TELEPHONE/MEDICINE</p>
<p>Stop Code: 325 &gt; TELEPHONE/NEUROLOGY</p>
<p>Stop Code: 326 &gt; TELEPHONE/GERIATRICS</p>
<p>Stop Code: 327 &gt; MED MD PERFORM INVASVE OR PROC</p>
<p>Stop Code: 328 &gt; MEDICAL/SURGICAL DAY UNIT MSDU</p>
<p>Stop Code: 329 &gt; MEDICAL PROCEDURE UNIT</p>
<p>Stop Code: 330 &gt; CHEMOTHERAPY PROC. UNIT-MED.</p>
<p>Stop Code: 332 &gt; PRE-BED CARE (MED SERVICE)</p>
<p>Stop Code: 333 &gt; CARDIAC CATHETERIZATION</p>
<p>Stop Code: 334 &gt; CARDIAC STRESS TEST</p>
<p>Stop Code: 335 &gt; PADRECC PARKINSONS</p>
<p>Stop Code: 336 &gt; MEDICAL PRE-PROCED EVAL</p>
<p>Stop Code: 337 &gt; HEPATOLOGY CLINIC</p>
<p>Stop Code: 338 &gt; TELEPHONE PRIMARY CARE</p>
<p>Stop Code: 339 &gt; OBSTETRICS</p>
<p>Stop Code: 340 &gt; GENOMIC CARE</p>
<p>Stop Code: 341 &gt; PEDIATRICS</p>
<p>Stop Code: 342 &gt; FAMILY PRACTICE</p>
<p>Stop Code: 344 &gt; MULTIPLE SCLEROSIS (MS)</p>
<p>Stop Code: 345 &gt; EPILEPSY ECOE</p>
<p>Stop Code: 346 &gt; ALS CENTER</p>
<p>Stop Code: 347 &gt; ALS HOME CARE PROGRAM</p>
<p>Stop Code: 348 &gt; PRIMARY CARE SHARED APPT</p>
<p>Stop Code: 349 &gt; SLEEP MEDICINE</p>
<p>Stop Code: 350 &gt; GERIPACT</p>
<p>Stop Code: 351 &gt; HOSPICE CARE</p>
<p>Stop Code: 352 &gt; GRECC CLINICAL DEMO</p>
<p>Stop Code: 353 &gt; PALLIATIVE CARE</p>
<p>Stop Code: 354 &gt; HOSPITAL IN HOME</p>
<p>Stop Code: 356 &gt; WRIISC</p>
<p>Stop Code: 369 &gt; EP LAB</p>
<p>Stop Code: 370 &gt; GEC LTSS</p>
<p>Stop Code: 371 &gt; HT SCREENING</p>
<p>Stop Code: 372 &gt; WEIGHT MGMT &amp; MOVE! PROG - IND</p>
<p>Stop Code: 373 &gt; WEIGHT MGMT &amp; MOVE! PROG - GRP</p>
<p>Stop Code: 391 &gt; CARDIAC ECHO</p>
<p>Stop Code: 392 &gt; AMB ECG MONITORING</p>
<p>Stop Code: 394 &gt; MED SPECIALTY SHARED APPT</p>
<p>Stop Code: 401 &gt; GENERAL SURGERY</p>
<p>Stop Code: 402 &gt; CARDIAC SURGERY</p>
<p>Stop Code: 403 &gt; OTOLARYNGOLOGY/ENT</p>
<p>Stop Code: 404 &gt; GYNECOLOGY</p>
<p>Stop Code: 405 &gt; HAND SURGERY</p>
<p>Stop Code: 406 &gt; NEUROSURGERY</p>
<p>Stop Code: 407 &gt; OPHTHALMOLOGY</p>
<p>Stop Code: 408 &gt; OPTOMETRY</p>
<p>Stop Code: 409 &gt; ORTHO/JOINT SURG</p>
<p>Stop Code: 410 &gt; PLASTIC SURGERY</p>
<p>Stop Code: 411 &gt; PODIATRY</p>
<p>Stop Code: 413 &gt; THORACIC SURGERY</p>
<p>Stop Code: 414 &gt; UROLOGY CLINIC</p>
<p>Stop Code: 415 &gt; VASCULAR SURGERY</p>
<p>Stop Code: 417 &gt; PROSTHETICS/ORTHOTICS</p>
<p>Stop Code: 418 &gt; AMPUTATION CLINIC</p>
<p>Stop Code: 419 &gt; ANESTHESIA PRE/POST-OP CONSULT</p>
<p>Stop Code: 420 &gt; PAIN CLINIC</p>
<p>Stop Code: 421 &gt; VASCULAR LABORATORY</p>
<p>Stop Code: 423 &gt; PROS AND SENS AIDS</p>
<p>Stop Code: 424 &gt; TELEPHONE/SURGERY</p>
<p>Stop Code: 425 &gt; TELEPHONE/PROSTHETICS/ORTHOTIC</p>
<p>Stop Code: 427 &gt; ANES SPECIAL PROCS IN OR SUITE</p>
<p>Stop Code: 428 &gt; TELEPHONE/OPTOMETRY</p>
<p>Stop Code: 429 &gt; PATIENT CARE IN OR</p>
<p>Stop Code: 430 &gt; CYSTO ROOM IN UROLOGY CL</p>
<p>Stop Code: 432 &gt; PRE-SURG EVAL</p>
<p>Stop Code: 434 &gt; NON-OR ANESTHESIA PROCEDURES</p>
<p>Stop Code: 435 &gt; SURGICAL PROCEDURE UNIT</p>
<p>Stop Code: 436 &gt; CHIROPRACTIC CARE</p>
<p>Stop Code: 437 &gt; VICTORS &amp; ADVANCED LOW VISION</p>
<p>Stop Code: 438 &gt; INTERMED LOW VISION CARE</p>
<p>Stop Code: 439 &gt; LOW VISION CARE</p>
<p>Stop Code: 440 &gt; TELE FIT &amp; ADJUST PROV SITE</p>
<p>Stop Code: 441 &gt; TELEPHONE ANESTHESIA</p>
<p>Stop Code: 443 &gt; DBQ REFERRAL CLINIC</p>
<p>Stop Code: 444 &gt; C&amp;P VIA CVT PT SITE</p>
<p>Stop Code: 445 &gt; C&amp;P VIA CVT PROV SITE</p>
<p>Stop Code: 446 &gt; IDES VIA CVT PT SITE</p>
<p>Stop Code: 447 &gt; IDES VIA CVT PROV SITE</p>
<p>Stop Code: 448 &gt; INTGRTED DIS EVAL (IDES) EXAM</p>
<p>Stop Code: 449 &gt; FITTING &amp; ADJSTMNTS 2ND ONLY</p>
<p>Stop Code: 450 &gt; COMP &amp; PENS (C&amp;P) EXAMS</p>
<p>Stop Code: 457 &gt; TRANSPLANT</p>
<p>Stop Code: 474 &gt; RESEARCH</p>
<p>Stop Code: 481 &gt; BRONCHOSCOPY</p>
<p>Stop Code: 486 &gt; CARDIOTHORACIC SURG</p>
<p>Stop Code: 487 &gt; BARIATRIC SURG</p>
<p>Stop Code: 488 &gt; SURG ONCOLOGY</p>
<p>Stop Code: 489 &gt; SPINAL SURG</p>
<p>Stop Code: 490 &gt; TELETRANSPLANT PT SITE</p>
<p>Stop Code: 491 &gt; TELETRANSPLANT PROV SITE</p>
<p>Stop Code: 497 &gt; REGISTRY EXAM CVT PT SITE</p>
<p>Stop Code: 498 &gt; REGISTRY EXAM CVT PROV SITE</p>
<p>Stop Code: 499 &gt; ENVIRON HEALTH REG EXAM</p>
<p>Stop Code: 502 &gt; MENTAL HEALTH CLINIC - IND</p>
<p>Stop Code: 504 &gt; GRANT &amp; PER DIEM GROUP</p>
<p>Stop Code: 507 &gt; HUD/VASH GROUP</p>
<p>Stop Code: 508 &gt; HCHV/HCMI GROUP</p>
<p>Stop Code: 509 &gt; PSYCHIATRY</p>
<p>Stop Code: 510 &gt; PSYCHOLOGY</p>
<p>Stop Code: 511 &gt; GRANT &amp; PER DIEM INDIV</p>
<p>Stop Code: 513 &gt; SUBSTANCE USE DISORDER IND</p>
<p>Stop Code: 514 &gt; SUB USE DISORDER HOME VST</p>
<p>Stop Code: 516 &gt; PTSD - GROUP</p>
<p>Stop Code: 519 &gt; SUB USE DISORDER PTSD TEAM</p>
<p>Stop Code: 522 &gt; HUD/VASH INDIV</p>
<p>Stop Code: 523 &gt; OPIOID TREATMENT PROGRAM</p>
<p>Stop Code: 524 &gt; ACTIVE DUTY SEXUAL TRAUMA</p>
<p>Stop Code: 527 &gt; TELEPHONE MH</p>
<p>Stop Code: 528 &gt; TELEPHONE HCMI</p>
<p>Stop Code: 529 &gt; HCHV/HCMI INDIV</p>
<p>Stop Code: 530 &gt; TELEPHONE/HUD-VASH</p>
<p>Stop Code: 533 &gt; MH INTERVNTION BIOMED CARE IND</p>
<p>Stop Code: 534 &gt; MH INTGRTD CARE IND</p>
<p>Stop Code: 535 &gt; MH VOCATIONAL ASSISTANCE - IND</p>
<p>Stop Code: 536 &gt; TELEPHONE/MH VOC ASSISTANCE</p>
<p>Stop Code: 538 &gt; PSYCHOLOGICAL TESTING</p>
<p>Stop Code: 539 &gt; MH INTGRTD CARE GRP</p>
<p>Stop Code: 542 &gt; TELEPHONE/PTSD</p>
<p>Stop Code: 545 &gt; TELEPHONE SUD</p>
<p>Stop Code: 546 &gt; TELEPHONE ICMHR</p>
<p>Stop Code: 550 &gt; MENTAL HEALTH CLINIC-GROUP</p>
<p>Stop Code: 552 &gt; ICMHR INDIVIDUAL</p>
<p>Stop Code: 555 &gt; HOMELESS VT COM EMP SVC INDIV</p>
<p>Stop Code: 556 &gt; HOMELESS VT COM EMP SVC GRP</p>
<p>Stop Code: 560 &gt; SUBSTANCE USE DISORDR GRP</p>
<p>Stop Code: 562 &gt; PTSD - INDIVIDUAL</p>
<p>Stop Code: 564 &gt; MH TEAM CASE MANAGEMENT</p>
<p>Stop Code: 565 &gt; MH INTERVENTION BIOMED GRP</p>
<p>Stop Code: 566 &gt; MH RISK-FACTOR-REDUCTION ED GR</p>
<p>Stop Code: 567 &gt; ICMHR GROUP</p>
<p>Stop Code: 568 &gt; MH CWT/SE</p>
<p>Stop Code: 573 &gt; MH INCENTIVE THERAPY F TO F</p>
<p>Stop Code: 574 &gt; MH CWT/TWE</p>
<p>Stop Code: 575 &gt; MH VOCATIONAL ASSISTANCE-GRP</p>
<p>Stop Code: 576 &gt; PSYCHOGERIATRIC - INDIVIDUAL</p>
<p>Stop Code: 577 &gt; PSYCHOGERIATRIC - GROUP</p>
<p>Stop Code: 579 &gt; TELEPHONE/PSYCHOGERIATRICS</p>
<p>Stop Code: 582 &gt; PRRC INDIVIDUAL</p>
<p>Stop Code: 583 &gt; PRRC GROUP</p>
<p>Stop Code: 584 &gt; TELEPHONE PRRC</p>
<p>Stop Code: 586 &gt; RRTP INDIVIDUAL</p>
<p>Stop Code: 587 &gt; RRTP GROUP</p>
<p>Stop Code: 591 &gt; HEALTHCARE FOR REENTRY VETS</p>
<p>Stop Code: 592 &gt; VETERANS JUSTICE OUTREACH</p>
<p>Stop Code: 593 &gt; RRTP OUTREACH SERVICES</p>
<p>Stop Code: 596 &gt; RRTP ADMISSION SCREENING SRVCS</p>
<p>Stop Code: 597 &gt; TELEPHONE - RRTP</p>
<p>Stop Code: 598 &gt; RRTP OUTPATIENT INDIVIDUAL</p>
<p>Stop Code: 599 &gt; RRTP OUTPATIENT GROUP</p>
<p>Stop Code: 602 &gt; ASSISTED HEMODIALYSIS</p>
<p>Stop Code: 603 &gt; LIMITED SELF CARE HEMODIALYSIS</p>
<p>Stop Code: 604 &gt; HOME/SELF HEMODIALYSIS TRNING</p>
<p>Stop Code: 605 &gt; HOMESELF HEMDIAL FOLLOWUP</p>
<p>Stop Code: 606 &gt; HOMESELF PERITNDIALY FOLLOWUP</p>
<p>Stop Code: 607 &gt; STAFFASSIST PERITNDIALY</p>
<p>Stop Code: 608 &gt; HOMESELF PERITNDIALY TRNING</p>
<p>Stop Code: 611 &gt; TELEPHONE/DIALYSIS</p>
<p>Stop Code: 644 &gt; NC RTCV TELECARE PT LOC</p>
<p>Stop Code: 645 &gt; NC RTCV TELECARE PRV LOC</p>
<p>Stop Code: 646 &gt; NC S&amp;F TELECARE PT LOC</p>
<p>Stop Code: 647 &gt; NC S&amp;F TELECARE PRV LOC</p>
<p>Stop Code: 648 &gt; RT CVT W NONVAMC PROVID LOC</p>
<p>Stop Code: 651 &gt; STATE NURSING HOME DAYS</p>
<p>Stop Code: 652 &gt; STATE RES REHAB TX PGRM (RRTP)</p>
<p>Stop Code: 656 &gt; DOD NON-VA CARE</p>
<p>Stop Code: 658 &gt; STATE HOME ADULT DAY HLTHCARE</p>
<p>Stop Code: 669 &gt; COMMUNITY CARE CONSULT</p>
<p>Stop Code: 673 &gt; CLINICAL TEAM CONFERENCE</p>
<p>Stop Code: 674 &gt; ADMIN PAT ACTIVTIES (MASNONCT)</p>
<p>Stop Code: 679 &gt; NC CVT TO HOME PROVID LOC</p>
<p>Stop Code: 680 &gt; HCBC ASSESSMENT</p>
<p>Stop Code: 681 &gt; VA-PAID HCBC PROVIDERS</p>
<p>Stop Code: 682 &gt; VA-REFER TO HCBC PROV</p>
<p>Stop Code: 683 &gt; HT NON-VIDEO MONITORING</p>
<p>Stop Code: 684 &gt; HT NON-VIDEO INTERVENTION</p>
<p>Stop Code: 685 &gt; HT PROGRAM PATIENTS</p>
<p>Stop Code: 686 &gt; TELEPHONE BY HT STAFF</p>
<p>Stop Code: 690 &gt; RT CLIN VID TH PAT SITE</p>
<p>Stop Code: 692 &gt; CVT PRV SITE SAME DIV/STA</p>
<p>Stop Code: 693 &gt; RT CLIN VD TH PRV SITE(DIFSTA)</p>
<p>Stop Code: 694 &gt; SF TH PAT SITE</p>
<p>Stop Code: 695 &gt; SF TH PRV SITE SAME DIV/STA</p>
<p>Stop Code: 696 &gt; SF TH PRV SITE(DIFSTA)</p>
<p>Stop Code: 697 &gt; CHART CONSULT</p>
<p>Stop Code: 698 &gt; REMOTE PT MONITOR PROV SITE</p>
<p>Stop Code: 699 &gt; CVT EMERGENCY CONSULT</p>
<p>Stop Code: 701 &gt; BP EVAL</p>
<p>Stop Code: 703 &gt; MAMMOGRAM (MG)</p>
<p>Stop Code: 704 &gt; WMS SPECIFIC PREVENTIVE CARE</p>
<p>Stop Code: 706 &gt; ALCOHOL SCREENING</p>
<p>Stop Code: 707 &gt; SMOKING CESSATION</p>
<p>Stop Code: 708 &gt; TELE SMOKE CESS PROV SITE</p>
<p>Stop Code: 710 &gt; PREVENTIVE IMMUNIZATION</p>
<p>Stop Code: 713 &gt; GAMBLING ADDICTION (2ND ONLY)</p>
<p>Stop Code: 714 &gt; OTHER ED IND</p>
<p>Stop Code: 717 &gt; PPD CLINIC (2ND ONLY)</p>
<p>Stop Code: 718 &gt; EYE TELE SCREENING</p>
<p>Stop Code: 719 &gt; MHV SECURE MESSAGING</p>
<p>Stop Code: 720 &gt; OTHER ED GRP</p>
<p>Stop Code: 721 &gt; OEND ED IND</p>
<p>Stop Code: 722 &gt; OEND ED GRP</p>
<p>Stop Code: 723 &gt; OEND ED CVT PT SITE</p>
<p>Stop Code: 724 &gt; OEND ED CVT PRV SITE</p>
<p>Stop Code: 901 &gt; TELE-ICU PATIENT SITE</p>
<p>Stop Code: 999 &gt; OCCUPATIONAL HEALTH</p>
<p>Stop Code: 103801</p>
<p>103 &gt; TELEPHONE TRIAGE</p>
<p>801 &gt; TELEPHONE TRIAGE IN VISN</p>
<p>Stop Code: 103802</p>
<p>103 &gt; TELEPHONE TRIAGE</p>
<p>802 &gt; TELEPHONE TRIAGE OUT OF VISN</p>
<p>Stop Code: 103803</p>
<p>103 &gt; TELEPHONE TRIAGE</p>
<p>803 &gt; TELEPHONE TRIAGE COMMERCIAL</p>
<p>Stop Code: 323531</p>
<p>323 &gt; PRIMARY CARE/MEDICINE</p>
<p>531 &gt; PRI CARE FOR PTS WITH SMI</p>
<p>Stop Code: 338531</p>
<p>338 &gt; TELEPHONE PRIMARY CARE</p>
<p>531 &gt; PRI CARE FOR PTS WITH SMI</p>
<p>Stop Code: 339184</p>
<p>339 &gt; OBSTETRICS</p>
<p>184 &gt; CARE/CASE MANAGER</p>
<p>Stop Code: 568535</p>
<p>568 &gt; MH CWT/SE</p>
<p>535 &gt; MH VOCATIONAL ASSISTANCE - IND</p>
<p>Stop Code: 674685</p>
<p>674 &gt; ADMIN PAT ACTIVTIES (MASNONCT)</p>
<p>685 &gt; HT PROGRAM PATIENTS</p>
<p>===============================================================================</p>
<p>Total number of Telehealth Stop code: 86</p>
<p>Press &lt;Enter&gt; to continue</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example 6: Inquire by Stop Code

The Telehealth Stop Code Lookup Query allows the user to Lookup a Stop Code and its Description.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>INQ</strong> Telehealth Inquiries</p>
<p>Telehealth Inquiries</p>
<p>Select one of the following:</p>
<p>C Clinic</p>
<p>M Medical Center Division</p>
<p>I Institution</p>
<p>P Patient Information</p>
<p>N Patient ICN</p>
<p>L List Telehealth Stop Codes</p>
<p>S Telehealth Stop Code Lookup</p>
<p>SN Station Number (Time Sensitive)</p>
<blockquote>
<p>R Clinic Schedule Queuing Report</p>
</blockquote>
<p>Search Option or (Q)uit: <strong>S</strong>top Code Lookup</p>
<p>Select SD TELE HEALTH STOP CODE FILE STOP CODE NUMBER: 685</p>
<p>===============================================================================</p>
<p>Stop Code: 685 &gt; HT PROGRAM PATIENTS</p>
<p>===============================================================================</p>
<p>Select SD TELE HEALTH STOP CODE FILE STOP CODE NUMBER: ^</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example 7: Inquire by Station Number

Inquire by Station Number allows the scheduling supervisor to inquire on the Station Number (Time Sensitive) file (#389.9) from the Telehealth Inquiries \[SD TELE INQ\] option.

INQ Telehealth Inquiries

ST Telehealth Stop Code Add/Edit

CLN VistA-Telehealth Clinic Update

PR Provider Add/Edit

DEF Default Provider Bulk Update

MSN Clinics Missing Station Number Report

DISP Display Clinic Availability Report

Select Telehealth Management Toolbox \<TEST ACCOUNT\> Option: INQ Telehealth Inquiries

Telehealth Inquiries

Select one of the following:

C Clinic

M Medical Center Division

I Institution

P Patient Information

N Patient ICN

L List Telehealth Stop Codes

S Telehealth Stop Code Lookup

SN Station Number (Time Sensitive)

> R ClinicSchedule Queuing Report

Search Option or (Q)uit: SN Station Number (Time Sensitive)

Select STATION NUMBER (TIME SENSITIVE) REFERENCE NUMBER: 1 01-01-80

Another one:?

Answer with STATION NUMBER (TIME SENSITIVE), or REFERENCE NUMBER, or

EFFECTIVE DATE, or MEDICAL CENTER DIVISION

Choose from:

1 01-01-80 XXXX

2 03-28-97 XXXX

3 12-01-97 XXXX

4 10-01-98 XXXX

5 07-01-99 XXXX

6 03-23-09 XXXX

7 04-27-11 XXXX

8 02-23-17 XXXX

9 12-11-15 XXXX

10 02-01-16 XXXX

Another one:2 03-28-97 XXXX 442GA

Another one:

===============================================================================

Number: 1 Reference Number: 1

Effective Date: Jan 01, 2080 Medical Center Division:

Station Number: XXX Inactive: No

Is Primary Division: Yes

Number: 2 Reference Number: 2

Effective Date: Mar 28, 1997 Medical Center Division:

Station Number: XXXX Inactive: Yes

Is Primary Division: No

===============================================================================

Select STATION NUMBER (TIME SENSITIVE) REFERENCE NUMBER:

Example 8: Clinic Schedule Queuing Report

When editing VistA clinic schedules, two transactions typically occur. The old schedule is deleted, which results in a BLOCK CLINIC DAY transaction being sent to TMP. When the new schedule is written to the clinic, an UNBLOCK CLINIC DAY transaction is sent. This results in the clinic being blocked momentarily until the second transaction arrives. This method has created a good deal of network traffic and occasionally causes problems if the transactions arrive out-of-order causing an inadvertent blocked day.

To resolve these problems, a queue is being created to hold all of the clinic schedule edit transactions briefly so that they can be evaluated. All of the BLOCK CLINIC DAY and UNBLOCK CLINIC DAY transaction pairs will be canceled, as they have no net effect on the system, but potentially cause a great deal of network congestion. Those that need to be sent on to TMP will be sent in the correct order.

The Clinic Schedule Queuing Report lists all of the transactions that were queued and the action resulting form the queuing. Actions can be *sent* (transaction was sent to VistA) or *offset* (transactions were cancelled and not sent to VistA).

INQ Telehealth Inquiries

ST Telehealth Stop Code Add/Edit

CLN VistA-Telehealth Clinic Update

PR Provider Add/Edit

DEF Default Provider Bulk Update

MSN Clinics Missing Station Number Report

DISP Display Clinic Availability Report

Select Telehealth Management Toolbox \<TEST ACCOUNT\> Option: INQ Telehealth Inquiries

Telehealth Inquiries

Select one of the following:

C Clinic

M Medical Center Division

I Institution

P Patient Information

N Patient ICN

L List Telehealth Stop Codes

S Telehealth Stop Code Lookup

SN Station Number (Time Sensitive)

> R Clinic Schedule Queuing Report

Search Option or (Q)uit: R Clinic Schedule Queuing Report

TMP Clinic Schedule Edit Transaction List

Select one of the following:

O ONE CLINIC

A ALL CLINICS

ONE CLINIC OR ALL: A// ONE CLINIC

Select CLINIC NAME:

DEVICE: HOME// 0;132;66 HOME (CRT)

TMP Clinic Schedule Edit Transaction List APR 27, 2023 PAGE: 1

CLINIC:

DATE DAY OF WEEK BLOCK/UNBLOCK ACTION MODIFIED MODIFIED BY

------------ ----------- ------------- ----------- --------------------- --------------------

OCT 24, 2022 MONDAY UNBLOCK SENT OCT 18, 2022@14:45:07 XXXXXX,XXXXX,X

OCT 25, 2022 TUESDAY UNBLOCK SENT OCT 18, 2022@14:45:07 XXXXX

OCT 26, 2022 WEDNESDAY UNBLOCK SENT OCT 18, 2022@14:45:07 XXXXX

OCT 27, 2022 THURSDAY UNBLOCK SENT OCT 18, 2022@14:45:07 XXXXX

OCT 28, 2022 FRIDAY UNBLOCK SENT OCT 18, 2022@14:45:07 XXXXX

OCT 29, 2022 SATURDAY UNBLOCK SENT OCT 18, 2022@15:24:37 XXXXX

OCT 31, 2022 MONDAY UNBLOCK SENT OCT 18, 2022@14:45:07 XXXXX

NOV 01, 2022 TUESDAY UNBLOCK SENT OCT 18, 2022@14:45:07 XXXXX

NOV 01, 2022 TUESDAY BLOCK OFFSET NOV 01, 2022@11:33:28 XXXXX

NOV 01, 2022 TUESDAY UNBLOCK OFFSET NOV 01, 2022@11:33:28 XXXXX

NOV 01, 2022 TUESDAY BLOCK OFFSET NOV 01, 2022@11:33:48 XXXXX

NOV 01, 2022 TUESDAY UNBLOCK OFFSET NOV 01, 2022@11:33:48 XXXXX

NOV 02, 2022 WEDNESDAY UNBLOCK SENT OCT 18, 2022@14:45:07 XXXXX

NOV 03, 2022 THURSDAY UNBLOCK SENT OCT 18, 2022@14:45:07 XXXXX

NOV 04, 2022 FRIDAY UNBLOCK SENT OCT 18, 2022@14:45:07 XXXXX

NOV 05, 2022 SATURDAY UNBLOCK SENT OCT 18, 2022@15:24:37

END OF REPORT

# Telehealth Stop Code Add/Edit \[SD TELE STOP CODE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the Holder of the SDTOOL key to Add or Edit the Stop Codes in the SD TELE HEALTH STOP CODE FILE (#40.6), which is responsible for two Real-Time Updates sent to the Telehealth Management Platform (TMP):

Example 1: Adding new stop code

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>ST</strong> Telehealth Stop Code Add/Edit</p>
<p>Enter Stop Code: <strong>311</strong></p>
<p>This stop code is NOT in the file, do you want to add it? NO// <strong>Y</strong> YES</p>
<p>STOP Code: 311 has been Added!</p>
<p>Do you want to edit another stop code? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example 2: Delete existing stop code

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>R ClinicSchedule Queuing Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>ST</strong> Telehealth Stop Code Add/Edit</p>
<p>Enter Stop Code: <strong>311</strong></p>
<p>This stop code is already in the file, do you want to delete it? NO// <strong>Y</strong> YES</p>
<p>STOP Code: 311 has been Deleted!</p>
<p>Do you want to edit another stop code? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# VistA-Telehealth Clinic Update \[SD TELE CLN UPDATE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the Holder of the SDTOOL key to send clinic update message(s) from VistA to TMP without a need to edit the Clinic Profile. The option allows to send clinic update for specific clinic or a list of clinics that meet selected options.

Example 1: Send update for selected clinic

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>CLN</strong> VistA-Telehealth Clinic Update</p>
<p>VistA Real-Time Clinic Updates</p>
<p>Select (C)linic, (S)top Code or (Q)uit: C// linic</p>
<p>Select Clinic: XXXX/XXX/XX</p>
<p>Another one:</p>
<p>===============================================================================</p>
<p>Clinic: XXXX/XXX/XX</p>
<p>===============================================================================</p>
<p>Sending HL7 message for Clinic: XXXX/XXX/XX</p>
<p>Press &lt;Enter&gt; to continue</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example 2: Send update for all clinics that meet specific criteria

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>CLN</strong> VistA-Telehealth Clinic Update</p>
<p>VistA Real-Time Clinic Updates</p>
<p>Select (C)linic, (S)top Code or (Q)uit: C// <strong>S</strong> Stop Code</p>
<p>(A)ctive Clinics, (I)nactive Clinics, (B)oth: A// ctive</p>
<p>Select division: ALL// ?</p>
<p>ENTER:</p>
<p>- Return for all divisions, or</p>
<p>- A division and return when all divisions have been selected--limit 20</p>
<p>Imprecise selections will yield an additional prompt.</p>
<p>(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)</p>
<p>Answer with MEDICAL CENTER DIVISION NUM, or NAME, or FACILITY NUMBER, or</p>
<p>TREATING SPECIALTY</p>
<p>Do you want the entire 16-Entry MEDICAL CENTER DIVISION List?</p>
<p>Select division: ALL//</p>
<p>Select Telehealth Stop Code: <strong>103</strong></p>
<p>Select another Telehealth Stop Code:</p>
<p>===============================================================================</p>
<p>Clinic: 913 (103/ ) NHM/TELE TRIAGE/DAYS-X</p>
<p>Clinic: 915 ( /103) NHM/TELE TRIAGE/NIGHTS-X</p>
<p>Clinic: 1976 (103/802) NHM/DAYTON TELE TRIAGE(631)-X</p>
<p>Clinic: 7479 (103/117) NHM/TELE TRIAGE/RN DAYS-X</p>
<p>===============================================================================</p>
<p>Sending HL7 message for Clinic: 913-NHM/TELE TRIAGE/DAYS-X</p>
<p>Sending HL7 message for Clinic: 915-NHM/TELE TRIAGE/NIGHTS-X</p>
<p>Sending HL7 message for Clinic: 1976-NHM/DAYTON TELE TRIAGE(631)-X</p>
<p>Sending HL7 message for Clinic: 7479-NHM/TELE TRIAGE/RN DAYS-X</p>
<p>Total number of clinics updated: 4</p>
<p>Press &lt;Enter&gt; to continue</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Provider Add/Edit \[SD PROVIDER ADD/EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides holder of the SDTOOL key with the ability to add or edit the providers associated with a selected clinic.

Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>PR</strong> Provider Add/Edit</p>
<p>CAUTION: DO NOT USE - Default Provider for setting up a Shared or Patient Site</p>
<p>Telehealth VistA Clinics.</p>
<p>Select Clinic:</p>
<p>Providers associated with this clinic:</p>
<p>- &lt;&lt; Default &gt;&gt;</p>
<p>DEFAULT PROVIDER: TEST,PROVIDER TP 192 OI&amp;T STAFF</p>
<p>EMAIL ADDRESS:</p>
<p>Select PROVIDER:</p>
<p>PROVIDER:</p>
<p>DEFAULT PROVIDER: YES//</p>
<p>Select PROVIDER:</p>
<p>Press &lt;Enter&gt; to continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Default Provider Bulk Update \[SD DEFAULT PROVIDER UPDATE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides users with the ability to bulk update Default Provider for dedicated clinics. A dedicated clinic is one in which only one provider is found with a Default Provider flag. The bulk update operation should be allowed on dedicated clinics only. If a clinic is shared clinic with multiple providers, no updates will take place.

Telehealth patient clinics are restricted. The Bulk Update operation will not act upon inactive clinics. If attempted, the message “Provider update on inactive clinics is not allowed.” will be returned. The Bulk Update operation also will not act upon Telehealth patient sites. In this case the message “Telehealth Patient Site Stop Codes are not allowed for Bulk Default Provider Update” will be displayed.

Example \#1: Search the option using Clinic option to select multiple clinics to update the default provider field for them. (Selected clinics with no Default provider entered and one entry in the PROVIDER multiple found and marked as default will be updated).

INQ Telehealth Inquiries

ST Telehealth Stop Code Add/Edit

CLN VistA-Telehealth Clinic Update

PR Provider Add/Edit

DEF Default Provider Bulk Update

MSN Clinics Missing Station Number Report

DISP Display Clinic Availability Report

Select Telehealth Management Toolbox \<TEST ACCOUNT\> Option: def Default Provider Bulk Update

Bulk update for Default Provider field

Select (C)linic, (S)top Code, (P)rovider, or (Q)uit: C// c Clinic

Select Clinic: \`

Another one:\`

Another one:\` NHM/ECHO

Another one:

===============================================================================

1666 NHM/ECHO (303/115)

--- No action taken, default provider is already set.

2070 (115/136)

\>\>\> Default Provider is set to:

2072 WOPC/TH/PHARM/GENERAL/PRO-X (118/)

--- No action taken, no default provider found.

Total number of clinics updated 1 out of 3

Press \<Enter\> to continue

Example \#2: Search the option by Stop code option to select multiple clinics to update the default provider field for them.

Bulk update for Default Provider field

Select (C)linic, (S)top Code, (P)rovider, or (Q)uit: C// s Stop Code

(P)rimary Stop Code, (S)econdary Stop Code: P// s Secondary Stop Code

Select Telehealth Stop Code: 115

Select another Telehealth Stop Code:

===============================================================================

1666 NHM/ECHO (303/115)

--- No action taken, default provider is already set.

Total number of clinics updated 0 out of 1

Press \<Enter\> to continue

Example \#3: Search the option using the ‘Provider’ option to select multiple clinics to update the default provider field for them.

(Note: Dedicated clinics in this case are clinics assigned the selected Provider and has no Default provider field assigned and PROVIDER multiple has one entry and flagged as default with be updated).

Bulk update for Default Provider field

Select (C)linic, (S)top Code, (P)rovider, or (Q)uit: C// p Provider

Select Provider:

Another one:

===============================================================================

1666 NHM/ECHO (303/115)

\>\>\> Default Provider set to:

2070 GOPC/TH/BARIATRIC GRP/WROX/PAT (115/136)

\>\>\> Default Provider set to:

6497 NHM/TH/SCI/PROVIDER-X (118/693)

--- No action taken, multiple providers assigned.

Total number of clinics updated 2 out of 3

Press \<Enter\> to continue

# Clinics Missing Station Number Report \[SD MISSING STATION NUMBER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report displays any local clinics that do not point to a valid Station Number. This report has two filters. The first is Active Clinics, Inactive Clinics or Both. The second is a choice of Clinic Types. The options are: (C)linic, (M)odule, (W)ard, (Z)Other Location, (N)on-Clinic Stop, (F)ile Area, (I)maging, Operating (R)oom or (A)ll. See an example below.

Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION NAME: SDMGR Scheduling Manager's Menu</p>
<p>Scheduling Version 5.3</p>
<p>ACR Ambulatory Care Reporting Menu ...</p>
<p>AM Appointment Management</p>
<p>CONS Consult/Request Tracking User Menu ...</p>
<p>SDRR Recall Reminder Main Menu ...</p>
<p>Appointment Menu ...</p>
<p>Automated Service Connected Designation Menu ...</p>
<p>Outputs ...</p>
<p>Supervisor Menu ...</p>
<p>Telehealth Management Toolbox ...</p>
<p>VistA Scheduling GUI Resource Mgmt Report Data</p>
<p>Select Scheduling Manager's Menu &lt;TEST ACCOUNT&gt; Option: TELEhealth Management To</p>
<p>olbox</p>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: MSN Clinics Missing</p>
<p>Station Number Report</p>
<p>CLINICS THAT ARE MISSING STATION NUMBER</p>
<p>List which clinics - (A)ctive, (I)nactive or (B)oth ? B// OTH</p>
<p>List which clinic types - (C)linic, (M)odule, (W)ard, (Z)Other Location, (N)on-C</p>
<p>linic Stop, (F)ile Area, (I)maging, Operating (R)oom or (A)ll ? C// ALL</p>
<p>DEVICE: HOME// 0;132;66 HOME (CRT)</p>
<p>CLINICS THAT ARE MISSING STATION NUMBER DATE: 04/07/22 PAGE: 1</p>
<p>CLINIC TYPE: ALL</p>
<p>BOTH ACTIVE AND INACTIVE CLINICS</p>
<p>CLINIC CLINIC NAME ABR TYPE INST DIV PRI SC SEC SC NCNT STATION</p>
<p>------- ------------------------------- ----------- ---------------- ------- ---------------- ------ ------ ---- -------</p>
<p>3 MISSING LOCATION IEN=3</p>
<p>10 Missing Hospital Location</p>
<p>1500 ZZCHY LORI HEARING AID ZZLHAC CLINIC 117 428 N</p>
<p>2185 ZZOUTSIDE CHY RAD CLINIC</p>
<p>2187 OUTSIDE BASE RAD CLINIC 379 112 N</p>
<p>2188 OUTSIDE BASE NUC MED CLINIC 379 116 N</p>
<p>2189 OUTSIDE BASE ULTRASOUND CLINIC 379 122 N</p>
<p>2190 OUTSIDE BASE MRI CLINIC 379 338 N</p>
<p>2191 OUTSIDE BASE CT CLINIC 379 337 N</p>
<p>2192 OUTSIDE BASE VAS CLINIC 379 188 N</p>
<p>2193 OUTSIDE BASE MAM CLINIC 379 266 N</p>
<p>2659 ZZFTC PC KELLEY CLINIC N</p>
<p>3382 zzchy test CLINIC N</p>
<p>3559 OUTSIDE US IMAGING</p>
<p>3621 ZZSTR TELE DERM IFC DNVR PAT CLINIC N</p>
<p>3742 ZZSET CLINIC</p>
<p>4179 ZZSMITH PC ZZSMITH CLINIC</p>
<p>4351 ZZZZ 1 CLINIC</p>
<p>4476 ZZDONT KNOW WHAT THIS IS CLINIC</p>
<p>4864 NEW TH TEST CLINIC</p>
<p>10998</p>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
<p>DEF Default Provider Bulk Update</p>
<p>MSN Clinics Missing Station Number Report</p>
<p>DISP Display Clinic Availability Report</p>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Display Clinic Availability Report \[SD DISPLAY AVAIL REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is an existing option on other Scheduling menus and placed here for convience for TMP users. It behaves as it has in the past. See an example below.

Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: DISP Display Clinic</p>
<p>Availability Report</p>
<p>Select division: ALL//</p>
<p>Select clinic: ALL// RAVI</p>
<p>1 RAVI 692 - 442</p>
<p>2 RAVI PAT 442</p>
<p>CHOOSE 1-2: 1 RAVI 692 - 442</p>
<p>Select another clinic: RAVI</p>
<p>1 RAVI 692 - 442</p>
<p>2 RAVI PAT 442</p>
<p>CHOOSE 1-2: 2 RAVI PAT 442</p>
<p>Select another clinic:</p>
<p> Date Range Selection </p>
<p>Beginning DATE : T (FEB 17, 2022)</p>
<p>Ending DATE : T+6 (FEB 23, 2022)</p>
<p>INCLUDE CANCELLATIONS AND/OR NO-SHOWS? No// (No)</p>
<p>DEVICE: HOME// HOME (CRT) Right Margin: 80//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>FEB 17,2022@11:30</p>
<p>FORT COLLINS</p>
<p>RAVI 692 - 442</p>
<p>FEBRUARY 2022</p>
<p>TIME|8 |9 |10 |11 |12 |1 |2 |3 |4 |5 |6</p>
<p>DATE| | | | | | | | | | |</p>
<p>TH 17[j j j|9 9 9|j j j|j j j] [j j j|j j j|j j j]</p>
<p>FR 18[1 1 1|1 1 1|1 1 1|1 1 1]</p>
<p>SA 19[1 1 1|1 1 1|1 1 1|1 1 1]</p>
<p>SU 20[1 1 1|1 1 1|1 1 1|1 1 1]</p>
<p>MO 21[j j j|j j j|j j j|j j j] [j j j|j j j|j j j]</p>
<p>TU 22[1 1 1|1 1 1|1 1 1] [1 1 1|1 1 1|1 1 1|1 1 1]</p>
<p>WE 23[5 5 5|5 5 5|5 5 5|5 5 5|5 5 5|5 5 5|5 5 5|5 5 5]</p>
<p>PRESS RETURN TO CONTINUE OR ^ TO QUIT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>FOR CLINIC AVAILABILITY PATTERNS:</p>
<p>0-9 and j-z --denote available slots where j=10,k=11...z=26</p>
<p>A-W --denote overbooks with A being the first slot to be overbooked</p>
<p>and B being the second for that same time, etc.</p>
<p>*,$,!,@,# --denote overbooks or appts. that fall outside of a clinic's</p>
<p>regular hours</p>
<p>PRESS RETURN TO CONTINUE OR ^ TO QUIT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>RAVI 692 - 442</p>
<p>FEBRUARY 2022</p>
<p>THURSDAY FEB 17,2022</p>
<p>9:15 AM *6780 (60) MINUTES</p>
<p>PRESS RETURN TO CONTINUE OR ^ TO QUIT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>RAVI 692 - 442</p>
<p>FEBRUARY 2022</p>
<p>FOR INDIVIDUAL APPOINTMENT LISTINGS:</p>
<p>* --UNSCHEDULED VISIT</p>
<p>PRESS RETURN TO CONTINUE OR ^ TO QUIT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>FEB 17,2022@11:30</p>
<p>GREELEY</p>
<p>RAVI PAT 442</p>
<p>FEBRUARY 2022</p>
<p>TIME |8 |9 |10 |11 |12 |1 |2 |3 |4</p>
<p>DATE | | | | | | | | |</p>
<p>TH 17 [j 9 9 9|9 j j j|j j j j|j j j j|j j j j|j j j j|j j j j|j j j j]</p>
<p>MO 21 [j j j j|j j j j|j j j j|j j j j|j j j j|j j j j|j j j j|j j j j]</p>
<p>TU 22 [j j 9 9|9 9 j j|j j j j|j j j j|j j j j|j j j j|j j j j|j j j j]</p>
<p>WE 23 [j j j j|j j j j|j j j j|j j j j|j j j j|j j j j|j j j j|j j j j]</p>
<p>Clinic --inactive from 05/07/2013 to 06/13/2019</p>
<p>FOR CLINIC AVAILABILITY PATTERNS:</p>
<p>0-9 and j-z --denote available slots where j=10,k=11...z=26</p>
<p>A-W --denote overbooks with A being the first slot to be overbooked</p>
<p>and B being the second for that same time, etc.</p>
<p>*,$,!,@,# --denote overbooks or appts. that fall outside of a clinic's</p>
<p>regular hours</p>
<p>PRESS RETURN TO CONTINUE OR ^ TO QUIT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Clinics With Institutional Discrepancy \[SD INSTITUTION DISCREPANCY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is a Missing Institution Report in the VistA Telehealth Management Toolbox so that a user can see which clinics are missing an Institution due to discrepancies found between the Medical Center Division and the Institution File Pointer.

Example:

Select Telehealth Management Toolbox \<TEST ACCOUNT\> Option: SID Clinics With Institutional Discrepancy

CLINICS THAT HAVE AN INSTITUTIONAL DISCREPANCY

List which clinics - (A)ctive, (I)nactive or (B)oth ? B// OTH

Select (C)linic, (S)top Code or (Q)uit: C// LINIC

CLINIC NAME or ALL: CHY HEAR

Press Enter for ALL divisions or

Select DIVISION: ALL//

Select (D)iscrepancy or (A)ll: D// ISCREPANCY

DEVICE: HOME// 0;132;60 HOME (CRT)

CLINICS WITH INSTITUTIONAL DISCREPANCY DATE: 01/29/24 PAGE: 1

BOTH ACTIVE AND \*INACTIVE CLINICS

CLINICS BEGINNING WITH "CHY HEAR"

CLINICS WITH DISCREPANCY ONLY

DIVISION: ALL

Station Medical Center Derived Station

Clinic Name IEN \###/### Number Division Institution Number Institution

------------------------------ ------- -------- -------- ----------------------------------- ----------- ---------- -----------

CHY HEARING AID DISP 3 3490 134/ CHEYENNE VAMROC 442 442

CHY HEARING AID FOLLOW UP 1 EH 4703 134/428 CHEYENNE VAMROC 442 442

CHY HEARING AID FOLLOW UP 2 2411 134/428 CHEYENNE VAMROC 442 442

CHY HEARING AID FOLLOW UP 3 4418 134/428 CHEYENNE VAMROC 442 442

\*CHY HEARING AID FOLLOW UP 6 EH 4420 134/428 CHEYENNE VAMROC 442 442

\*\* END \*\*