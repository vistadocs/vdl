---
title: SD*5.3*575 Display of Mental Health Treatment Coordinator (MHTC) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Display of Mental Health Treatment Coordinator (MHTC)
app_code: PCMM
app_name: Primary Care Management Module
section: CLI
app_status: active
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*575
group_key: "PCMM:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - mhtc
  - health
  - care
  - mental
  - pcmm
  - primary
  - patient
  - table
  - class
  - contents
page_count: 0
word_count: 1868
section_count: 2
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: January 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_575rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_575rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=95"
---

![](sd-5-3-575-display-of-mental-health-treatment-coordinator-mhtc-release-notes/001.png)

Primary Care Management Module (PCMM)

Display of Mental Health Treatment Coordinator (MHTC)

RELEASE NOTES

Patch SD\*5.3\*575

January 2012

Revision History

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
<td>Jan 2012</td>
<td><blockquote>
<p>Initial Release</p>
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
- [Acronyms and Definitions](#acronyms-and-definitions)
- [Appendix A: Standard Position File (#403.46)](#appendix-a-standard-position-file-40346)
The purpose of this document is to describe the changes to MHTC functionality in support of the Improve Veteran Mental Health (IVMH) initiative. It addresses a critical need to rapidly identify in a patient’s chart the Mental Health (MH) Treatment Coordinator so that information regarding the Veteran’s mental health care can be accessed to coordinate care more quickly and effectively. The changes introduced with this patch impact not only Primary Care Management Module (PCMM) coordinators and mental health professionals, but also all others providing services to Veterans who are seen in Mental Health who need to coordinate the Veteran’s care, such as nurses, physicians, ward clerks, etc.

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch SD\*5.3\*575 consists of enhancements to a number of features in PCMM so that the MHTC can be displayed for a patient in CPRS.

The modifications and enhancements to PCMM are included in section III.

# Description of Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following roles already exist in PCMM, but will now include MHTC designation roles as displayed in the below listing: (Refer to [Appendix A: Standard Position File](#appendix-a-standard-position-file-403.46) for a complete listing of the positions available in PCMM upon release of this patch.)

- Clinical Nurse Specialist (MHTC)
- Clinical Pharmacist (MHTC)
- Nurse (RN) (MHTC)
- Nurse Practitioner (MHTC)
- Physician Assistant (MHTC)
- Physician-Psychiatrist (MHTC)
- Psychologist (MHTC)
- Rehab/Psych Technician (MHTC)
- Social Worker (MHTC)

  The following roles will be added providing with and without MHTC designation:
- Addiction Therapist
- Addiction Therapist (MHTC)
- Chaplain
- Chaplain (MHTC)
- LPC
- LPC (MHTC)
- MFT
- MFT (MHTC)
- Peer Support Staff\*
- Occupational Therapist
- Occupational Therapist (MHTC)
- Recreation Therapist
- Recreation Therapist (MHTC)
- Voc Rehab Spec/Counselor
- Voc Rehab Spec/Counselor (MHTC)

  \*Note: Peer Support Staff does not have a MHTC designation.

Below lists the additional new functionality that will be available in PCMM:

- PCMM will create an API(s) to display the MHTC in CPRS which will appear on the patient inquiry and primary care display.
- PCMM will allow only one MHTC per patient. If a patient has already been assigned a MHTC the user will not see or be able to select a MHTC designated position.
- PCMM will not allow a Mental Health team to be setup as a primary care team.
- When setting up a Mental Health team, PCMM will not allow any of the checkboxes related to Primary Care Providers to be checked on the Settings tab.
- A user will be able to create a mental health team at a specific site if he/she is assigned the SC PCMM Setup key in the VistA account.
- PCMM will designate a team as a mental health team only if the purpose is set to “Mental Health Treatment” in the Primary Care Team Profile Settings.
- PCMM will allow a mental health team to have an unlimited number of positions. Any number of designated mental health/non-mental health roles can be assigned to these positions, i.e. pharmacists, etc.
- PCMM will prevent a user from attempting to assign a patient to more than one MHTC.
- PCMM will allow a patient to be assigned to multiple providers within their assigned mental health team.
- The MHTC designations will display in all areas where the role is viewed.
- The Staff Assignment history for any MHTC Position will be displayed in the Staff Assignment History table located on the Staff/FTEE tab of the Primary Care Team Position Setup window.
- PCMM will allow a patient to be on multiple mental health teams; there will be no limitations on the number of mental health teams for which a patient can be assigned.
- PCMM will allow a person assigned to a MHTC role to be assigned to any non-mental health team.
- PCMM will allow a patient to be assigned to a MHTC even if they are not assigned to a Primary Care Provider.
- e Specialist Pharmacistlainction Therapists (RN)Occupational Therapist

# Installation and Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific information pertaining to the installation of this patch can be found in the patch description and section referred to as ‘INSTALLATION INSTRUCTIONS’ in patch SD\*5.3\*575.

Pre-conditions for installation of this patch require the below patches to be installed prior to installation:

SD\*5.3\*504

SD\*5.3\*584

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Routine Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new routine, SCMCMHTC, will be created to pass the MHTC for a patient to CPRS for display.

# Acronyms and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
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
<td>CPRS GUI header bar</td>
<td><p>A set of buttons and icons at the top of the CPRS GUI window that a user can see from any tab. The header bar contains such buttons as the Patient Inquiry button, the Primary Care button, the Flag button, and the Visit Encounter button.<br />
<br />
An example of a CPRS GUI header bar is shown below:</p>
<p>![](sd-5-3-575-display-of-mental-health-treatment-coordinator-mhtc-release-notes/002.png)<br />
Example of a CPRS GUI header bar</p></td>
</tr>
<tr class="odd">
<td>MH Treatment Coordinator (MHTC)</td>
<td><p>The liaison between the patient and the mental health system at a VA site. There is only one MH treatment coordinator per patient and they are the key coordinator for behavioral health services care.</p>
<p>For more information about the MH treatment coordinator’s responsibilities, see VHA Handbook 1160.1, "Uniform Mental Health Services in VA Medical Centers and Clinics," pp. 3-4. <strong>Note:</strong> In the handbook, the MHTC is called the Principal Mental Health Provider.</p></td>
</tr>
<tr class="even">
<td>OR Patch</td>
<td>An OR patch is a CPRS patch.</td>
</tr>
<tr class="odd">
<td>Patient Inquiry display</td>
<td><p>CPRS GUI header display that contains the following information about a patient: mailing address, phone numbers, eligibility, health insurance, service connection/rated disabilities, primary care provider and MH treatment coordinator. A user can view the Patient Inquiry Display by clicking the Patient Inquiry button on the far left side of the header row directly below the menu bar.<br />
<br />
The Patient Inquiry button is highlighted in yellow in the example below:<br />
![](sd-5-3-575-display-of-mental-health-treatment-coordinator-mhtc-release-notes/003.png)</p>
<p>Example of a Patient Inquiry button</p></td>
</tr>
<tr class="even">
<td>PCMM Coordinator</td>
<td><p>The person who performs PCMM administrative tasks at a VA site and assigns a patient to a primary care team and a primary care provider.</p>
<p><strong>Note</strong>: The PCMM Coordinator could also assign a patient to a MH treatment coordinator upon agreement with Mental Health or Mental Health may have its own MH PCMM Coordinator for this process.</p></td>
</tr>
<tr class="odd">
<td>Primary Care button</td>
<td>Button on the CPRS GUI header bar that identifies the patient’s primary care and mental health providers. The Primary Care button is to the immediate right of the Visit Encounter button, and to the immediate left of the Flag button.<br />
<br />
The Primary Care button is outlined in red in the example below:<br />
![](sd-5-3-575-display-of-mental-health-treatment-coordinator-mhtc-release-notes/004.png)<br />
Example of a Primary Care button</td>
</tr>
<tr class="even">
<td>Primary Care display</td>
<td>CPRS GUI header display that contains information about a patient’s primary care and MH treatment coordinators. A user can view the Primary Care Display by clicking the Primary Care button on the header row directly below the menu bar.</td>
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
<td>A field in PCMM that denotes a function or task of a staff member involved with the implementation, maintenance and continued success of primary care and mental health care. Roles are displayed in several tables on the PCMM GUI. Sites are not allowed to edit the Role fields via FileMan without the direction of Decentralized Hospital Computer Program (DHCP) Customer Support.</td>
</tr>
<tr class="odd">
<td>Scope</td>
<td>The sum of products and services to be provided as a project.</td>
</tr>
<tr class="even">
<td>Team</td>
<td>A group of staff members organized in PCMM for a certain purpose (i.e., Primary Care, Mental Health, OEF/OIF…).</td>
</tr>
<tr class="odd">
<td>Team Profile</td>
<td>A screen within PCMM that shows the various characteristics of a particular team. For example, it will show the number of patients allowed for enrollment, name, and positions assigned.</td>
</tr>
</tbody>
</table>

# Appendix A: Standard Position File (#403.46)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The below 54 entries are available to choose from in the Position pick-list:

| ADDICTION THERAPIST                |
|------------------------------------|
| ADDICTION THERAPIST (MHTC)         |
| ADMIN COORDINATOR                  |
| CARE MANAGER                       |
| CASE MANAGER                       |
| CHAPLAIN                           |
| CHAPLAIN (MHTC)                    |
| CLINICAL NURSE SPECIALIST          |
| CLINICAL NURSE SPECIALIST (MHTC)   |
| CLINICAL PHARMACIST                |
| CLINICAL PHARMACIST (MHTC)         |
| DESIGNATED WOMEN’S HEALTH PROVIDER |
| DIETITIAN                          |
| HEALTH TECHNICIAN                  |
| INTERN (PHYSICIAN)                 |
| LPC                                |
| LPC (MHTC)                         |
| MAS CLERK                          |
| MEDICAL STUDENT                    |
| MFT                                |
| MFT (MHTC)                         |
| NURSE (LPN)                        |
| NURSE (RN)                         |
| NURSE (RN) (MHTC)                  |
| NURSE PRACTITIONER                 |
| NURSE PRACTITIONER (MHTC)          |
| OCCUPATIONAL THERAPIST             |
| OCCUPATIONAL THERAPIST (MHTC)      |
| OIF OEF CLINICAL CASE MANAGER      |
| OIF OEF PROGRAM MANAGER            |
| OIF OEF TRANSITION PATIENT ADV     |
| OTHER                              |
| PATIENT SERVICES ASSISTANT         |
| PEER SUPPORT STAFF                 |
| PHYSICIAN ASSISTANT                |
| PHYSICIAN ASSISTANT (MHTC)         |
| PHYSICIAN-ATTENDING                |
| PHYSICIAN-PRIMARY CARE             |
| PHYSICIAN-PSYCHIATRIST             |
| PHYSICIAN-PSYCHIATRIST (MHTC)      |
| PHYSICIAN-SUBSPECIALTY             |
| PSYCHOLOGIST                       |
| PSYCHOLOGIST (MHTC)                |
| RECREATION THERAPIST               |
| RECREATION THERAPIST (MHTC)        |
| REHAB/PSYCH TECHNICIAN             |
| REHAB/PSYCH TECHNICIAN (MHTC)      |
| RESIDENT (PHYSICIAN)               |
| SOCIAL WORKER                      |
| SOCIAL WORKER (MHTC)               |
| TEAM PHARMACIST                    |
| TRAINEE                            |
| VOC REHAB SPEC/COUNSELOR           |
| VOC REHAB SPEC/COUNSELOR (MHTC)    |

[Return to Description of Functionality section](#description-of-functionality)