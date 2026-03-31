---
title: TMP Version 5.0 VistA Patch 806 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: VistA Patch 806
app_code: TMP
app_name: Telehealth Management Platform
section: CLI
app_status: active
pkg_ns: TMP
patch_ver: 5.0
patch_id: TMP*5.0
group_key: "TMP:TMP:5.0"
file_numbers: []
security_keys: []
menu_options: 0
description: The Telehealth Management Program (TMP) integrates with Veterans Health Information Systems and Technology Architecture (VistA) to schedule, cancel or update appointments in support of Telehealth services provided by the VHA. When an appointment is made or canceled on TMP, a message is sent to VistA
audience: 
keywords: 
  - stop
  - code
  - telehealth
  - strong
  - clinic
  - table
  - blockquote
  - telephone
  - vista
  - edit
page_count: 0
word_count: 3499
section_count: 1
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/TMP_VistA_UM_Manual_SD_53_806.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/TMP_VistA_UM_Manual_SD_53_806.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=231"
---

Department of Veterans AffairsScheduling PackageTelehealth Management Platform (TMP) VistA

> User Manual

![](tmp-version-5-0-vista-patch-806-user-guide/001.png)

October 2021Version 5.3Revision History

| Date     | Version | Description                | Author           |
|--------------|-------------|--------------------------------|----------------------|
| October 2021 | 1.02        | Changes of SD\*5.3\*780 patch  | LIBERTY ITS          |
| August 2021  | 1.01        | Changes of SD\*5.3\*779 patch  | LIBERTY ITS          |
| May 2021     | 1.0         | Initial version for submission | \[Development Team\] |
|              |             |                                |                      |

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
<th><p>Select Supervisor Menu &lt;TEST ACCOUNT&gt; Option: <strong>TELE</strong>health Management Toolbox</p>
<blockquote>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
</blockquote>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>INQ</strong> Telehealth Inquiries</p>
<p>Telehealth Inquiries</p>
<p>Select one of the following:</p>
<p>C Clinic</p>
<p>M Medical Center Division</p>
<p>I Institution</p>
<p>P Patient Information</p>
<p>L List Telehealth Stop Codes</p>
<p>S Telehealth Stop Code Lookup</p>
<p>Search Option or (Q)uit: <strong>C</strong> Clinic</p>
<p>Select CLINIC: <strong>`2070</strong> GOPC/TH/BARIATRIC GRP/WROX/PAT SUSAN,PROVIDER</p>
<p>===============================================================================</p>
<p>Clinic : 2070-GOPC/TH/BARIATRIC GRP/WROX/PAT</p>
<p>Default Provider :</p>
<p>Provider : 520691300-FORSTER,OFELIA E &lt;&lt; Default &gt;&gt;</p>
<p>Medical Division : 1-NORTHAMPTON</p>
<p>Institution : 631-VA CNTRL WSTRN MASSCHUSETS HCS</p>
<p>Station Number : 631</p>
<p>Stop Code : 120-HOME TREATMENT SERVICES (118)</p>
<p>Credit Stop Code : 525-PALLIATIVE CARE (353)</p>
<p>Country : 1-USA</p>
<p>Location Timezone : 2-EASTERN</p>
<p>Timezone Exception:</p>
<p>Overbooks per day : 20</p>
<p>===============================================================================</p>
<p>Select CLINIC: <strong>^</strong></p></th>
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
<th><blockquote>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
</blockquote>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>INQ</strong> Telehealth Inquiries</p>
<p>Telehealth Inquiries</p>
<p>Select one of the following:</p>
<p>C Clinic</p>
<p>M Medical Center Division</p>
<p>I Institution</p>
<p>P Patient Information</p>
<p>L List Telehealth Stop Codes</p>
<p>S Telehealth Stop Code Lookup</p>
<p>Search Option or (Q)uit: <strong>M</strong> Medical Center Division</p>
<p>Select MEDICAL CENTER DIVISION NAME: NOR-PRRTP 631PA</p>
<p>===============================================================================</p>
<p>Medical Division : 3-NOR-PRRTP</p>
<p>Facility Number : 631PA</p>
<p>Institution : 11574-NORTH-MAIN-MASSCHST-PRRTP</p>
<p>===============================================================================</p>
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
<th><blockquote>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
</blockquote>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>INQ</strong> Telehealth Inquiries</p>
<p>Telehealth Inquiries</p>
<p>Select one of the following:</p>
<p>C Clinic</p>
<p>M Medical Center Division</p>
<p>I Institution</p>
<p>P Patient Information</p>
<p>L List Telehealth Stop Codes</p>
<p>S Telehealth Stop Code Lookup</p>
<p>Search Option or (Q)uit: <strong>I</strong> Institution</p>
<p>Select INSTITUTION NAME: CENTRAL OFFICE DC CO 101</p>
<p>===============================================================================</p>
<p>Name : 101-CENTRAL OFFICE</p>
<p>City : WASHINGTON</p>
<p>State : 11-DISTRICT OF COLUMBIA</p>
<p>District : 29</p>
<p>VA region IEN :</p>
<p>Location Timezone : 2-EASTERN</p>
<p>Timezone Exception:</p>
<p>Country : 1-USA</p>
<p>Station # : 101</p>
<p>Facility DEA #: :</p>
<p>Facility Exp. date::</p>
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

L List Telehealth Stop Codes

S Telehealth Stop Code Lookup

Search Option or (Q)uit: P Patient Information

Select Patient: kathleen,SOLOMON L KATHLEEN,SOLOMON L 6-8-37 10174678

0 NO NSC VETERAN DC

\>\>\> Active Patient Record Flag(s):

\<BEHAVIORAL\> CATEGORY I

Do you wish to view active patient record flag details? Yes// n (No)

Enrollment Priority: Category: NOT ENROLLED End Date: 11/02/2010

\*\*\* Patient Requires a Means Test \*\*\*

Primary Means Test Required from AUG 23,2019

Enter \<RETURN\> to continue.

===============================================================================

Number (IEN) : 15937

Name :, KATHLEEN SOLOMON L

Sex : MALE

Date of Birth : JUN 8,1937

SSN : 101-74-6780

Full ICN : 1008655794V858823

Integrated Control: 1008655794

ICN Checksum : 858823

Full ICN History : 4420011765V792817

1008655794V858823

Deceased Date :

===============================================================================

Select Patient:

Example 5: List Telehealth Stop Codes

The List Telehealth Stop Codes Query allows the user to view the current contents of the SD TELE HEALTH STOP CODE FILE (#40.6).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
</blockquote>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>INQ</strong> Telehealth Inquiries</p>
<p>Telehealth Inquiries</p>
<p>Select one of the following:</p>
<p>C Clinic</p>
<p>M Medical Center Division</p>
<p>I Institution</p>
<p>P Patient Information</p>
<p>L List Telehealth Stop Codes</p>
<p>S Telehealth Stop Code Lookup</p>
<p>Search Option or (Q)uit: <strong>L</strong> List Stop codes</p>
<p>===============================================================================</p>
<p>Stop Code: 103 &gt; TELEPHONE TRIAGE</p>
<p>Stop Code: 111 &gt; TELE-PATHOLOGY</p>
<p>Stop Code: 118 &gt; HOME TREATMENT SERVICES</p>
<p>Stop Code: 136 &gt; TELE POST DEPLOY PT SITE</p>
<p>Stop Code: 137 &gt; TELE POST DEPLOY PROV SITE</p>
<p>Stop Code: 147 &gt; TELEPHONE/ANCILLARY</p>
<p>Stop Code: 148 &gt; TELEPHONE/DIAGNOSTIC</p>
<p>Stop Code: 160 &gt; CLINICAL PHARMACY</p>
<p>Stop Code: 169 &gt; TELEPHONE/CHAPLAIN</p>
<p>Stop Code: 178 &gt; TELEPHONE HBPC</p>
<p>Stop Code: 179 &gt; RT CLIN VID CARE HOME</p>
<p>Stop Code: 181 &gt; TELEPHONE/DENTAL</p>
<p>Stop Code: 182 &gt; TELEPHONE CASE MANAGEMENT</p>
<p>Stop Code: 184 &gt; CARE/CASE MANAGER</p>
<p>Stop Code: 185 &gt; NURSE PRACTITIONER</p>
<p>Stop Code: 186 &gt; PHYSICIAN ASSISTANT</p>
<p>Stop Code: 189 &gt; STORE &amp; FORWARD HOME PROV SITE</p>
<p>Stop Code: 199 &gt; TELEPHONE POLYTRAUMA/TBI</p>
<p>Stop Code: 216 &gt; TELEPHONE/REHAB AND SUPPORT</p>
<p>Stop Code: 221 &gt; TELEPHONE VIST</p>
<p>Stop Code: 224 &gt; TELEPHONE SCI</p>
<p>Stop Code: 225 &gt; SCI TELEHEALTH VIRTUAL</p>
<p>Stop Code: 229 &gt; TELEPHONE/BLIND REHAB PROGRAM</p>
<p>Stop Code: 322 &gt; COMP WOMEN'S HLTH</p>
<p>Stop Code: 324 &gt; TELEPHONE/MEDICINE</p>
<p>Stop Code: 325 &gt; TELEPHONE/NEUROLOGY</p>
<p>Stop Code: 326 &gt; TELEPHONE/GERIATRICS</p>
<p>Stop Code: 338 &gt; TELEPHONE PRIMARY CARE</p>
<p>Stop Code: 348 &gt; PRIMARY CARE SHARED APPT</p>
<p>Stop Code: 371 &gt; HT SCREENING</p>
<p>Stop Code: 424 &gt; TELEPHONE/SURGERY</p>
<p>Stop Code: 425 &gt; TELEPHONE/PROSTHETICS/ORTHOTIC</p>
<p>Stop Code: 428 &gt; TELEPHONE/OPTOMETRY</p>
<p>Stop Code: 440 &gt; TELE FIT &amp; ADJUST PROV SITE</p>
<p>Stop Code: 441 &gt; TELEPHONE ANESTHESIA</p>
<p>Stop Code: 444 &gt; C&amp;P VIA CVT PT SITE</p>
<p>Stop Code: 445 &gt; C&amp;P VIA CVT PROV SITE</p>
<p>Stop Code: 446 &gt; IDES VIA CVT PT SITE</p>
<p>Stop Code: 447 &gt; IDES VIA CVT PROV SITE</p>
<p>Stop Code: 490 &gt; TELETRANSPLANT PT SITE</p>
<p>Stop Code: 491 &gt; TELETRANSPLANT PROV SITE</p>
<p>Stop Code: 502 &gt; MENTAL HEALTH CLINIC - IND</p>
<p>Stop Code: 527 &gt; TELEPHONE MH</p>
<p>Stop Code: 528 &gt; TELEPHONE HCMI</p>
<p>Stop Code: 530 &gt; TELEPHONE/HUD-VASH</p>
<p>Stop Code: 534 &gt; MH INTGRTD CARE IND</p>
<p>Stop Code: 536 &gt; TELEPHONE/MH VOC ASSISTANCE</p>
<p>Stop Code: 542 &gt; TELEPHONE/PTSD</p>
<p>Stop Code: 545 &gt; TELEPHONE SUD</p>
<p>Stop Code: 546 &gt; TELEPHONE ICMHR</p>
<p>Stop Code: 579 &gt; TELEPHONE/PSYCHOGERIATRICS</p>
<p>Stop Code: 584 &gt; TELEPHONE PRRC</p>
<p>Stop Code: 597 &gt; TELEPHONE - RRTP</p>
<p>Stop Code: 611 &gt; TELEPHONE/DIALYSIS</p>
<p>Stop Code: 644 &gt; NC RTCV TELECARE PT LOC</p>
<p>Stop Code: 645 &gt; NC RTCV TELECARE PRV LOC</p>
<p>Stop Code: 646 &gt; NC S&amp;F TELECARE PT LOC</p>
<p>Stop Code: 648 &gt; RT CVT W NONVAMC PROVID LOC</p>
<p>Stop Code: 674 &gt; ADMIN PAT ACTIVTIES (MASNONCT)</p>
<p>Stop Code: 679 &gt; NC CVT TO HOME PROVID LOC</p>
<p>Stop Code: 680 &gt; HCBC ASSESSMENT</p>
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
<p>Stop Code: 698 &gt; SF TELECARE FROM NONVAMC PROV</p>
<p>Stop Code: 699 &gt; CVT EMERGENCY CONSULT</p>
<p>Stop Code: 708 &gt; TELE SMOKE CESS PROV SITE</p>
<p>Stop Code: 718 &gt; EYE TELE SCREENING</p>
<p>Stop Code: 719 &gt; MHV SECURE MESSAGING</p>
<p>Stop Code: 723 &gt; OEND ED CVT PT SITE</p>
<p>Stop Code: 724 &gt; OEND ED CVT PRV SITE</p>
<p>Stop Code: 901 &gt; TELE-ICU PATIENT SITE</p>
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
<th><blockquote>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
</blockquote>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>INQ</strong> Telehealth Inquiries</p>
<p>Telehealth Inquiries</p>
<p>Select one of the following:</p>
<p>C Clinic</p>
<p>M Medical Center Division</p>
<p>I Institution</p>
<p>P Patient Information</p>
<p>L List Telehealth Stop Codes</p>
<p>S Telehealth Stop Code Lookup</p>
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
<th><blockquote>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
</blockquote>
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
<th><blockquote>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
</blockquote>
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
<th><blockquote>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
</blockquote>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>CLN</strong> VistA-Telehealth Clinic Update</p>
<p>VistA Real-Time Clinic Updates</p>
<p>Select (C)linic, (S)top Code or (Q)uit: C// linic</p>
<p>Select Clinic: ZZSA/TEL/PM</p>
<p>Another one:</p>
<p>===============================================================================</p>
<p>Clinic: 1108 ZZSA/TEL/PM</p>
<p>===============================================================================</p>
<p>Sending HL7 message for Clinic: ZZSA/TEL/PM</p>
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
<th><blockquote>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
</blockquote>
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
<th><blockquote>
<p>INQ Telehealth Inquiries</p>
<p>ST Telehealth Stop Code Add/Edit</p>
<p>CLN VistA-Telehealth Clinic Update</p>
<p>PR Provider Add/Edit</p>
</blockquote>
<p>Select Telehealth Management Toolbox &lt;TEST ACCOUNT&gt; Option: <strong>PR</strong> Provider Add/Edit</p>
<p>CAUTION: DO NOT USE - Default Provider for setting up a Shared or Patient Site</p>
<p>Telehealth VistA Clinics.</p>
<p>Select Clinic: RAVI 692 - 442 BONTEMPO,PHIL M</p>
<p>DEFAULT PROVIDER: TEST,PROVIDER TP 192 OI&amp;T STAFF</p>
<p>EMAIL ADDRESS:</p>
<p>Select PROVIDER: ABIDE,JILLIAN R//</p>
<p>PROVIDER: ABIDE,JILLIAN R//</p>
<p>DEFAULT PROVIDER:</p>
<p>Select PROVIDER:</p>
<p>Press &lt;Enter&gt; to continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>