---
consolidated_title: "tmp user guide"
app_code: TMP
doc_type: UG
master_source: "TMP Version 4.0 Release 4.9.0.8 User Guide"
master_pub_date: October 2021
consolidated_from: 5 versions
prior_versions:
  - "TMP Version 1.5 Release 4.6 User Guide"
  - "TMP Version 2.0 Release 4.8 User Guide"
  - "TMP Version 3.0 Release 4.9.0.6 User Guide"
  - "TMP Version 6.0 Release 4.9.0.9 User Guide"
---

Department of Veterans AffairsScheduling PackageTelehealth Management Platform (TMP) VistA

> USER MANUAL

![](tmp-version-4-0-release-4-9-0-8-user-guide/001.png)

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

Name : KATHLEEN,SOLOMON L

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

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: TMP Version 1.5 Release 4.6 User Guide

## Benefits of the Telehealth Management Platform

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Telehealth staff will find that use of the Telehealth Management Platform results in significant time savings. Facility Telehealth Coordinators will be able to complete deployment checklists more quickly. Fewer steps are required for scheduling rooms, equipment, and support personnel. The result is a simpler and more efficient scheduling process. Veteran access to quality care will also benefit from the Telehealth Management Platform thanks to increased support for clinical and administrative staff.

Useful features provided by the Telehealth Management Platform include the following.

- VistA Integration: Appointments that are scheduled or canceled in the Telehealth Management Platform are automatically updated in VistA. Schedulers are no longer required to enter appointments into VistA after scheduling in the Telehealth Management Platform.
- Scheduling Packages: Tools that can be used to simplify scheduling and the creation of Telehealth Service Agreements.
- Resource Databases: Resource data (e.g. facility, site, group, components, users, teams, etc.) can be used to prepopulate required fields (such as for scheduling an appointment).
- Resource Groups: Technology, rooms, and users can be linked together as a Resource Group and simultaneously scheduled for an appointment (rather than having to schedule technology, rooms, and users separately); these Resource Groups can be viewed remotely, resulting in transparency of resource availability.
- Robust Reporting Capabilities: Reports can be easily generated at the National, Veterans Integrated Service Network (VISN) and Facility levels with desired levels of granularity.
- Proxy Add to VistA: Unregistered Veterans who are scheduled through the Telehealth Management Platform will automatically be proxy registered into the distant VistA station.
- Automatic Drug Enforcement Administration (DEA) Registration Verification: Providers who prescribe medication will receive email notifications that indicate if the patient site where the Veteran is being seen is DEA registered.
- Automatic Verification of Provider Proxy Privileging: Schedulers will be able to see if a provider is privileged at a secondary or patient facility when entering scheduling data.
- Automatic Calendar Updates for Home Visits: Veterans who are being seen in their home can receive email notifications with an internet calendar server (iCal) to save appointment information to their calendar.

## Getting Started with the Telehealth Management Platform

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To use the Telehealth Management Platform, a user account is required. Any user can request the level of access/security role of TMP user. However, only a Facility Telehealth Coordinator (FTC) and/or designee can request an account for a level of access/security role other than “TMP User”. To request a new user account, go to the [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) and select “New User Request” from the Resources sidebar. As part of this request, an appropriate level of access/security role must be selected. See Appendix A: Levels of Access/Security Roles for more information about the different levels of access/security roles and their associated abilities.

### Understanding the layout of the Telehealth Management Platform

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once an account has been created, a user can access the [Telehealth Management Platform](https://internalcrm.crm15.xrm.va.gov/TMP). The Telehealth Management Platform is organized by functions, with each function having a set of features. For example, “Create Technology Resource” is a feature of the “Resources” function.

The three primary functions and their main uses are:

- Resources, from which you can enter in clinics, rooms, and technologies that can be used to schedule telehealth appointments.
- Telehealth Administration, from which you can create the Scheduling Packages and Telehealth Service Agreements that are required before you can schedule telehealth appointments.
- Scheduling, from which you can schedule, cancel and manage telehealth appointments.

These functions are explained in more detail in the following sections.

## Creating Teams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users are organized into teams to provide patient-centered services. In telehealth, teams are assigned to accomplish specific tasks, streamline business and clinical operations and create an efficient telehealth program.

Teams are created to make it easier to give privileges and send notifications to users. For example, members of the Scheduling Team will be able to schedule appointments and will automatically receive notifications related to scheduling (e.g., cancelations).

Examples of when teams will be used include:

- To establish approval teams for Telehealth Service Agreements (TSAs).
- To share privileges across facilities.
- To send out scheduling notifications for appointments.
- To notify facility staff about a provider’s credentials and privileges.

Creating teams is handled by the National Telehealth Technology Helpdesk (NTTHD). To create a team, [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) with the type of team you want to create, including a list of members to be added to the team.

An outline of the different teams and staff that will typically be included as part of those teams is provided below. See Appendix B: Teams for more information about the teams.

- TMP Site Team
  - Staff are automatically added to this team by the site.
- TMP FTC Approval Group
  - Staff that typically need to be added to this team include FTCs and their designees.
- TMP Chief of Staff Approval Group
  - Staff that typically need to be added to this team include Facility Chiefs of Staff and their designees.
- TMP Service Chief of Staff Approval Group
  - Staff that typically need to be added to this team include Facility Service Chiefs and their designees.
- TSA Notification Group
  - Staff that typically need to be added to this team include any staff who need to be notified when a TSA is put into production.
- TMP Scheduler Group
  - Staff that typically need to be added to this team include schedulers.
- TMP Staff Team
  - Staff that typically need to be added to this team include Telehealth Clinical Technicians, who are automatically assigned to this team by their respective site.

## Managing Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Managing Resources is an important process as scheduling through the Telehealth Management Platform is dependent on having resources associated with the appointment.

The types of resources include Facilities & Sites, Users, Resource Groups, and Single Resources. Once resources are set up, they can be pulled into an appointment and managed through the Telehealth Management Platform.

Managing Resources requires the “Resource Manager” level of access/security role. Staff that will typically need this role include Telehealth Clinical Technicians and Facility Telehealth Coordinators.

### Facilities & Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans Integrated Service Networks, facilities, and sites are pre-loaded into the Telehealth Management Platform. A site is the physical location or virtual location (e.g. a Hub) where providers or patients are located.

> **NOTE:** *Parameters related to Veterans Integrated Service Networks, facilities and sites are locked and cannot be edited by a Facility Telehealth Coordinator. To modify information related to Veterans Integrated Service Networks, facilities and sites, a request must be submitted to the National Telehealth Technology Help Desk.*

### Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Staff can access the Telehealth Management Platform through user accounts. In turn, the Telehealth Management Platform allows staff to be managed through the user accounts. See Appendix A: Levels of Access/Security Roles for a review of the different user types. A user’s security role can be viewed on the User Record.

### Single Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Single Resources are classified as either “Infrastructure” or “Users”. Infrastructure resources include Rooms, Technology, and VistA Clinics. User Resources include Providers, Telepresenters, and Imagers. Note that “Components” (i.e. peripherals) can be created and associated with Technology Resources. Resources are pre-loaded into the Telehealth Management Platform. Each Single Resource has a calendar that shows availability. This results in a global inventory management system which assists with tracking and filtering available resources.

Once a resource is added to the Telehealth Management Platform, it is associated with the site and does not need to be added again. The resource can then by reserved when scheduling a telehealth appointment.

### Resource Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Resource Group is a collection of two or more resources that can be scheduled together. Once a Single Resource is created, it can be added to a “Resource Group”. A Resource Group reduces the number of resources that need to be added to a Scheduling Package and increases efficiency in scheduling.

“Paired Resource Groups” are Resource Groups made from different types of Single Resources to facilitate the creation of the Scheduling Package. The most common Resource Group, which includes a Provider and a VistA Clinic, is an example of a Paired Resource Group.

“Like Resource Groups” are Resource Groups that are made from the same type of Single Resource. A Resource Group that includes only Providers is considered a Like Resource Group, and would be used when multiple Providers use the same VistA Clinic.

### Managing Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Resources can be managed directly through TMP. Resources can be replaced, updated, or deactivated on all associated Resource Groups, Scheduling Packages and TSAs. Deactivated Resources may also be reactivated.

Deactivated Resources are not deleted; they remain in the Telehealth Management Platform but are not available for scheduling. A Resource that has been deactivated can be reactivated to make it available for scheduling.

If replacing, updating, or deactivating a resource that is associated with an appointment, the appointment must first be canceled. After canceling the appointment, the appropriate change can be made, and the appointment can then be rescheduled.

If a Resource which is scheduled for an appointment is modified without canceling and recreating the associated appointment, there is a risk that unavailable Resources will be scheduled for an appointment and result in a negative impact to the Veteran’s access of care.

A Resource can be managed by any user who from the same Site where the Resource is located.

### Inventory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All technology is initially imported into the Telehealth Mangaement Platform by the National Telehealth Tecnology Helpdesk (NTTHD). Sites and Facilities will not need to import technology, but may be required to validate the imported information.

To do so, it will be necessary to either:

- Match current technology within the system to what was imported into the Telehealth Management Platform

*OR*

- Create new technology when no technology to be matched exists

Validation only has to be performed at initial implementation of the Telehealth Management Platform; it is not an ongoing process.

Staging for Technology is tracked through the Telehealth Management Platform. In addition to supporting validation, the Telehealth Management Platform has a status field that shows if the Technology is in the acquisition process, deployment process, deployed or in the RMA process.

### Provider Virtual Medical Rooms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provider virtual medical rooms are for providers who use webcams to connect to clinic-based appointments. A provider virtual medical room is a static link saved to the provider’s TMP User Record. Provider virtual medical rooms must be requested from the National Telehealth Technology Help Desk (NTTHD).

## Scheduling Packages, TSAs and Additional Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Telehealth Administration is important as it allows telehealth agreements to be created, approved, and maintained. Information from the telehealth agreements can then be pulled when scheduling through the Telehealth Management Platform. The most commonly used features under the Telehealth Administration function are Scheduling Packages, Telehealth Service Agreements (TSAs), Credentialing and Privileging, and TSA Approval Process.

Managing Scheduling Packages requires the TMP Scheduling Package Manager level of access/security role and is typically needed by Facility Telehealth Coordinators.

Managing TSAs requires the TMP TSA Approver level of access/security role. Staff that will typically need these roles and to be added to these teams include Facility Telehealth Coordinators, Chiefs of Staff and Service Chiefs.

Further, the following teams must be created to complete the TSA Approval Process: TMP FTC Approval Group, TMP Service Chief Approval Group, Chief of Staff Approval Group and TSA Notification Team. Staff that will typically need these roles include Facility Telehealth Coordinators, Chiefs of Staff, Service Chiefs, and individuals that need to be notified of the TSA such as Credentialing and Privileging staff.

Managing Credentialing & Privileging requires the TMP Privileging level of access/security role. One team, the TMP Credentialing & Privileging Group, is also needed for managing privileging. Credentialing and privileging staff will typically need these security roles.

Managing Provider Performance Evaluations (PPE) requires the TMP PPE Feedback access/security role. One team, the TMP Service Chief Approval Group, is also needed for managing PPE Feedback. Staff that will typically need these roles include the Service Chief.

### Creating Scheduling Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Scheduling Packages are templates used to display information for the Provider Site and Patient Sites. There are two types of Scheduling Package options in TMP.

The first type of Scheduling Package option is called “Scheduling Packages” and is used for scheduling between a Provider site and Patient Sites. The second type of Scheduling Package option is called “TSAs” and is used to manage TSAs and Approvals for Interfacility service.

Provider information for a particular service and site only needs to be completed once on the Scheduling Package. Patient Site information, when needed, is completed when adding the Patient Site to the Scheduling Package. For example, a clinical cart might be added as a technology for the Patient Site.

TSAs are completed agreements that contain both provider site and patient site information. TSAs are required documents for telehealth care delivered between facilities and sites. TSAs provide clinical and administrative information to ensure quality care is being provided by the facility or site.

Completed TSAs convey important information between sites to ensure the Veteran receives the necessary care and the appointment goes smoothly. The completed TSA displays all clinical information specific to an appointment, including provider preference, clinical workflow, emergency procedures, contacts, and appointment instructions. Resources shared between sites are also documented by the TSA.

When an Intrafacility TSA is added to a Scheduling Package, no approval is required. Instead, notification emails are automatically sent to inform staff that the TSA has been added to the Scheduling Package.

Interfacility TSAs must go through the TSA Approval Process before they can be used to schedule telehealth appointments.

> **NOTE:** While Interfacility TSAs are routed through an approval and notification process, Intrafacility TSAs are not. For intrafacility TSAs, the Facility Telehealth Coordinator must pull a quarterly report on telehealth being conducted in their facility and submit it to the Chief of Staff.

### Interfacility TSA Approval Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The interfacility approval process automatically sends approval emails when an interfacility TSA is created. Approvers follow a link from the email to go directly to the TSA page on TMP. The Approvers can then approve or reject the TSA. The status of the TSA in TMP automatically will update to reflect the approval or denial.

The TSA remains in draft until it is completed. Once completed, the TSA Notification Team is alerted that that the TSA has been put into production for their Facility.

The Telehealth Management Platform further supports the TSA Approval Process through Reminder Emails, Audit History, Closed Activities, and Background Processes.

Reminder Emails allows the TSA Manager to send a reminder email to staff whose signature is needed to continue the approval process. Audit History is used to view changes made throughout the history of the TSA. Closed Activities are used to view emails that have been generated regarding a selected TSA. Background Processes is used to view the status of the TSA Approval Process.

### Credentialing and Privileging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All providers must be credentialed and privileged to practice at a VA facility. Telehealth enables the provision of clinical care across VA facility boundaries; the Telehealth Management Platform supports this by allowing receiving facilities to accept the provider’s privilege at their home facility.

The Home/Parent Privileging Record is the facility where the provider has full privileges. There can only be one Home/Parent Privileging Record for a telemedicine provider in the Telehealth Management Platform. If a provider holds full privileges at more than one facility, one of those facilities must be selected as the home location for the Home/Parent Privileging Record.

The Proxy/Secondary Privileging Record is for non-home facilities where the provider is privileged. A provider can only have one Proxy/Secondary Privileging Record per facility in the Telehealth Management Platform. A provider must have a Proxy/Secondary Privileging Record for a non-home facility to be scheduled for appointments at that facility.

When a provider is added to an Interfacility Scheduling Package in TMP, the FTC will notify the Credentialing and Privileging (C&P) office for the provider’s facility. The provider facility C&P office will then create a TMP Home/Parent privileging record.

When the Home/Parent record has been created, the FTC notifies the patient facility C&P office to create the Proxy/Secondary privileging record.

If there is a change of providers on a Scheduling Package, the appropriate staff are automatically notified via email. This includes the Facility Telehealth Coordinators and Service Chief Groups. A change in providers on a Scheduling Package requires a new Home/Parent Privileging Record and Proxy/Secondary Privileging Record for the new provider. The Home/Parent Privileging Record and Proxy/Secondary Privileging Record for the previous provider can then be deactivated.

### Professional Practice Evaluation (PPE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PPE Process is initiated to provide a feedback-based evaluation of a provider’s process. This process includes generating requests, to Facilities receiving telehealth Services from a provider, for feedback related to the provider’s practice.

The Telehealth Management Platform automatically acknowledges and logs such requests, and triggers a notification to the requesting Service Chief when all requests for feedback have been responded to.

## Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Scheduling through the Telehealth Management Platform is simplified by allowing resources and service agreements to be pulled into appointments. As the Telehealth Management Platform is integrated with VistA, scheduling through the Telehealth Management Platform automatically updates VistA. Scheduling is also facilitated through the use of calendars, which automatically verify that the required resources are available for a requested date. The most commonly used features under the Scheduling function are Clinic-Based Scheduling, VA Video Connect Scheduling, Completing Appointments, and Canceling Appointments. Clinic-Based scheduling is used to coordinate resources for an appointment between two VA Facilities. VA Video Connect scheduling is used to coordinate resources for an appointment between a VA Facility and a Veteran’s home. Both types of scheduling support individual and group appointments. Appointments can then be completed or canceled, as appropriate, after being scheduled through the Telehealth Management Platform.

Managing Scheduling, including Completing and Canceling Appointments, requires the TMP Scheduler and TMP Scheduling Team level of access/security role. Staff that will typically need these levels of access/security roles include Telehealth Clinical Technicians and Facility Telehealth Coordinators. Staff must take the VHA Scheduling Training before scheduling in the Telehealth Management Platform.

### Clinic-Based Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Telehealth Management Platform makes scheduling information available across Facilities, assisting with the scheduling process. Additionally, consults, workload, and documentation of clinical visits (for continuity of care) can be captured through the Telehealth Management Platform. This helps address scheduling challenges which require finding a day, time, and room with technology that fits the Veteran’s schedule, provider site’s schedule, and patient site’s schedule. The Telehealth Management Platform supports the following clinic-based appointments:

- Clinical Video Telehealth – Individual – Intrafacility
- Clinical Video Telehealth – Individual – Interfacility
- Clinical Video Telehealth – Group – Intrafacility
- Clinical Video Telehealth – Group – Interfacility
- Store-and-Forward Telehealth – Individual – Intrafacility
- Store-and-Forward Telehealth – Individual – Interfacility

### VA Video Connect Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA Video Connect appointments are beneficial as they facilitate Veteran access to VA healthcare. Veterans can engage with their healthcare team from anywhere, reducing the amount of travel required for healthcare.

The Telehealth Management Platform supports the following VA Video Connect appointments:

- VA Video Connect – Individual – Intrafacility
- VA Video Connect – Individual – Interfacility
- VA Video Connect – Group – Intrafacility

The Telehealth Management Platform also supports the creation of a Video On Demand (VOD). As part of the Video On Demand creation, the Telehealth Management Platform generates a link which is sent to both the provider and the patient.

To facilitate inviting family members of Veterans to a VA Video Connect appointment, a non-VA email field is provided.

### Completing and Canceling Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is important to complete or cancel appointments to ensure the Telehealth Management Platform accurately reflects appointment statuses. This enables schedulers to easily filter by appointment status, for example to view scheduled appointments, completed appointments, or canceled appointments. As a result, provider productivity and resource utilization can be captured and accurately reported. Thanks to VistA integration, completing and canceling appointments through the Telehealth Management Platform automatically updates the appointment status in VistA.

Appointments may need to be canceled for various reasons. An individual appointment may be canceled if the Veteran cancels the appointment, the Veteran does not show up for the appointment, there is a technology error, there is a scheduling error, or the clinic cancels the appointment. A group appointment may be canceled if the there is a technology error, scheduling error, or the clinic cancels the appointment.

Additionally, an individual may be canceled from a group appointment without canceling the entire group appointment.

## Workplace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Telehealth Management Platforms supports pulling and displaying data from several sources through the Workplace function. This facilitates the use of data reports and analytics for reviewing VISN performance. Data sources include benchmarks, dashboard, and reports; these data sources are used to strengthen and expand telehealth programs. They are also used during Conditions of Participation reviews to evaluate performance and identify quality issues. During the Conditions of Participation review, the Telehealth Quality Team collaborates with the VISN Program Manager and Facility telehealth staff to ensure all data elements are addressed and analyzed, with improvements being made as required.

All levels of access/security roles can access the Workplace. However, views and options may be limited for different levels of access/security roles. Staff that will typically need to utilize the Workplace include VISN Leads, Facility Telehealth Coordinators, Telehealth Clinical Technicians, Schedulers, and non-telehealth staff (e.g. executive leadership and supervisors of telehealth staff).

Views, charts, and dashboards can be created through the Telehealth Management Platform. Views allow staff to adjust filter searches, for example limiting a search to show completed appointments or resources for a single facility. The information for each view is displayed through an associated chart. There are two types of views. “System Views” are generated by the Telehealth Management Platform while “My Views” are custom views created by the user. The settings option allows the views to be changed, for example to display more information.

Dashboards are used to display specific views and charts on a single page; this is helpful for staff that need to monitor specific data daily and would otherwise need to navigate to multiple places in the Telehealth Management Platform to access information that can be displayed on the dashboard.

A sharing option allows users to share views, charts, and dashboards with each other.

Reports can be generated from the Telehealth Management Platform. Reports are used as impartial mechanisms for reviewing data and VISN performance. Through the Telehealth Management Platform, a user can export information from a view into a report. For example, a user could export the number of canceled appointments due to technology failures into a report.

## Phone Book

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phone Book is a tool that allows Providers to connect to other Providers, as well as non-VA sites for Telemedicine and Teleconsultation. Through Phonebook, users can easily view site-specific contact information and capabilities. For sites with an assigned virtual medical room link, Phonebook also allows users to find and access the virtual medical room link. To manage the Phone Book, the TMP On Call Manager level of access/security role is required.

Phonebook is a useful tool in multiple situations. Examples of when it would be desirable to use Phonebook include:

- Access contact information for a site
- Connect to a site using an assigned virtual medical room
- View emergency procedures and emergency contact numbers for a specific site
- Determinate a site’s capabilities

## Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Settings menu, while displaying many features only enabled for System Administrations, does give the end user the ability to look at Video on Demand data.

## Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Help menu connects the end-user to Microsoft resources for general out of the box information on Microsoft products.

Note that the Telehealth Management Platform has many customizations unique to VHA Telehealth operations that may not be found in the Microsoft product page; for additional help refer to the trainings and resources listed in the following section.

## TMP Site Team

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TMP Site team is automatically assigned and managed by the TMP Site. This team can read records for the site.

## TMP FTC Approval Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TMP FTC Approval Group team is automatically assigned ownership of Scheduling Packages, Telehealth Service Agreements, Patient Site Resources, and Provider Site Resources within their own facility.

Staff who are added to the TMP FTC Approval Group will inherit the TMP User, TMP TSA Approver, and TMP TSA Manager levels of access/security roles.

The basic functions for this team are:

- Approve TSAs pertaining to their facility
- Create, Read, Update Scheduling Packages pertaining to their facility
- Create, Read, Update TSAs pertaining to their facility
- Add Provider, Patient Resources to Scheduling Packages and TSAs pertaining to their facility
- View Audit History pertaining to their facility

## TMP Chief of Staff Approval Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TMP Chief of Staff Approval Group routes TSAs in the approval process.

Users who are added to the TMP Chief of Staff Approval Group will inherit the TMP User and TSA Approver levels of access/security roles.

The basic functions for this team are:

- Approve TSAs pertaining to their facility
- Deny TSAs to reroute them back to the TMP TSA Manager at their facility for review

## TMP Service Chief Approval Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TMP Service Chief Approval Group routes TSAs in the approval process.

Staff who are added to the Chief of Staff Approval Group will inherit the TMP User, TSA Approver, and PPE Feedback levels of access/security roles.

The basic functions for this team are:

- Approve TSAs pertaining to their facility
- Deny TSAs to reroute them back to the TMP TSA Manager at their facility for review
- View Telehealth privileging records for a Provider at their facility
- Request and Submit a Professional Practice Evaluation (PPE) for a provider at their facility

## TMP Credentialing and Privileging Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TMP Credentialing and Privileging Group creates privileging records for Providers pertaining to their facility

Staff who are added to the Credentialing and Privileging Group will inherit the TMP User and Privileging levels of access/security roles.

The basic functions for this team are:

- View Professional Practice Evaluation (PPE) records for a Provider at their facility
- View Telehealth privileging records for a Provider at their facility
- Append Telehealth privileging records for a Provider at their facility
- Create Home/Primary and Proxy/Secondary privileging records for a Provider at their facility

## TSA Notification Team

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TSA Notification Team receives email notifications when a TSA is put into Production. If you are a part of the TSA Notification team, you will receive all notifications regarding TSAs.

Staff who are added to the TSA Notification Team will inherit the TMP User level of access/security role.

The basic functions for this team are:

- View TSAs pertaining to their facility
- Receive email notifications when a TSA at their facility is put into Production

## TMP Scheduler Team

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TMP Scheduler Team schedules Veterans’ appointments via TSAs.

Staff who are added to the TMP Scheduler Team will inherit the TMP User and Scheduler levels of access/security roles.

The basic functions for this team are:

- Open and view the appointment calendar
- Create Clinic-Based or Home, Mobile appointments
- Open and view an appointment
- Complete or Cancel an appointment within their site or facility

## TMP Staff Team

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TMP Staff team receives scheduling notifications.

Staff who are added to the TMP Staff Team will inherit the TMP User level of access/security role.

The basic functions for this team are:

- View appointment information, and
- Receive email notifications
