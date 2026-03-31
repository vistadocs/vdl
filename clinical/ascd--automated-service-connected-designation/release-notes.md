---
title: ASCD Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: ASCD
app_name: Automated Service Connected Designation
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: 
  - SDSC CLINICAL
  - SDSC SUPER
menu_options: 0
description: - [# Introduction](#introduction) - [Install Requirements](#install-requirements) - [Overview of New Functionality and Enhancements](#overview-of-new-functionality-and-enhancements) - [Hospital Inquiry (HINQ) – DVB\4.0\58](#hospital-inquiry-hinq-dvb4058) - [Patient Care Encounter (PCE) – PX\1.0\184]
audience: 
keywords: 
  - encounters
  - date
  - encounter
  - service
  - report
  - connected
  - ascd
  - sdsc
  - table
  - review
page_count: 0
word_count: 8999
section_count: 8
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2007
revision_count: 1
revision_newest: 9/20/2007
revision_oldest: 9/20/2007
docx_url: "https://www.va.gov/vdl/documents/Clinical/Automated_Service_Connected_Designation/ascd_sd_53_495_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Automated_Service_Connected_Designation/ascd_sd_53_495_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=174"
---

![](ascd-release-notes/001.png)

Automated Service Connected Designation (ASCD)

Release Notes

SD\*5.3\*495

PX\*1.0\*184

DVB\*4.0\*58

September 2007

Health Program Support Office (HPSO)

Revision History

|           |              |                 |                              |
|-----------|--------------|-----------------|------------------------------|
| Date  | Revision | Description | Author                   |
| 9/20/2007 | 1.0          | Release Version | PMS Legacy Enhancements Team |
|           |              |                 |                              |
|           |              |                 |                              |
|           |              |                 |                              |
|           |              |                 |                              |
|           |              |                 |                              |

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
  - [Install Requirements](#install-requirements)
  - [Overview of New Functionality and Enhancements](#overview-of-new-functionality-and-enhancements)
    - [Hospital Inquiry (HINQ) – DVB\4.0\58](#hospital-inquiry-hinq-dvb4058)
    - [Patient Care Encounter (PCE) – PX\1.0\184](#patient-care-encounter-pce-px10184)
    - [Scheduling (SD) – SD\5.3\495](#scheduling-sd-sd53495)
    - [Changes to Integrated Billing (IB)](#changes-to-integrated-billing-ib)
- [Package Enhancements and Modifications](#package-enhancements-and-modifications)
  - [Hospital Inquiry (HINQ) – VBA / ICD9 Code Mapping](#hospital-inquiry-hinq-vba-icd9-code-mapping)
    - [DISABILITY CONDITION (#31) file modified](#disability-condition-31-file-modified)
  - [Patient Care Encounter (PCE) and Scheduling](#patient-care-encounter-pce-and-scheduling)
    - [Automation of Diagnosis Code (SC) – (NSC) Designation](#automation-of-diagnosis-code-sc-nsc-designation)
    - [Criteria for Flagging Encounters for Review](#criteria-for-flagging-encounters-for-review)
  - [Automated Service Connected Designation Menu](#automated-service-connected-designation-menu)
    - [User Types](#user-types)
    - [ASCD Compile Parameter \[SDSC SITE PARAMETER\] Option](#ascd-compile-parameter-sdsc-site-parameter-option)
    - [Compile ASCD Encounters by Date Range \[SDSC COMPILE\] Option](#compile-ascd-encounters-by-date-range-sdsc-compile-option)
    - [Edit ASCD Encounters by Date Range \[SDSC EDIT BY DATE\] Option](#edit-ascd-encounters-by-date-range-sdsc-edit-by-date-option)
    - [Edit ASCD Encounters by ListMan \[SDSC EDIT LISTMAN\] Option](#edit-ascd-encounters-by-listman-sdsc-edit-listman-option)
    - [### ### ### ### ### Edit Single ASCD Encounter \[SDSC SINGLE EDIT\] Option](#edit-single-ascd-encounter-sdsc-single-edit-option)
    - [### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ASCD Reports \[SDSC REPORTS\] Option](#ascd-reports-sdsc-reports-option)
    - [Compile ASCD Encounters on a Nightly Basis \[SDSC NIGHTLY COMPILE\]](#compile-ascd-encounters-on-a-nightly-basis-sdsc-nightly-compile)
    - [Purge ASCD NSC Encounters \[SDSC PURGE NSC ENC\]](#purge-ascd-nsc-encounters-sdsc-purge-nsc-enc)
  - [Files and Fields](#files-and-fields)
    - [New Files](#new-files)
    - [Modified Files](#modified-files)
  - [Other Functionality](#other-functionality)
    - [Mail Group](#mail-group)
    - [Security Keys](#security-keys)
    - [Parameter Definition](#parameter-definition)
    - [Background Option Scheduling](#background-option-scheduling)
    - [SCOUT – Class III File Conversion](#scout-class-iii-file-conversion)
    - [SCOUT – Deactivation of Class III software](#scout-deactivation-of-class-iii-software)
The Automated Service Connected Designation (ASCD) project will automate the SC decision for outpatient encounters using the mapped ICD/Rated Disability Codes at the time the clinician actually picks the ICD code for the encounter within the Patient Care Encounter (PCE) and Scheduling packages ONLY.
PleaseNOTE: The automation of the SC decision is NOT applicable to the ancillary packages at this time (i.e. CPRS, QUADRAMED, Radiology, Surgery, etc.).
In the current clinical work environment, providers are requested to designate at the point of care if a specific patient care encounter is service connected (SC) based on available disability rating information. This software will computerize the clinician’s process at each encounter, i.e. mark the encounter service-connected (SC) or non service-connected (NSC) as appropriate via the PCE & Scheduling packages. Thus, when a provider or clinician chooses the diagnosis code within PCE & Scheduling for the encounter the system will automatically determine if the diagnosis is related to the veteran's established service connected conditions, and will likewise automatically make the proper SC/NSC determination for that encounter. Additionally, the Class III Service Connection Objective Update Tool (SCOUT) has been converted and implemented as Class I Automated Service Connected Designation (ASCD). This software recognizes potentially billable encounters for SC veterans that cannot be automatically matched to Rated Disability codes as well as potentially non-billable encounters which were designated NSC but should be SC. These encounters are displayed in reports for coders and/or utilization review staff to review the patient visit information and change the incorrect SC/NSC designation so they can be billed appropriately.
The Hospital Inquiry (HINQ), Patient Care Encounter (PCE) and Scheduling packages have been enhanced as part of the ASCD software.
Additional information and documentation on ASCD can be obtained from –
VHA Software Document Library https://www.va.gov/vdl/
DVB\*4.0\*58, PX\*1.0\*184 and SD\*5.3\*495 patch descriptions.
Project Notebook <http://tspr.vista.med.va.gov/warboard/portfolio.asp>.

## Install Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Package Integration

The ASCD application processing assumes the following VistA packages are installed and fully patched:

DVB V.4.0

IB V.2.0

ICD V.18.0

ICPT V.6.0

Kernel V.8.0

Kernel Toolkit V.7.3

PCE V.1.0

PRCA V.4.5

SD V.5.3

VA FileMan V.22.0

VA MailMan V.8.0

Required Patches:

The following patches are required prior to installation of patches DVB\*4.0\*58, SD\*5.3\*495 and PX\*1.0\*184 for this project:

DVB\*4.0\*50

PX\*1.0\*158

SD\*5.3\*466

PRCA\*4.5\*250

IB\*2.0\*369

## Overview of New Functionality and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Automated Service Connected Designation (ASCD) project will add the following new functionality and enhancements to the HINQ, PCE and SCHEDULING packages:

### Hospital Inquiry (HINQ) – DVB\*4.0\*58

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch introduces modifications to the DISABILITY CONDITION file (#31).

- The Veterans Health Administration (VHA) has mapped the Veteran Benefits Administration (VBA) 4 digit RATED DISABILITIES (VA) code terminology to the ICD-9-CM codes used for billing and reporting purposes within VistA. This mapping will facilitate the automation of the Service Connected (SC)/Non-Service Connected (NSC) decision for outpatient encounters.

### Patient Care Encounter (PCE) – PX\*1.0\*184

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch introduces modifications/enhancements for outpatient encounter entry/edit.

- Modifications were made to the outpatient encounter diagnosis entry process to automate the response to the question "Was treatment for SC Condition?" for each diagnosis code. The question will not allow user entry and will be displayed briefly to the user with the ASCD answer.
- Modification was made to PCE Encounter Data Entry - Supervisor \[PXCE ENCOUNTER ENTRY SUPER\] option to allow users to change the ASCD value which will be displayed as the default. This will allow users to access encounters that are not set for review and are not accessible via the ASCD review options.
- Modifications were made to check-out screen under the section "Patient's Service Connection and Rated Disabilities:" to display the RATED DISABILITY CODE number before the Rated Disabilities (VA) name.
- Modifications were made to correct a problem identified during testing where the classification questions were being asked when entering a standalone encounter for a non-count clinic or an inpatient.

### Scheduling (SD) – SD\*5.3\*495

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch introduces modifications/enhancements for outpatient encounter entry/edit.

- Modifications were made to the outpatient encounter diagnosis entry process to automate the response to the question "Was treatment for SC Condition?" for each diagnosis code. The question will not allow user entry and will be displayed briefly to the user with the ASCD answer.
- Modifications were made to the outpatient encounter checkout process to determine if the encounter needs additional review for the service connected designation and if applicable the encounter will be placed in review file upon checkout.
- The SCOUT application was converted and modified for processing and reporting of outpatient encounters that have been set for review.

### Changes to Integrated Billing (IB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- If the SC/NSC determination is changed and if the encounter is already defined in Claims Tracking then the encounters Claims Tracking Entry is updated.

> ► The Reason Not Billable (RNB) of SC TREATMENT is either added or removed.

- If the encounter changed from NSC to SC and there is no RNB, then SC TREATMENT is added as the RNB.
- If the encounter changed from SC to NSC and the RNB is SC TREATMENT then its deleted.

> ► The Last Reviewed By is set to the ASCD user.

> ► The Billable Finding is set to either 'NSC TO SC' or 'SC TO NSC'.

- If the encounter is not already in Claims Tracking then it will be added with the correct/update SC/NSC information from PCE when it is added.

PLEASE NOTE: Changing a patient’s status from Non-Service Connected (NSC) to Service Connected (SC) needs to be monitored to ensure any newly SC designated care has not been billed. If SC care has been billed, the bill needs to be cancelled.

# Package Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new functionality for ASCD software is discussed in detail in the following sections.

## Hospital Inquiry (HINQ) – VBA / ICD9 Code Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### DISABILITY CONDITION (#31) file modified

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DISABILITY CONDITION file (#31) has been modified so that specific 4 digit Rated Disabilities (VA) codes that have been selected by the Veterans Health Administration (VHA) will contain a special mapping to specific ICD-9-CM codes. This mapping will be used to fully or partially match an encounter diagnosis code to the veteran's established rated disabilities service connected conditions in making a SC or NSC determination on that encounter.

A new multiple field named RELATED ICD9 CODES has been added. There are two sub-file fields, RELATED ICD9 CODES Field (#.01) and ICD9 MATCH Field (#.02). These fields contain the ICD9 code pointer and a matching value respectively. A ‘1’ indicates a true match and a ‘0’ indicates a partial match.

## Patient Care Encounter (PCE) and Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Automation of Diagnosis Code (SC) – (NSC) Designation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Care Encounter (PCE) and Scheduling packages outpatient encounter data entry process for entering diagnosis codes has been enhanced to automate the service connected (SC) or non-service connected (NSC) decision-making.

The response to the service connected classification prompt "Was treatment for SC Condition?” has been automated for each diagnosis code entry. The question will not allow user entry and will be displayed briefly to the user with the ASCD answer. However, users can change the ASCD default value for encounters that are not set for review and are not accessible via the ASCD review options via the PCE Encounter Data Entry - Supervisor \[PXCE ENCOUNTER ENTRY SUPER\] option,. The next service connected classification prompt will be presented for user input if applicable.

Scheduling uses the patient’s mapped RATED DISABILITIES (VA) and ICD9 codes in the DISABILITY CONDITION (#31) file to determine the SC/NSC response for outpatient encounters.

The Service Connected Classification status automation uses the following conditions:

- Outpatient Encounters and;
- Veteran is Service Connected and;
- The encounter eligibility is Service Connected and;
- The clinic is not a non-count clinic.

Encounter Check-out Diagnosis code enter/edit screen Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><mark>Enter Diagnosis</mark> : 200.07</p>
<p>Reticulosarcoma involving spleen (ICD-9-CM 200.07)</p>
<p>Ok? YES// YES Reticulosarcoma involving spleen (ICD-9-CM 200.07)</p>
<p>&gt;&gt;&gt; Code : 200.07</p>
<p>Provider Narrative: RETICULOSARCOMA INVOLVING SPLEEN</p>
<p>RETICULOSARCOMA INVOLVING SPLEEN</p>
<p>Is this Diagnosis Primary for the Encounter: YES//</p>
<p>Is this Diagnosis Ordering, Resulting, or Both: BOTH O&amp;R</p>
<p>Modifier:</p>
<p>Encounter Provider: PCEPROVIDER,ONE// GTS</p>
<p>Is this provider Primary or Secondary? P// PRIMARY</p>
<p>Comments:</p>
<p><mark>Patient's Service Connection and Rated Disabilities:</mark></p>
<p>SC Percent: 75%</p>
<p><mark>Rated Disabilities:</mark> <mark>7014</mark> RAPID PULSE OF THE HEART (20%-SC) ◄ RATED DISABILITY CODE - 7014</p>
<p><mark>7706</mark> REMOVAL OF SPLEEN (100%-SC) ◄ RATED DISABILITY CODE - 7706</p>
<p>--- <mark>Classification</mark> --- [Required]</p>
<p><mark>Was treatment for SC Condition? NO</mark> ◄ Prompt and response displayed, no user interaction</p>
<p>Was treatment related to Combat? NO</p>
<p>Was treatment related to Agent Orange Exposure? NO</p>
<p>Was treatment related to Ionizing Radiation Exposure? NO</p>
<p>Was treatment related to Environmental Contaminant Exposure? NO</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The RATED DISABILITY CODE numbers are now displayed before the Rated Disabilities (VA) name as shown above.

The response to the question "Was treatment for SC Condition?" will be automatically set to YES for any of the following conditions:

- The patient has rated disabilities and the encounter diagnosis code is a true match with at least one diagnosis code associated with the rated disability code(s).
- The patient has rated disabilities and the encounter diagnosis code is a partial match with at least one (1) diagnosis code associated with a rated disability code.
- The patient is service connected with a percentage, but does NOT have any rated disabilities.
- The patient has rated disabilities but they are not mapped to any diagnosis codes.

The response to the question "Was treatment for SC Condition?" will be automatically set to NO for any of the following conditions:

- The patient has rated disabilities but the encounter diagnosis code does NOT match any of the diagnosis codes associated with the rated disabilities.
- If patient has multiple rated disabilities (mapped and not mapped) and the encounter diagnosis code does not match a diagnosis for the mapped rated disability.

### Criteria for Flagging Encounters for Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The service connected status is automatically determined within Scheduling and PCE upon entry of the diagnosis if the encounter is SC eligible. Certain encounters are sent to the ASCD review file (#409.48) after all diagnosis codes have been entered for the encounter and it has been checked out. The following criteria is used to determine if the encounter will be sent for additional review.

The encounter WILL need additional review based on the following conditions:

The patient has rated disabilities and one of the encounter diagnosis codes is a partial match with at least one (1) diagnosis code associated with a rated disability code.

The patient is service connected with a percentage, but does NOT have any rated disabilities.

The patient has rated disabilities but the entered encounter diagnosis codes do NOT match any diagnosis code associated with the rated disabilities.

The patient has rated disabilities on file but they are not mapped to any diagnosis code at all.

The patient has rated disabilities and the encounter *secondary* diagnosis code is a true match with a rated disability code.

The encounter WILL NOT need additional review based on the following conditions:

The patient is non-billable for 1<sup>st</sup> and 3<sup>rd</sup> party.

- The patient has rated disabilities and the encounter *primary* diagnosis code is a true match with a rated disability code(s).

  A user with the PCE ENCOUNTER DATA ENTRY-SUPERVISOR option will have the ability to change the service connected value during data entry. ASCD will compute the SC value and it will be presented as a default. This option can be used to edit those encounters that are not sent for review.

#### #### #### #### Ancillary Package Encounters

Any outpatient encounter record sent to the Patient Care Encounter (PCE) system from an ancillary package for workload reporting will be reviewed using the same criteria detailed above.

However, it should be noted:

- Encounters will be flagged for review when the ASCD value is a true match but the originating value does not match the ASCD value.
- The original SC value will NOT change but the encounter will be flagged for additional review if the original SC value is different from the ASCD evaluation value.
- Ancillary packages will NOT be updated if value is changed after ASCD review. The following message will be displayed to users when they access an encounter that originated from an ancillary package:

> ► WARNING: This encounter came from another package. If it is changed

> it will not agree with what is in the originating package.

- PLEASE NOTE: CPRS will be updated if SC/NSC value is changed after ASCD review.

#### Records Removed from the SDSC SERVICE CONNECTED CHANGES File (#409.48)

Any outpatient encounter record that has been reviewed and was updated by adding a primary diagnosis code that has a true match with one of the patient’s rated disabilities will be deleted from the SDSC SERVICE CONNECTED CHANGES file (#409.48).

## Automated Service Connected Designation Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Automated Service Connected Designation Menu \[SDSC MENU\] option will be added to the Scheduling Manager's Menu \[SDMGR\] option. The menu options for ASCD should be distributed accordingly to personnel responsible for the management and administration of outpatient encounter check-out processing and review.

The ASCD options are as follows:

ASCD Compile Parameter \[SDSC SITE PARAMETER\]

ASCD Reports ... \[SDSC REPORTS\]

Compile ASCD Encounters by Date Range \[SDSC COMPILE\]

Edit ASCD Encounters by Date Range \[SDSC EDIT BY DATE\]

Edit ASCD Encounters by ListMan \[SDSC EDIT LISTMAN\]

Edit Single ASCD Encounter \[SDSC SINGLE EDIT\]

Purge ASCD NSC Encounters \[SDSC PURGE NSC ENC\]

### User Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three (3) types of Users are recognized and authorized to use the Automated Service Connected Designation Menu \[SDSC MENU\] option:

1\) <u>General Users</u>

These users are not assigned a security key and can only see and review the encounters with a status of ‘NEW’. They can print the reports, which do not require a security key.

2\) <u>Clinical Reviewers</u>

These users are assigned the SDSC CLINICAL security key. They can only see and review encounters with a status of ‘REVIEW’. They can print the reports, which do not require a security key.

3\) <u>Supervisors</u>

These users are assigned the SDSC SUPER security key. They can see and review ALL encounters with a status of ‘NEW’, ‘REVIEW’, and ‘COMPLETED’. This security key should be restricted to only a few users who as supervisors have the ability to undo a change. Supervisors have access to all ASCD options.

### ASCD Compile Parameter \[SDSC SITE PARAMETER\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASCD Compile Parameter \[SDSC SITE PARAMETER\] menu option is used to set the number of days that the manual ‘Compile ASCD Encounters by Date Range’ \[SDSC COMPILE\] option will use as a start date when searching for outpatient encounters that may need additional review by the ASCD software. This value is also used in the ‘Compile Results Report’ \[SDSC CHECK COMPILE\] and ‘Manager Summary Report’ \[SDSC MANAGER SUMMARY REPORT\] to validate the beginning date.

The site parameter is set to 30 days by the SD\*5.3\*495 patch installation. This option is LOCKED by the SDSC SUPER security key.

### Compile ASCD Encounters by Date Range \[SDSC COMPILE\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option gathers encounters that have been updated or encounters with late identified insurance by performing a search on the OUTPATIENT ENCOUNTER file (#409.68). The start date of the compile is based on the number of days defined by the Site Parameter Definition \[SDSC SITE PARAMETER\]. The option uses the rules listed under ‘Criteria for Flagging Encounters for Review’ to determine if the encounter should be added to the review file. This option can be run real-time or scheduled for a later time for a given date range. It is suggested that this option be run at least once a month to update any records not completed at the time of the nightly compile.

This option also purges and reports those records from the SDSC SERVICE CONNECTED CHANGES file (#409.48) when corresponding records do not exist in the OUTPATIENT ENCOUNTER file (#409.68).

The compile will NOT select any outpatient encounters where the patient does not have any 3rd party insurance.

- However, if auditing has been turned on for certain fields in the Patient File (#2); field .3192 COVERED BY HEALTH INSURANCE? and field .01 INSURANCE TYPE of the INSURANCE TYPE subfile (#.3121), the compile will check to see if above-mentioned fields have recently been changed to YES or a new insurance company has been added.

All outpatient encounters within a 24 month range will be checked for late identified insurance to see if there are any SC encounters which potentially may not be SC and may now be billable due to the addition of active insurance.

After completion of the compile, a MailMan message containing the results will be sent to members of the mail group, SDSC NIGHTLY TALLY.

MailMan Message Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: ASCD Compile Numbers [#2012538] 02/20/07@15:48 20 lines</p>
<p>From: ASCD COMPILE In 'IN' basket. Page 1</p>
<p>-------------------------------------------------------------------------------</p>
<p>Date Range (Compile) - From: Feb 19, 2007 Thru: Feb 19, 2007</p>
<p>Date Range (Late Ins.) - None</p>
<p>Number of encounters Service Connected (Compile) : 0</p>
<p>Number of encounters Service Connected (Late Ins.) : 0</p>
<p>(Number SvcConn with a True Map) : 0</p>
<p>(Number SvcConn with a Partial Map) : 0</p>
<p>(Number SvcConn that don't Map to VBA) : 0</p>
<p>Number of encounters Not Service Connected : 0</p>
<p>Number of encounters that are Non-billable : 26</p>
<p>Number of encounters with Non-count Clinics : 2</p>
<p>Number of encounters with no diagnoses : 0</p>
<p>Number of encounters with other errors : 0</p>
<p>Number of encounters already evaluated : 30</p>
<p>---------------------------------------------------------------------------</p>
<p>Total Encounters Checked: 58</p>
<p>ASCD Late Insurance Check:</p>
<p>Auditing is not turned on for field COVERED BY HEALTH INSURANCE.</p>
<p>Auditing is not turned on for field INSURANCE TYPE</p>
<p>Enter message action (in IN basket): Ignore//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Edit ASCD Encounters by Date Range \[SDSC EDIT BY DATE\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables users to review ASCD encounters one record at a time within a selected date range. The user will select encounters for a date range by division(s) and can choose to display only SC or NSC or all encounters they need to review.

Security Keys:

SDSC SUPER users can review and edit encounters with a status of NEW, REVIEW and COMPLETED.

SDSC CLINICAL users can review and edit encounters with a status of REVIEW.

General users can review and edit encounters with a status of NEW.

For each encounter found the user may choose one of the following actions -

Y (YES) to modify this encounter's Service Connected value. This enables the user

to edit the diagnosis code(s) and change the value for the SC questions,

> where applicable. NOTE: *In order to set an encounter with multiple diagnoses to NSC and mark it as billable, ALL diagnoses would need to be changed to NO.*

N (NO) to retain this encounter's Service Connected value. NO allows the user to

accept the original SC determination entered for this encounter.

S (SKIP) to skip this encounter and review it later. SKIP allows the user to move on

to the next encounter to be edited. The skipped encounter will still be

available for review at a later date.

R (REVIEW) to flag this encounter for clinical review. REVIEW enables the user to

send the encounter back to a clinical reviewer if the decision cannot easily

be made as to whether this encounter is truly service connected or not.

Edit Encounter by Date Range Screen Display Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Automated Service Connected Designation Menu Option: EDIT</p>
<p>1 Edit ASCD Encounters by Date Range</p>
<p>2 Edit ASCD Encounters by ListMan</p>
<p>3 Edit Single ASCD Encounter</p>
<p>CHOOSE 1-3: 1 Edit ASCD Encounters by Date Range</p>
<p>Service Connected Encounters Review Selection</p>
<p>Select one of the following:</p>
<p>S Service Connected</p>
<p>N Non-Service Connected</p>
<p>A All</p>
<p>Which type do you want to review?: S// Service Connected</p>
<p>Please enter START date: 05252007 (MAY 25, 2007)</p>
<p>Please enter END date: Jun 07, 2007// (JUN 07, 2007)</p>
<p>1 DAYTON</p>
<p>2 SPRINGFIELD</p>
<p>3 MIDDLETOWN</p>
<p>4 LIMA</p>
<p>5 RICHMOND</p>
<p>6 ALL</p>
<p>Select DIVISION: (1-6): 6//</p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p>------------------------------------------------------------------------------</p>
<p>Encounter 2688352 is marked as service connected.</p>
<p>Date of Encounter: 12/04/2006@10:00</p>
<p>Location: TELE-MH GREELEY/VETERAN</p>
<p>Primary Provider: PROVIDER,PRIMARY</p>
<p>Patient: PMS,ONE (0001) *SENSITIVE*</p>
<p>Patient is copay eligible.</p>
<p>Patient is not insured.</p>
<p>ASCD Evaluation: SC (no ICD9 match)</p>
<p>POVs/ICDs:</p>
<p>*SC* 380.15 CHR MYCOT OTITIS EXTERNA</p>
<p>780.6 FEVER</p>
<p>Rated Disabilities:</p>
<p>5209 ELBOW CONDITION (55%-SC)</p>
<p>6210 AUDITORY CANAL DISEASE (50%-SC)</p>
<p><mark>DO YOU WANT TO CHANGE THE SERVICE CONNECTION FOR THIS ENCOUNTER?</mark> <mark>?</mark></p>
<p>Enter:</p>
<p>'YES' to modify this encounter's Service Connected statuses.</p>
<p>'NO' to retain this encounter's Service Connected statuses.</p>
<p>'SKIP' to skip this encounter and review it later.</p>
<p>'REVIEW' to flag this encounter for clinical review.</p>
<p>Select one of the following:</p>
<p>Y YES</p>
<p>N NO</p>
<p>S SKIP</p>
<p>R REVIEW</p>
<p>DO YOU WANT TO CHANGE THE SERVICE CONNECTION FOR THIS ENCOUNTER? <mark>Y</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

(Continued…)

<span class="mark">PAT/APPT/CLINIC: PMS,ONE 12/04/2006@10:00 TELE-MH REELEY/VETERAN</span>

ICD CODE: ...There are 2 ICD CODES associated with this encounter.

<span class="mark">- - E N C O U N T E R D I A G N O S I S (ICD9 CODES) - -</span>

<span class="mark">No. ICD DESCRIPTION PROBLEM LIST</span>

1 380.15 CHR MYCOT OTITIS EXTERNA <span class="mark">PRIMARY</span> ORDERING

SC:Y CV:NAO:NIR:NEC:N

2 780.6 FEVER RESULTING

SC:N CV:NAO:NIR:NEC:N

Enter Diagnosis : 1

ONE primary diagnosis must be established for each encounter!

Is this the PRIMARY DIAGNOSIS for this ENCOUNTER? YES//

Select one of the following:

O ORDERING

R RESULTING

OR BOTH O&R

Is this Diagnosis Ordering or Resulting:: // OR BOTH O&R

Patient's Service Connection and Rated Disabilities:

SC Percent: 60%

Rated Disabilities: 5209 ELBOW CONDITION (55%-SC)

6210 AUDITORY CANAL DISEASE (50%-SC)

--- <span class="mark">Classification</span> --- <span class="mark">\[Required\]</span>

Was treatment for SC Condition? YES// <span class="mark">NO</span> ◄ <span class="mark">Changed here</span>

Was treatment related to Combat? NO//

Was treatment related to Agent Orange Exposure? NO

Was treatment related to Ionizing Radiation Exposure? NO

Was treatment related to Environmental Contaminant Exposure? NO

Enter <span class="mark">NEXT</span> Diagnosis :

Would you like to add any Diagnosis to the Problem List? NO//

\- - - - S o r r y A b o u t T h e W a i t - - - -

This information is being stored or monitored by Scheduling

Integrated Billing, Order Entry, Registration, Prosthetics

PCE/Visit Tracking and Automated Med Information Exchange.

Performing Ambulatory Care Validation Checks.

No validation errors found!

(Continued…)

<span class="mark">PAT/APPT/CLINIC: PMS,ONE 12/04/2006@10:00 TELE-MH REELEY/VETERAN</span>

ICD CODE: ...There are 2 ICD CODES associated with this encounter.

<span class="mark">- - E N C O U N T E R D I A G N O S I S (ICD9 CODES) - -</span>

<span class="mark">No. ICD DESCRIPTION PROBLEM LIST</span>

1 380.15 CHR MYCOT OTITIS EXTERNA <span class="mark">PRIMARY</span> ORDERING

SC:<span class="mark">N</span> CV:NAO:NIR:NEC:N

2 780.6 FEVER RESULTING

SC:N CV:NAO:NIR:NEC:N

Enter NEXT Diagnosis :

Would you like to add any Diagnoses to the Problem List? NO//

\- - - - S o r r y A b o u t T h e W a i t - - - -

This information is being stored or monitored by Scheduling

Integrated Billing, Order Entry, Registration, Prosthetics

PCE/Visit Tracking and Automated Med Information Exchange.

Performing Ambulatory Care Validation Checks.

No validation errors found!

### Edit ASCD Encounters by ListMan \[SDSC EDIT LISTMAN\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables users to review multiple ASCD encounters for the selected date range and division(s), as well as the ability to choose which type they would like to display. This option displays the encounters using VistA List Manager format. The various types of encounter statuses displayed will be based on the security key assigned to the user (See section on ‘Edit ASCD Encounters by Date Range’ \[SDSC EDIT BY DATE\] for security keys).

Edit Encounter by Date Range Screen Display Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Automated Service Connected Designation Menu Option: EDIT</p>
<p>1 Edit ASCD Encounters by Date Range</p>
<p>2 Edit ASCD Encounters by ListMan</p>
<p>3 Edit Single ASCD Encounter</p>
<p>CHOOSE 1-3: 2 Review Encounters screen display List Manger Example:</p>
<p>Service Connected Encounters Review Selection</p>
<p>Select one of the following:</p>
<p>S Service Connected</p>
<p>N Non-Service Connected</p>
<p>A All</p>
<p>Which type do you want to review?: S// Service Connected</p>
<p>Please enter START date: 05252007 (MAY 25, 2007)</p>
<p>Please enter END date: Jun 07, 2007// (JUN 07, 2007)</p>
<p>1 DAYTON</p>
<p>2 SPRINGFIELD</p>
<p>3 MIDDLETOWN</p>
<p>4 LIMA</p>
<p>5 RICHMOND</p>
<p>6 ALL</p>
<p>Select DIVISION: (1-6): 6//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

(Continued: ListMan Display of Encounters Example: )

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><mark>ASCD Jan 26, 2007@11:14:07 Page: 1 of 1</mark></p>
<p>The Service Connected status needs to be reviewed for the following encounters.</p>
<p>Selected Date Range: Oct 20, 2006 - Apr 04, 2007</p>
<p><mark>Encounter Enc Date/Time Patient Status</mark></p>
<p>1 2688352 08/02/2007@09:00 PMS,ONE (0001) NEW</p>
<p>2 2688333 08/06/2007@09:00 PMS,TWO (0002) NEW</p>
<p>3 2688340 08/11/2007@08:00 PMS,THREE (0003) REVIEW</p>
<p>4 2688342 08/01/2007@10:00 PMS,FOUR (0004) REVIEW</p>
<p>5 2688346 08/10/2007@11:30 PMS,FIVE (0005) COMPLETED</p>
<p>6 2688344 08/03/2007@16:00 PMS,SIX (0006) COMPLETED</p>
<p>7 2688358 08/01/2007@14:00 PMS,SEVEN (0007) COMPLETED</p>
<p><mark>+ Enter ?? for more actions</mark></p>
<p>Review Encounter</p>
<p>Select Item(s): Next Screen// REV Review Encounter</p>
<p>Select Number to Review: (1-7): <mark>1 &lt;return&gt;</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

(Continued: Review Encounter Detail Display Example: )

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><mark>Encounter Detail Apr 04, 2007@16:58:12 Page: 1 of 0</mark></p>
<p>Encounter 2688352 is marked as service connected.</p>
<p>Date of Encounter: 12/04/2006@10:00</p>
<p>Location: TELE-MH GREELEY/VETERAN</p>
<p>Primary Provider: PROVIDER,PRIMARY</p>
<p>Patient: PMS,ONE (0001) *SENSITIVE*</p>
<p>Patient is copay eligible.</p>
<p>Patient is not insured.</p>
<p>ASCD Evaluation: SC (no ICD9 match)</p>
<p>POVs/ICDs:</p>
<p>*SC* 380.15 CHR MYCOT OTITIS EXTERNA</p>
<p>780.6 FEVER</p>
<p>Rated Disabilities:</p>
<p>5209 ELBOW CONDITION (55%-SC)</p>
<p>6210 AUDITORY CANAL DISEASE (50%-SC)</p>
<p><mark>Enter ?? for more actions</mark></p>
<p><mark>YES Modify SvcConnected Status</mark></p>
<p><mark>NO Retain SvcConnected Status</mark></p>
<p><mark>REV Flag for Clinical Review</mark></p>
<p>Select Item(s): Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** For each encounter reviewed, users can choose Yes, No, or Review actions as described under the section ‘Edit ASCD Encounters by Date Range’ \[SDSC EDIT BY DATE\] option.

### ### ### ### ### ### Edit Single ASCD Encounter \[SDSC SINGLE EDIT\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables users to edit ASCD encounters one record at a time. User can enter a specific encounter \# , status, or patient name. If patient name is entered, then a list of all encounters will be displayed for that patient.

The following user prompt is presented:

Select OUTPATIENT ENCOUNTER:

For each encounter reviewed, users can choose Yes, No, or Review actions as described under the section ‘Edit ASCD Encounters by Date Range’ \[SDSC EDIT BY DATE\].

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ASCD Reports \[SDSC REPORTS\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains all the reports related to the Automated Service Connected Designation module. All reports are accessible to users except the Manager Summary Report which is locked by the SDSC SUPER security key.

ASCD Reports ... \[SDSC REPORTS\]

Clinic Service Total Summary Report \[SDSC SERVICE TOTAL REPORT\]

Compile Results Report \[SDSC CHECK COMPILE\]

Estimated Recovered Costs Report \[SDSC RECOVERED REPORT\]

First Party Billable Service Connected Report \[SDSC FIRST PARTY REPORT\]

Manager Summary Report \[SDSC MANAGER SUMMARY REPORT\]

Provider Service Connected Encounters Report \[SDSC PROVIDER REPORT\]

Provider Total Summary Report \[SDSC PROVIDER TOTAL REPORT\]

Service Connected Encounters Report \[SDSC ENC REPORT\]

Third Party Billable Service Connected Report \[SDSC THIRD PARTY REPORT\]

Unbilled/Billable Amount Report \[SDSC UNBILL AMT REPORT\]

User Service Connected Encounters Report \[SDSC USER REPORT\]

User Total Summary Report \[SDSC USER TOTAL REPORT\]

#### Clinic Service Total Summary Report \[SDSC SERVICE TOTAL REPORT\]

This report prints the service connected changes by clinical service, M:MEDICINE; S:SURGERY; P:PSYCHIATRY; R:REHAB MEDICINE; N:NEUROLOGY; 0:NONE, under the following categories per that clinic service.

- Number of outpatient encounters where ASCD automatically matched the encounter diagnosis with at least one (1) diagnosis associated with the patient’s rated disability codes (partial match) - VBA OK.
- Number of outpatient encounters set to Clinical Review - REVIEW
- Number of outpatient encounters marked as ‘Service Connected=YES’ but were changed to ‘Service Connected =NO’ - SC to NSC.
- Number of outpatient encounters marked as ‘Service Connected=NO’ but were changed to ‘Service Connected=YES’ – NSC to SC.
- Number of outpatient encounters marked as ‘Service Connected=YES’ or ‘Service Connected = No’ that were not changed.- SC KEPT.
- Number of outpatient encounters marked as ‘NEW’, which have not been reviewed yet.

Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date. They will also be able to select one or more clinical service(s).

Clinic Service Total Summary Report Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Service Summary Data Report PAGE: 1</p>
<p>For Encounters Dated 12/16/06 THRU 3/26/07 For Service: ALL</p>
<p>VBA OK REVIEW SC to NSC NSC to SC SC KEPT NEW</p>
<p>-------------------------------------------------------------------------------</p>
<p>MEDICINE</p>
<p>CLINIC ONE 0 1 0 0 1 10</p>
<p>MEDICINE SWO 0 0 0 0 0 1</p>
<p>--------- --------- --------- --------- --------- ---------</p>
<p>Subtotal MEDICINE 0 1 0 0 1 11</p>
<p>SURGERY</p>
<p>BU-GEN SURG RAINSTEI 0 0 0 0 0 5</p>
<p>--------- --------- --------- --------- --------- ---------</p>
<p>Subtotal SURGERY 0 0 0 0 0 5</p>
<p>--------- --------- --------- --------- --------- ---------</p>
<p>TOTAL 0 1 0 0 1 16</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Compile Results Report \[SDSC CHECK COMPILE\]

This report prints the reasons why encounters were not compiled into the SDSC SERVICE CONNECTED CHANGES file (#409.48). For a given date range, users can choose from a summary or detail format. The start date of the report is based on the value defined for the SDSC Site Parameter. The Detail reports provide the same information as the summary and additional information on only those encounters with diagnosis code related reasons.

Compile Results Report – (Summary) Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Compile Results Report – Summary PAGE: 1</p>
<p>For Encounters Dated 11/15/06 THRU 12/15/06</p>
<p># Enc Reason</p>
<p>-------------------------------------------------------------------------------</p>
<p>1 A diagnosis fully matched a rated disability condition</p>
<p>3 No Diagnoses for this encounter</p>
<p>-------------------------------------------------------------------------------</p>
<ol start="4" type="1">
<li><p>TOTAL Encounters</p></li>
</ol>
<p>* Third Party=TP; Means Test=MT</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Compile Results Report – (Detail) Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Compile Results Report – Summary PAGE: 1</p>
<p>For Encounters Dated 11/15/06 THRU 12/15/06</p>
<p># Enc Reason</p>
<p>-------------------------------------------------------------------------------</p>
<p>1 A diagnosis fully matched a rated disability condition</p>
<p>3 No Diagnoses for this encounter</p>
<p>-------------------------------------------------------------------------------</p>
<p>4 TOTAL Encounters</p>
<p>Compile Results Report - Detail</p>
<p>For Encounters Dated 11/15/06 THRU 12/15/06</p>
<p>Enc # Visit # Clinic Encounter Date/Time Patient Name</p>
<p>Reason</p>
<p>-------------------------------------------------------------------------------</p>
<p>2688336 2361624 CLINIC ONE 11/15/2006@09:00 PMS,ONE</p>
<p>A diagnosis fully matched a rated disability condition</p>
<p>2688337 2361625 CLINIC TWO 11/15/2006@09:00 PMS,TWO</p>
<p>No Diagnoses for this encounter</p>
<p>2688341 2361629 CLINIC THREE 11/15/2006@11:00 PMS,THREE</p>
<p>No Diagnoses for this encounter</p>
<p>2688343 2361631 CLINIC FOUR 11/15/2006@13:00 PMS,FOUR</p>
<p>No Diagnoses for this encounter</p>
<p>10 TOTAL Encounters</p>
<p>* Third Party=TP; Means Test=MT</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Estimated Recovered Costs Report \[SDSC RECOVERED REPORT\]

This report prints bills and payments for outpatient encounters where the Service Connected value has been changed from SC to NSC using the ASCD options.

The report can be printed for a specified date range for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date. The report requires a 132-column format.

The Estimated Recovered Cost Report may not accurately reflect payments and reimbursements. One problem is due to the fact that the system can bill several outpatient co-payment charges on the same receivable in AR. Payments are applied to the outstanding balance of the receivable, not to specific charges that compose the receivable. So there is the possibility that there will be multiple encounters where the "Principal Bill" amount will be less than the "Principal Pay" amount. In addition, the Total First Party (paid) amount will be overstated, because there is the chance of counting the payment on a receivable more than once.

Estimated Recovered Costs Report Example:

Recovered Costs Report by Division: ALL Run Date: Oct 28, 2005@13:41:48 Page 1

Enc \# Patient Enc Date Change Date Auth Date Pay Date Prncpl Bill Prncpl Pay

------------------------------------------------------------------------------------------------

3514166 PMS,ONE (0001) 01/07/2004 09/23/2004 09/23/2004 15.00 0.00

------------------------------------------------------------------------------------------------

TOTAL FIRST PARTY: 15.00 0.00

3507193 PMS,TWO (0002) 01/02/2004 01/22/2004 350.13 0.00

3507266 PMS,THREE (0003) 01/02/2004 01/17/200 01/27/2004 46.73 22.38

3508792 PMS,FOUR (0004 ) 01/05/2004 09/23/2004 01/16/2004 94.47 0.00

3509818 PMS,FIVE (0005) 01/05/2004 09/23/2004 01/13/2004 02/02/2004 39.72 7.94

3510085 PMS,SIX (0006) 01/05/2004 01/10/2004 69.52 0.00

3511104 PMS,SEVEN (0007) 01/06/2004 09/23/2004 02/10/2004 46.73 0.00

-------------------------------------------------------------------------------------------------

THIRD PARTY TOTAL: 647.30 30.32

------------------------------------------------------------------------------------------------

TOTAL FOR BOTH: 662.30 30.32

TOTAL PAGE FOR 3 DIVISIONS

Estimated Recovered Costs Report by Division(s): KINGMAN CBOC,LAKE HAVASU CITY,COTTONWOOD,

Run Date: Oct 28, 2005@13:42:30 Page 2

Prncpl Bill Prncpl Pay

--------------------------------------------------------------------------------------------

FIRST PARTY TOTAL

COTTONWOOD 0.00 0.00

KINGMAN CBOC 0.00 0.00

LAKE HAVASU CITY 0.00 0.00

---------------------------------------------------------------------------------------------

THIRD PARTY TOTAL

COTTONWOOD 0.00 0.00

KINGMAN CBOC 46.73 22.38

LAKE HAVASU CITY 94.47 0.00

---------------------------------------------------------------------------------------------

TOTAL FOR BOTH FIRST AND THIRD PARTY

141.20 22.38

\<End of Report\>

#### First Party Billable Service Connected Report \[SDSC FIRST PARTY REPORT\]

This report prints information on any outpatient encounters that are potentially billable to first party (means test).

The report can be printed for a specified date range for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

First Party Billable Service Connected Report Example:

OUTPATIENT ENCOUNTERS POTENTIALLY BILLABLE FOR CO-PAYS PAGE: 1

FOR ENCOUNTERS DATED 10/1/06 THRU 2/26/07 By Division: ALL

DATE PATIENT ENCOUNTER

01/07/2004@10:00 PMS,ONE (0001) 3514166

01/09/2004@13:00 PMS,TWO (0002) 3518457

\<End of Report\>

#### Manager Summary Report \[SDSC MANAGER SUMMARY REPORT\]

This report prints totals for the following information pertaining to the ASCD outpatient encounters:

\# of checked out encounters

ASCD encounters that are potentially billable

Encounters with rated disability codes

SC was NOT changed

Changed from SC to NSC

Changed from NSC to SC

Clinical Review

Not editable

Not yet processed

The report can be printed for a specified date range for one or more divisions and will search through ‘All’ checked out outpatient encounters or just the ‘Compiled ASCD Encounters Only’. Users provide a start date, which cannot be greater than the value defined for the SDSC Site Parameter. The end date can be any date beginning with the start date through current date. This report is LOCKED by the SDSC SUPER security key.

Managers Summary Report – (All) Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Managers Summary Data Report PAGE: 1</p>
<p>For Encounters Dated 10/1/06 THRU 2/26/07 For Division: ALL</p>
<p>------------------------------------------------------------------------------</p>
<p>All Checked Out Encounters: 57</p>
<p>ASCD Encounters that are potentially billable: 56</p>
<p>-------</p>
<p>Encounters verified with Rated Disability Codes: 28</p>
<p>Encounters where SC NOT changed: 4</p>
<p>Encounters where SC was changed to NSC: 0</p>
<p>Encounters where NSC was changed to SC: 1</p>
<p>Encounters sent to Clinical Review: 2</p>
<p>Encounters not editable: 0</p>
<p>Encounters not yet processed: 21</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Managers Summary Report – (Compiled) Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Managers Summary Data Report PAGE: 1</p>
<p>For Encounters Dated 10/1/06 THRU 2/26/07 For Division: ALL</p>
<p>-------------------------------------------------------------------------------</p>
<p>ASCD Encounters that are potentially billable: 56</p>
<p>-------</p>
<p>Encounters verified with Rated Disability Codes: 28</p>
<p>Encounters where SC NOT changed: 4</p>
<p>Encounters where SC was changed to NSC: 0</p>
<p>Encounters where NSC was changed to SC: 1</p>
<p>Encounters sent to Clinical Review: 2</p>
<p>Encounters not editable: 0</p>
<p>Encounters not yet processed: 21</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Provider Service Connected Encounters Report \[SDSC PROVIDER REPORT\]

This report prints information regarding ASCD outpatient encounters and it is sorted by the primary provider for the encounter/visit.

The report can be printed using either a summary or detail format within a specified date range and one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

\* The ‘VBA SC’ column refers to whether any encounter diagnosis was matched to a diagnosis code associated with a rated disability code. Values are ‘YES’ or ‘NO’.

\*\* The ‘User SC’ column refers to the user assigned service connected value for an encounter based upon their review of the encounter. Values are ‘YES’, ‘NO’, or ‘TBD (to be determined)’.

Provider Service Connected Encounters Report – (Summary) Example:

> OUTPATIENT ENCOUNTERS SERVICE CONNECTED REVIEW BY PROVIDER PAGE: 1

> FOR ENCOUNTERS DATED 11/15/06 THRU 12/15/06 By Division: ALL

> ENCOUNTER DATE PATIENT NAME ENC \# VBA SC USER SC

> PROVIDER,ONE

> 11/15/2006@08:00 PMS,ONE(0001) 2688333 YES NO

> 11/15/2006@11:00 PMS,TWO(0002) 2688340 YES NO

> 11/15/2006@13:00 PMS,THREE(0003) 2688342 YES NO

> Total: 3

> 11/15/2006@11:00 PMS,TWO(0002) 2688340 YES NO

> 11/15/2006@13:00 PMS,THREE(0003) 2688342 YES NO

> Total: 3

> \<End of Report\>

Provider Service Connected Encounters Report – (Detail) Example:

OUTPATIENT ENCOUNTERS SERVICE CONNECTED REVIEW BY PROVIDER PAGE: 1

FOR ENCOUNTERS DATED 11/15/06 THRU 12/15/06 By Division: ALL

ENCOUNTER DATE PATIENT NAME ENC \# VBA SC USER SC

PROVIDER,ONE

11/15/2006@08:00 PMS,ONE (0001) 2688333 YES NO

POVs/ICDs:

780.6 FEVER

460\. ACUTE NASOPHARYNGITIS

Rated Disabilities:

7005 ARTERIOSCLEROTIC HEART DISEASE (60%-SC)

7913 DIABETES MELLITUS (20%-SC)

6013 GLAUCOMA (10%-SC)

6260 TINNITUS (10%-SC)

11/15/2006@11:00 PMS,TWO(0002) 2688340 YES NO

POVs/ICDs:

780.6 FEVER

Rated Disabilities:

7005 ARTERIOSCLEROTIC HEART DISEASE (60%-SC)

7913 DIABETES MELLITUS (20%-SC)

6013 GLAUCOMA (10%-SC)

6260 TINNITUS (10%-SC)

Total: 2

\<End of Report\>

#### Provider Total Summary Report \[SDSC PROVIDER TOTAL REPORT\]

This report prints totals of the ASCD encounters for the categories listed below per each provider:

- Number of outpatient encounters where ASCD automatically matched the encounter diagnosis with at least one (1) diagnosis associated with the patient’s rated disability codes (partial match) - VBA OK.
- Number of outpatient encounters marked as ‘Service Connected=YES’ but were changed to ‘Service Connected =NO’ - SC to NSC.
- Number of outpatient encounters marked as ‘Service Connected=NO’ but were changed to ‘Service Connected=YES’ – NSC to SC.
- Number of outpatient encounters marked as ‘Service Connected=YES’ or ‘Service Connected = No’ that were not changed.- SC KEPT.
- Number of outpatient encounters marked as ‘NEW’ which have not been reviewed yet.

The report can be printed for a specified date range for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

Provider Total Summary Report Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Provider Summary Data Report PAGE: 1</p>
<p>For Encounters Dated 2/18/07 THRU 3/20/07 By Division: ALL</p>
<p>VBA OK SC to NSC NSC to SC SC KEPT NEW</p>
<p>-------------------------------------------------------------------------------</p>
<p>PROVIDER,ONE 0 0 0 0 2</p>
<p>------- ------- ------- ------- -------</p>
<p>TOTAL 0 0 0 0 2</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Service Connected Encounters Report \[SDSC ENC REPORT\]

This report prints details of the current status of each outpatient encounter found in the SDSC SERVICE CONNECTED CHANGES file (#409.48).

The report can be printed for a specified date range and for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

Service Connected Encounters Report – (All) Example:

> O/P ENCOUNTERS THAT ARE SERVICE CONNECTED & NON SERVICE CONNECTED PAGE: 1

> ENCOUNTERS DATED 10/1/06 THRU 2/26/07 By Division: ALL

> DATE PATIENT ENCOUNTER SC VALUE

> 10/04/2006@11:00 PIMS,SERCONVET RD (5434) 2688296 YES

> POVs/ICDs:

> V72.6 LABORATORY EXAMINATION

> Rated Disabilities:

> 7005 ARTERIOSCLEROTIC HEART DISEASE (60%-SC)

> 7913 DIABETES MELLITUS (20%-SC)

> 6013 GLAUCOMA (10%-SC)

> 6260 TINNITUS (10%-SC)

> 10/04/2006@12:42 PMS,SC VET (7388) 2688291 NO

> POVs/ICDs:

> 345.10 GEN CNV EPIL W/O INTR EP

> 355.8 MONONEURITIS LEG NOS

> 244.9 HYPOTHYROIDISM NOS

> Rated Disabilities:

> 8045 TRAUMATIC BRAIN DISEASE (40%-SC)

> 5296 LOSS OF PART OF SKULL (10%-SC)

> 8045 TRAUMATIC BRAIN DISEASE (10%-SC)

> \<End of Report\>

#### Third Party Billable Service Connected Report \[SDSC THIRD PARTY REPORT\]

This report prints information on any ASCD encounters that are potentially billable to third party (insurance).

The report can be printed for a specified date range and for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

Third Party Billable Service Connected Report Example:

OUTPATIENT ENCOUNTERS POTENTIALLY BILLABLE TO INSURANCE PAGE: 1

FOR ENCOUNTERS DATED 10/1/06 THRU 2/26/07 By Division: ALL

DATE PATIENT ENCOUNTER

01/05/2004@08:00 PMS, ONE (0001) 3508792

01/05/2004@08:30 PMS, TWO (0002) 3508961

01/05/2004@13:00 PMS, THREE (0003) 3510196

01/05/2004@13:30 PMS, FOUR(0004) 3509818

\<End of Report\>

#### #### Unbilled/Billable Amount Report \[SDSC UNBILL AMT REPORT\]

This report prints Billing information for reviewed ASCD encounters ONLY, whose SC value changed from 'SC' to 'NSC' and have not yet been billed or whose SC value changed from 'NSC' to 'SC' which have already been billed. Users holding the SDSC SUPER key will have the ability to print the Supervisor report, which prints the names of the last two editors of the ASCD encounter record.

The report can be printed for a specified date range and for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

Unbilled/Billable Amount Report – (Regular) – (NSC to SC) Example:

Unbilled/Billable Amount Report – (Supervisor) – (SC to NSC) Example:

Unbilled/Billable Amount Report – (Supervisor) – (SC to NSC) Example:

#### #### #### #### #### #### #### #### User Service Connected Encounters Report \[SDSC USER REPORT\]

This report prints details or a summary of ASCD encounters sorted by the user who last edited the service connection information for the encounter.

The report can be printed for a specified date range for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

User Service Connected Encounters Report – (Summary) Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>OUTPATIENT ENCOUNTERS SERVICE CONNECTED REVIEW BY USER PAGE: 1</p>
<p>FOR ENCOUNTERS DATED 1/2/04 THRU 3/1/04 By Division: ALL</p>
<p>ENCOUNTER DATE ENC # VBA SC USER SC STATUS DATE LAST EDITED</p>
<p>PMS, ONE</p>
<p>01/02/2004@09:15 3507237 NO NO COMPLETED OCT 04, 2005</p>
<p>01/02/2004@09:40 3507200 NO NO COMPLETED OCT 28, 2005</p>
<p>01/02/2004@10:00 3507193 NO NO COMPLETED OCT 12, 2005</p>
<p>01/02/2004@10:00 3507266 NO NO COMPLETED OCT 13, 2005</p>
<p>01/02/2004@15:15 3507936 NO NO COMPLETED OCT 13, 2005</p>
<p>01/05/2004@08:00 3508792 NO NO COMPLETED OCT 13, 2005</p>
<p>01/05/2004@08:30 3508961 NO NO COMPLETED OCT 13, 2005</p>
<p>01/05/2004@08:30 3510088 NO NO COMPLETED OCT 28, 2005</p>
<p>01/05/2004@13:00 3510196 NO NO COMPLETED OCT 13, 2005</p>
<p>01/05/2004@13:00 3510326 NO NO COMPLETED OCT 04, 2005</p>
<p>01/05/2004@14:00 3509857 NO NO COMPLETED OCT 13, 2005</p>
<p>01/05/2004@14:30 3510085 NO NO COMPLETED OCT 13, 2005</p>
<p>Total: 12</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

User Service Connected Encounters Report – (Detail) Example:

OUTPATIENT ENCOUNTERS SERVICE CONNECTED REVIEW BY USER PAGE: 1

FOR ENCOUNTERS DATED 1/1/04 THRU 11/12/04

ENCOUNTER DATE ENC \# VBA SC USER SC STATUS DATE LAST EDITED

PMS, ONE

01/02/2004@09:40 3507200 NO YES COMPLETED SEP 23, 2004

POVs/ICDs:

428.0 CONGEST HEART FAIL UNSPECIFIED

702.0 ACTINIC KERATOSIS

427.31 ATRIAL FIBRILLATION

276.8 HYPOPOTASSEMIA

Rated Disabilities:

6100 IMPAIRED HEARING (20%-SC)

5310 FOOT INJURY (10%-SC)

5318 GRP XVIII - PELVIC GIRDLE GRP 3 (10%-SC)

6260 TINNITUS (10%-SC)

5310 FOOT INJURY (10%-SC)

5314 THIGH MUSCLE INJURY (10%-SC)

Total: 1

\<End of Report\>

#### User Total Summary Report \[SDSC USER TOTAL REPORT\]

This report prints totals of the ASCD encounters under the following categories per user:

SET TO REVIEW Number of outpatient encounters set to Clinical Review.

SC to NSC Number of outpatient encounters marked as 'Service

Connected=YES' but were changed to 'Service Connected =NO'.

NSC to SC Number of outpatient encounters marked as 'Service

Connected=NO' but were changed to 'Service Connected=YES'.

SC KEPT Number of outpatient encounters marked as 'Service

Connected=YES' or 'Service Connected = No' that were not changed.

The report can be printed for a specified date range for one or more divisions. Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date.

User Total Summary Report Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>User Summary Data Report PAGE: 1</p>
<p>For Encounters Dated 10/1/06 THRU 2/26/07 By Division: ALL</p>
<p>SET TO REVIEW SC to NSC NSC to SC SC KEPT</p>
<p>-------------------------------------------------------------------------------</p>
<p>USER,ONE 1 2 3 2</p>
<p>USER,TWO 0 11 0 25</p>
<p>------- ------- ------- -------</p>
<p>TOTAL 1 13 3 27</p>
<p>&lt;End of Report&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Compile ASCD Encounters on a Nightly Basis \[SDSC NIGHTLY COMPILE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option gathers encounters that have been updated or encounters with late identified insurance by performing a search on the OUTPATIENT ENCOUNTER file (#409.68). ONLY the previous day encounter records are searched.

This option is NOT interactive and must be scheduled to run daily. It is highly recommended you schedule the option after installing the ASCD software. This option is similar to the Compile ASCD Encounters by Date Range \[SDSC COMPILE\] Option.

### Purge ASCD NSC Encounters \[SDSC PURGE NSC ENC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will purge ASCD encounters with a status of NEW where the encounter SC value equals the ASCD value of "NO" for a specified division(s) within a user defined date range.

Users provide a start date which cannot be greater than the date of the first outpatient encounter within the SDSC SERVICE CONNECTED CHANGES file (#409.48). The end date can be any date beginning with the start date through current date. User may choose to print the report to a device so as to have a record of the encounters deleted. Users must have the SDSC SUPER key to run this option.

Purge ASCD NSC Encounters Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Please enter START date: 101106 (OCT 11, 2006)</p>
<p>Please enter END date: Jun 11, 2007// (JUN 11, 2007)</p>
<p>1 DAYTON</p>
<p>2 SPRINGFIELD</p>
<p>3 MIDDLETOWN</p>
<p>4 LIMA</p>
<p>5 RICHMOND</p>
<p>6 ALL</p>
<p>Select DIVISION: (1-6): 6//</p>
<p>This option will permanently remove the outpatient encounters that are at a</p>
<p>NEW status when both the Encounter SC value and the ASCD value are 'NO' from</p>
<p>the SDSC SERVICE CONNECTED CHANGES file (#409.48).</p>
<p>Are you sure you want to continue? N// YES</p>
<p>DEVICE: HOME// UCX/TELNET Right Margin: 80//</p>
<p>Purge ASCD NSC Encounters PAGE: 1</p>
<p>For Encounters Dated 10/11/06 THRU 6/11/07 For Division: ALL</p>
<p>Encounter Date Encounter No. Patient Name Provider SC Val</p>
<p>-------------------------------------------------------------------------------</p>
<p>10/11/06@09:00 22148 PATIENT,ONE PROVIDER,ONE NO</p>
<p>11/8/06@08:00 22185 PATIENT,TWO PROVIDER,TWO NO</p>
<p>11/14/06@08:00 22189 PATIENT,TWO PROVIDER,ONE NO</p>
<p>12/7/06@08:30 22194 PATIENT,FOUR PROVIDER,SIX NO</p>
<p>12/13/06@10:00 22204 PATIENT,TEN PROVIDER,NINE NO</p>
<p>12/18/06@08:00 22206 PATIENT,TWENTY PROVIDER,EIGHT NO</p>
<p>Number of NSC Records Purged: 6 for ALL</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the new and modified files and fields for the ASCD software.

### New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new file, \#409.48, has been added to the SCHEDULING package. This file contains a list of encounters which were selected for review based on a comparison of the encounter’s ICD9 diagnosis codes and the patient’s mapped VBA rated disabilities/ICD9 codes.

#### SDSC SERVICE CONNECTED CHANGES (#409.48) file

Field Number Field Name

.01 OUTPATIENT ENCOUNTER

.02 DATE LAST EDITED

.03 LAST EDITED BY

.04 DATE CREATED

.05 STATUS

.06 SERV. CONNECT (OK BY USER?)

.07 DATE OF ENCOUNTER

.08 PRIMARY PROVIDER

.09 SERV. CONNECT (OK BY VBA/ICD?)

.1 CLAIMS TRACKING ENTRY

.11 PATIENT

.12 DIVISION

.13 SERV. CONNECT (ORIGINAL VALUE)

1 TRACK EDITS - (SUB-FILE (#409.481) Multiple)

#### TRACK EDITS SUB-FILE (#409.481)

Field Number Field Name

.01 EDIT NUMBER

.02 DATE EDITED

.03 EDITED BY

.04 TYPE OF ENTRY

.05 SERV. CONNECT (OK BY USER?)

.06 REVIEW REQUIRED?

### Modified Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File \#31 a part of the HINQ package was modified. A new sub-file multiple field has been created and populated with the new mapping of patient RATED DISABILITIES (VA) and ICD-9-CM codes supplied by the Veterans Health Administration (VHA) office.

#### DISABILITY CONDITION (#31) file

Field Number Field Name

20 RELATED ICD9 CODES - (SUB-FILE (#31.01) Multiple)

#### RELATED ICD9 CODES SUB-FILE (#31.01)

Field Number Field Name

.01 RELATED ICD9 CODES

.02 ICD9 MATCH

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new mail group, SDSC NIGHTLY TALLY, was created for the ASCD project. This mail group is used by the Compile ASCD Encounters on a Nightly Basis \[SDSC NIGHTLY COMPILE\] and Compile ASCD Encounters by Date Range \[SDSC COMPILE\] options to generate a MailMan message containing their results for distribution to the group members.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Allocation of Security Keys \[XUKEYALL\] option of the Key Management \[XUKEYMGMT\] menu, allocate the following security keys to the appropriate personnel.

- SDSC CLINICAL

> This key should be assigned to a person (usually a physician) who should be able to review encounters set to a status of REVIEW in the ASCD system.

- SDSC SUPER

> This key should be assigned to a supervisor who should be able to review encounters set to all statuses in the ASCD system.

> Locked Menus

> The following menu options are LOCKED by the SDSC SUPER security key:

> ASCD Compile Parameter \[SDSC SITE PARAMETER\]

> Manager Summary Report \[SDSC MANAGER SUMMARY REPORT\]

> Purge ASCD NSC Encounters \[SDSC PURGE NSC ENC\]

### Parameter Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of patch SD\*5.3\*495 will create the initial value of 30 DAYS for the SDSC SITE PARAMETER. This value is used by some of the options in the ASCD software. For example, it is used to control the number of days that the manual compile can be run when searching the OUTPATIENT ENCOUNTER (#409.68) file for encounters that need additional review for final service connected determination.

### Background Option Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Compile ASCD Encounters on a Nightly Basis \[SDSC NIGHTLY COMPILE\] option should be scheduled to run nightly. Use the Schedule/Unschedule Options \[XUTM SCHEDULE\] option to set it up (i.e. RESCHEDULING FREQUENCY: D@2AM).

### SCOUT – Class III File Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site is running the Class III Service Connection Objective Update Tool (SCOUT) software, a file conversion will run and file all valid outpatient encounter records from the Class III ANU SERVICE CONNECTED CHANGES FILE (#626140) into the Class I SDSC SERVICE CONNECTED CHANGES FILE (#409.48). The new file will enable users to process the outpatient encounter records from the ASCD file.

The installation of patch SD\*5.3\*495 will create a background job to run this conversion. A mailman message detailing the conversion results will be sent to the installer of the patch. Please review patch SD\*5.3\*495 for complete details on the file conversion and mailman message output.

### SCOUT – Deactivation of Class III software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that all options under the Class III SCOUT software be deactivated upon successful startup and implementation of the ASCD software.