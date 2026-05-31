---
title: PSS*1*254 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: PSS
app_name: 'Pharmacy: Data Management'
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*254
group_key: PSS:PSS:1
file_numbers:
- '51.23'
security_keys: []
menu_options: 1
description: These release notes cover the changes to Pharmacy Data Management PSS\1\254 for First Databank (FDB) Framework (Fwk) Upgrade v4.5 for this release.
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 2392
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: May 2025
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/PSS_1_0_P254_RN.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/PSS_1_0_P254_RN.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=93
audit_applied: '2026-05-31'
master_source: PSS*1*254 Release Notes
master_pub_date: May 2025
consolidated_from: 7 versions
prior_versions:
- PSS*1*139 Release Notes
- PSS*1*172 Release Notes
- PSS*1*188 Release Notes
- PSS*1*189 Release Notes
- PSS*1*191 Release Notes
- PSS*1*192 Release Notes
consolidated_title: release notes
---

![](pss-1-254-release-notes/001.png)

May 2025

Office of Information and Technology (OIT)

Table of Contents

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The First Databank (FDB) Framework (Fwk) Upgrade Project provided innovative enhancements to Clinical Decision Support (CDS) within the Veterans Health Administration (VHA). The VA applications that are integrated with FDB are Medication Order Check Healthcare Application (MOCHA), Data Update (DATUP), Pharmacy Enterprise Customization System (PECS), Pharmacy Product System-National (PPS-N), and Consolidated Mail Order Pharmacy (CMOP).

The Veterans Health Information Systems and Technology Architecture (VistA) Pharmacy Application, for Pharmacy Data Management, patch PSS\*1\*254 makes changes to the current MOCHA Server which is a Java Enterprise Edition (JEE) application, to work with the upgraded version of FDB. These updates are also made to the Pharmacy Enterprise Product System (PEPS) options.

The following patches are included in the FDB Fwk v4.5 Upgrade: DATUP (PRED\*4\*1, PRED\*4\*2, and PRED\*4\*3), MOCHA (PREM\*4\*1 and PREM\*4\*2), PPS-N (PREN\*4\*1), PECS (PREC\*7\*1), and VistA (PSS\*1\*254, PSJ\*5\*423, and PSO\*7\*779).

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to Pharmacy Data Management PSS\*1\*254 for First Databank (FDB) Framework (Fwk) Upgrade v4.5 for this release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of FDB Fwk Upgrade v4.5 and applies to the changes made between this release and any previous release for this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issue for FDB Fwk Upgrade v4.5 PSS\*1\*254 .

### New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable (N/A) to the FDB Fwk Upgrade v4.5 PSS\*1\*254 release.

### Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHA, Patient Care Services, and Pharmacy Benefits Management (PBM) has requested the FDB Fwk upgrade from version 3.3 to version 4.5 for VA Pharmacy applications. MOCHA Server will be upgrading the Application Programming Interface calls in support of the FDB Fwk version 4.5 upgrade.

The following are the enhancements and modifications to the FDB Fwk Upgrade version 4.5 PSS\*1\*254 release.

- FDB-3288 - Lookup Dosing Check Info For Drug is not displaying any data
- FDB-3490 - PSJ OE (Inpatient OE) - UNK and Blank Reason Suppression
- FDB-3511 - MOCHA/VistA: (Issue Tracker \#9 and \#25) - non-wt based solutions with pre-mix marked as "yes" - get 'dosing checks cannot be done..."
- FDB-3520 - MOCHA/VistA: (Nov 2021 UAT Issue Tracker \#4 and 8) IV Order (PSJ OE/IV) - Above Range / Within Max
- FDB-3532 - MOCHA/VistA: Weight Required and BSA Required displays twice for both Max Single and Max Daily
- FDB-3667 – CPRS/VistA: (Nov 2021 UAT Issue Tracker \#15) IVPB not showing max daily dose message
- FDB-3797 - MOCHA/VistA: (Issue Tracker \#19) - Continuous infusion not able to do dose range check
- FDB-3810 - MOCHA/VistA - (Issue tracker \#27) - lower than normal freq "max daily dose could not be done" in CPRS
- FDB-4027 - MOCHA/VistA: No reason provided for continuous epidural route when dose checks could not be performed warning is returned
- FDB-4590 - VistA: (May 2022 UAT Issue tracker \#1) FDB Dosing information is not available for this Drug (CABENUVA)
- FDB-4597 - VistA: (May 2022 UAT Issue tracker \#4) Nose drops ordered with SPRAYS dose unit returning: Dosing Checks could not be performed. Reason(s): An unexpected error has occurred.
- FDB-4600 - VistA/MOCHA: PSS Check PEPS Services Setup - Custom DDI
- FDB-4605 - VistA: (May 2022 UAT Issue tracker \#5) Weight Based Drip - Free Text Dosing in IV package is providing an incorrect error message in Pharmacy
- FDB-4611 - VistA: (May 2022 UAT Issue tracker \#7) Unnecessary 'Invalid or Undefined Frequency' message is returned when an invalid route is entered
- FDB-4612 - VistA/CPRS: (May 2022 UAT Issue tracker \#8) Lowercase display of route in general dosing information message CPRS & backdoor
- FDB-4623 - VistA: (May 2022 UAT Issue Tracker \#11) Message for invalid routes is not clear to general end users
- FDB-4624 - VistA: (May 2022 UAT Issue tracker \#19) Fosphenytoin MG PE error
- FDB-4628 - VistA: (May 2022 UAT issue tracker 24) Non-free text Day of Week schedule does not give maximum daily dose order check
- FDB-4637 - VistA: (May 2022 UAT issue tracker 22) AlertSpace triggers alerts based on tablet strength and not total dose
- FDB-4638 - VistA: (May UAT issue tracker 17) Alert message using what appears to be a different "drug" source
- FDB-4652 - CPRS (May 2022 UAT Issue tracker \#15) Continuous infusion – Free text dosing rate – No weight messaging
- FDB-4673 - VistA: (May 2022 UAT Issue tracker \#19) GINGER ROOT using units of CAP/TAB getting unexpected error
- FDB-4685 - VistA: (May 2022 UAT Issue tracker \#4) Nose drops ordered with SPRAYS dose unit returning Unable to convert units
- FDB-4711 - VistA: (May 2022 UAT Issue tracker \#5) UNITS/DAY results in unexpected error
- FDB-4765 - VistA: General dosing guidelines are displayed when frequency is out of range for combo drugs
- FDB-4923 - VistA: Dose Range Check messaging for Complex Orders
- FDB-5034 - VistA/CPRS: Inconsistent Display of Frequency Messages
- FDB-5612 - Vista Mocha - GCN SEQ -FR 6 Inpatient order on edit should display a drug level error only ONCE
- FDB-5661 - VistA - Leuprolide and Degarelix drugs-The frequency schedule is for "week" the chemo message is displayed
- FDB-5814 - VistA/MOCHA: Unexpected error returned when performing order check for fish oil with GCNSEQNO 73367
- FDB-6202 - VistA: Update Rollback/Back-out Process Data Handling
- FDB-8871 - PECS/VistA/CPRS: Two monographs associated with the same VA custom DDI
- FDB-7415 - VistA: PSS\*1\*254 and PSJ\*5\*423 VistA FDB v4.5 Production Release
- FDB-2407 - (VistA/MOCHA) PEPS Services \> Check PEPS Services Setup and Outpatient pharmacy functions
- FDB-2409 - MOCHA/VistA: Validate Maximum Single Dose Order Check for Simple Medication Orders
- FDB-2410 - MOCHA/VistA: Validate Maximum Single Dose Order Check for Complex Medication Orders
- FDB-2411 - MOCHA/VistA: Warning Message when Dosage Exceeds Maximum Single Dose
- FDB-2453 - MOCHA/VistA: Drug Allergy Checks and Warning Message Displayed for Drug or Drug Class Allergy Reactions
- FDB-2470 - MOCHA/VistA: Monograph information is displayed in VistA
- FDB-2471 - MOCHA/VistA: Order Check for duplicate therapy check between two drugs in VistA
- FDB-2614 - MOCHA/VistA: Maximum Single Dose Order Check with a New IV or Unit Dose Medication Order
- FDB-2615 - MOCHA/VistA: Order Check Request from VistA for Drug-Drug Interaction Check Between One Drug and List of Drugs
- FDB-2616 - MOCHA/VistA: Error Response in VistA when Order Check Request Cannot be Performed
- FDB-2729 - VistA: Capstone: Update standard medication route mappings in the VistA files to FDB v4.4
- FDB-2890 - MOCHA/VistA: Capstone: Update VistA PEPS Services "Check Vendor Database Link" option DB version field
- FDB-2959 - VistA: Update M routines to correct PEPS Services "Check Vendor Database Link" option dB version field
- FDB-2960 - VistA: Update M routines to update standard medication route mappings to FDB v4.4
- FDB-2981 - VistA: Update PEPS Services Check PEPS Services Setup "Q4H" dosing check frequency value for FDB v4.4 upgrade
- FDB-2982 - VistA: Update PEPS Services Check PEPS Services Setup Drug-Drug Interaction Check to Allow Critical or Significant Result for Hard-coded Drugs
- FDB-3273 - VistA: Validate PSS post init routine to handle dose unit changes for FDB v4.4
- FDB-3365 - MOCHA/VistA/CPRS: Renew/copy/edit existing orders/Rxs in CPRS or VistA
- FDB-3436 - VistA: Installation routine update in PSS\*1\*254 to configure encrypt_only_tlsv12, update PEPS endpoints for DEV/SQA/STAGE, and update PPS-N endpoints for DEV/SQA/STAGE/PREPROD/PROD
- FDB-3499 - VistA: Installation routine update in PSS\*1\*254 to update VistA file 51.23 (standard medication routes) to permitted values for FDB v4.4
- FDB-3501 - VistA: Installation routine update in PSS\*1\*254 to update PEPS endpoints for PREPROD and PROD and PPS-N endpoint for PREPROD
- FDB-3927 - CPRS: Display new contraindicated warning message that was introduced in FDB v4.4
- FDB-3977 - MOCHA/VistA: Prototype to implement filtering out top-level messages beyond the first whenever subsequent message content is completely contained in the first
- FDB-4161 - MOCHA/VistA/CPRS: Prototype to transform frequency abbreviations not supported in FDB v4.4 (e.g., X#D) as VA was using them in v3.3
- FDB-4539 - VistA/CPRS: Bad route messaging
- FDB-4540 - CPRS: Update Dose Range Check in CPRS to Display Max Single Dose Messages for Complex Orders
- FDB-4560 - VistA/CPRS: Continuous IV Dosing Display only the Max Daily Dose Message
- FDB-4868 - VistA: Create new PSS\*1\*254 v19 patch to allow for installation SQC
- FDB-4980 - VistA: Refine process to roll back VistA PSS\*1\*254 and PSJ\*5\*423 patches
- FDB-5281 - VistA: Rollback of FDB v4.4 frequency format to allow for edit of dosing check frequency in VistA files 51 and 51.1
- FDB-5282 - VistA: Apply FDB v4.4 frequency format and convert unsupported frequencies
- FDB-5324 - Create and Execute Test Cases for missing or invalid GCNSEQNO scenarios (FDB-4271) in JIRA
- FDB-5394 - VistA/CPRS: Remove v3.3 frequency message; allow v4.x frequency messages
- FDB-5603 - VistA: Installing PSS 254 - Quick Order report that is easy to import into Excel
- FDB-5604 - VistA: Installing PSS 254 - Orderable Items report that is easy to import into Excel
- FDB-5833 - VistA/CPRS: If the frequency check status is 'ExceedsHigh' Inpatient or outpatient Medications shall display the FDB frequency message
- FDB-6009 - VistA: Validate PSS and PSJ rollback using BTN account following re-mirror
- FDB-6165 - VistA/CPRS/MOCHA: Add drug name prefixed to frequency message
- FDB-6204 - VistA: Update to the Rollback Messaging and PEPS Dev Port
- FDB-6247 - Execute initial remote order check test using DAYTSHR & CHYSHR VistA
- FDB-6354 - VistA/CPRS: As a user, I can see DDIs with UNKNOWN severity levels are available when performing order checks
- FDB-6377 - VistA: Create Test Cases on next remote order check tests using DAYTSHR & CHYSHR
- FDB-6495 - VistA: Peer Review and Execute Test Cases on remote order Test Set \_ DAYTSHR & CHYSHR
- FDB-6508 - Vista /Mocha/CPRS: Create next test cases next remote order check tests using DAYTSHR & CHYSHR
- FDB-6623 - VistA/MOCHA/CPRS: Create and execute next remote order check tests using DAYTSHR & CHYSHR
- FDB-6701 - VistA: Validate the extended dosing intervals for LEUPROLIDE ACETATE GCN# 44968 in FDB v4.5 using VistA SQC account
- FDB-6751 - VistA/CPRS: Annual dosing intervals - once a year
- FDB-6795 - VistA/CPRS: Display max daily dose messaging returned by FDB API response for invalid frequencies
- FDB-6815 - Vista Mocha CPRS\_ From PECS - New and Existing DDI Customizations Regression Testing
- FDB-6905 - VistA/CPRS: Validate extended dosing intervals for ID 6 (LEUPROLIDE ACETATE 30MG/KIT INJ,SUSP,SA) and ID 18 (PALIPERIDONE PALMITATE 273MG/KIT (3 MONTH) INJ,SUSP,SA )
- FDB-7041 - VistA/CPRS: As a user, I can see existing VA DRC customizations are available when performing order checks
- FDB-7042 - VistA/CPRS: As a user, I can see the VA's one existing DPT (Duplicate Therapy) customization is available when performing order checks
- FDB-7260 - VistA/CPRS: Validate extended dosing intervals for IDs 34 (UBLITUXIMAB-XIIY 25MG/ML INJ,SOLN) and 11 (INCLISIRAN 284MG/1.5ML INJ,SOLN,SYR)
- FDB-7303 - VistA/CPRS: As a user, I can see new VA DRC customizations are available when performing order checks
- FDB-7440 - VistA/CPRS: (Step 4) Verify new (DPT) Duplicate Therapy customization is available when performing order checks
- FDB-7526 - VistA/CPRS: As a user, I am able to use 'DOSE ROUTES' introduced in FDB v4.5 when placing orders
- FDB-7552 - VistA/MOCHA/CPRS: Create and execute next remote order check tests concerning discontinued orders using DAYTSHR & CHYSHR (Sprint 29)
- FDB-7669 - VistA/CPRS: (Step 2) Validate modification and deletion of DRC customizations
- FDB-7672 - VistA/CPRS: (Step 2) Validate modification and deletion of DPT customizations
- FDB-7739 - VistA/MOCHA/CPRS: Create and execute remote order tests concerning duplicate therapy checks for expired orders using DAYTSHR & CHYSHR
- FDB-7765 - VistA/CPRS: (Step 2) Validate DRC 'rate field' customizations
- FDB-7835 - VistA/CPRS: (Step 2) As a user, I can see VA DRC customizations for 'DOSE ROUTES' newly introduced in FDB v4.5
- FDB-7913 - VistA/CPRS: (Step 2) As a user, I can see VA DRC customizations for existing 'DOSE UNITS'
- FDB-7915 - VistA/CPRS: (Step 3) As a user, I can see VA DRC customizations 'DOSE UNITS' newly introduced in FDB v4.5
- FDB-8028 - VistA/CPRS: (Step 2) Low and high frequency customizations
- FDB-8118 - VistA: Validate that PSS Drug Dosing Lookup returns FDB routes for drug records having null high half-life values
- FDB-8119 - VistA/CPRS: As a user, I am able to use 'DOSE UNITS' introduced in FDB v4.5 when placing orders
- FDB-8248 - VistA/CPRS: Validate DRC rate field customizations using distinct customization values
- FDB-8349 - VistA/CPRS: (Step 2) Validate Professional Monograph customizations
- FDB-8350 - VistA/MOCHA: Restore Dose Unit on Continuous Rates to Remove Rate
- FDB-8858 - VistA: Address Feedback from DBA Review on File Updates - Route and Unit
- FDB-9102 - VistA/CPRS: Remove dose routes inappropriate for DRC Screening
- FDB-9233 - VistA: FDB Fwk v4.5 Pre-Prod IOC Issue tracker#21: Medication route of perineural did not give expected Max Daily and Frequency Message

# Known Issues


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [## Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [This Release](#this-release)
    - [New Features and Functions Added](#new-features-and-functions-added)
    - [Enhancements and Modifications to Existing](#enhancements-and-modifications-to-existing)
- [Known Issues](#known-issues)
  - [Product Documentation](#product-documentation)
No known issues at the time this was written.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation describing the new functionality introduced by this patch is available. Upon National Release, the documentation will be in the form of Adobe Acrobat files. Documentation will be found on the VA Software Document Library at:

<https://www.va.gov/vdl/application.asp?appid=93>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 41%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong><em> </em></th>
<th><strong>Title</strong><em> </em></th>
<th><strong>FTP Mode</strong><em> </em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PSS_1_0_P254 _RN.DOCX</p>
<p>PSS_1_0_P254 _RN.PDF</p></td>
<td>PSS*1*254 Pharmacy Data Management Release Notes</td>
<td>Binary </td>
</tr>
<tr class="even">
<td><p>PSS_1_0_P254_UM.DOCX</p>
<p>PSS_1_0_P254_UM.PDF</p></td>
<td>Pharmacy Data Management User Manual</td>
<td>Binary<em> </em></td>
</tr>
<tr class="odd">
<td><p>PSS_1_VISTA_TO_MOCHA_ID_P254.DOCX</p>
<p>PSS_1_VISTA_TO_MOCHA_ID_P254.PDF</p></td>
<td>VistA to MOCHA Version 2.1 Interface Document</td>
<td>Binary<em> </em></td>
</tr>
<tr class="even">
<td><p>PSS_1_DOSING_ORD_CK_UM_P254.DOCX</p>
<p>PSS_1_DOSING_ORD_CK_UM_P254.PDF</p></td>
<td>Dosing Order Check Version 2.1 User Manual</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td><p>PSS_1_0_P254_DIBR.DOCX</p>
<p>PSS_1_0_P254_DIBR.PDF</p></td>
<td>PSS*1*254 Pharmacy Data Management Deployment, Installation, Back-out, Rollback Guide</td>
<td>Binary</td>
</tr>
<tr class="even">
<td><p>PSS_1_0_P254_TM.DOCX</p>
<p>PSS_1_0_P254_TM.PDF</p></td>
<td>Pharmacy Data Management Technical Manual/Security Guide</td>
<td>Binary</td>
</tr>
</tbody>
</table>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSS*1*192 Release Notes

## Documentation and Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to retrieve files from <span class="mark">REDACTED</span>.

This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the documentation directly using Secure File Transfer

Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI

Field Offices:

<span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl

Title File Name Transfer Mode

---------------------------------------------------------------------------

Release Notes/Installation Guide PSS_1_P192_RN.PDF Binary

User Manual PSS_1_UM.PDF Binary

*(This page included for two-sided copying.)*

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch Display Page: 1

=============================================================================

Run Date: APR 21, 2016 Designation: PSS\*1\*192 TEST v16

Package : PHARMACY DATA MANAGEMENT Priority : MANDATORY

Version : 1 Status : UNDER DEVELOPMENT

=============================================================================

Associated patches: (v)PSS\*1\*104 \<\<= must be installed BEFORE \`PSS\*1\*192'

(u)PSS\*1\*189 \<\<= must be installed BEFORE \`PSS\*1\*192'

Subject: MCCF ePHARMACY COMPLIANCE PHASE 3

Category: ROUTINE

OTHER

ENHANCEMENT

DATA DICTIONARY

INPUT TEMPLATE

Description:

===========

This patch has enhancements that extend the capabilities of the Veterans

Health Information Systems and Technology Architecture (VistA) electronic

pharmacy (ePharmacy) billing system. Below is a list of all the applications

involved in this project along with their patch number:

APPLICATION/VERSION PATCH

---------------------------------------------------------------

OUTPATIENT PHARMACY (OP) V. 7.0 PSO\*7\*448

INTEGRATED BILLING (IB) V. 2.0 IB\*2\*550

ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*20

CONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP) V. 2.0 PSX\*2\*79

PHARMACY DATA MANAGEMENT (PDM) V. 1.0 PSS\*1\*192

All five of these patches are being released in the Kernel Installation and

Distribution System (KIDS) multi-build distribution.

KIDS multi-build name: BPS PSO IB PSX PSS BUNDLE 9.0

KIDS Host File name: BPS_1_20_PSO_IB_PSX_PSS.KID

This specific patch contains the following functionality:

---------------------------------------------------------

1\. Three new fields for ePharmacy billable assessment have been added to the

Drug File (#50) which will be Yes/No fields:

ePharmacy Billable (#84)

ePharmacy Billable (TRICARE) (#85)

ePharmacy Billable (CHAMPVA) (#86)

The fields will be used in Integrated Billing to assess billable status

for a prescription instead of basing assessment on the DEA, Special HDLG

field.

2\. A new field called Sensitive Diagnosis Drug (#87) has been added to the

Drug File (#50) which will be a Yes/No field. The field is used in

Integrated Billing to assess sensitive diagnosis status for a

Prescription instead of basing the assessment on the DEA, Special HDLG

field.

3\. The system option Drug Enter/Edit \[PSS DRUG ENTER/EDIT\] contains prompts

to allow the user to enter the new ePharmacy data at the main level.

4\. The help text references to "E" and "U" have been removed from the DEA,

Special HDLG field, however, the user will still be able to enter "E" or

"U". If the user enters an "E" or "U" in the DEA, Special HDLG field, a

warning message is displayed indicating the values no longer have any

ePharmacy impact and refer the user to the new fields which replace the

"E" and "U" functionality.

5\. The option Lookup into Dispense Drug File \[PSS LOOK\] displays the

following new ePharmacy values:

ePharmacy Billable

ePharmacy Billable (TRICARE)

ePharmacy Billable (CHAMPVA)

Sensitive Diagnosis Drug

6\. During the patch installation, the system populates the ePharmacy

Billable field according to existing logic based on values in the DEA,

Special HDLG field, and removes the "E" from the DEA, Special HDLG field.

Also, the system populates the Sensitive Diagnosis Drug field to Yes if

the DEA, Special HDLG field contains "U" and removes the "U" from the

DEA, Special HDLG field.

7\. The system generates one post installation report showing the value of

the DEA Special HDLG field before the patch is installed and the value of

the DEA Special HDLG field after the patch is installed and the "E" and

"U" characters are removed. The functions of both characters have been

replaced by the new DRUG file (#50) fields to maintain consistency

throughout the VA. A drug will only be on the report if the value for

the DEA Special HDLG field is changed for that drug. The report also

displays drugs that do not have any value in the DEA Special Handling

Field.

Patch Components:

-----------------

Files & Fields Associated:

File Name (#) New/Modified/

Sub-file Name (#) Field Name (Number) Deleted

------------------- --------------------------------- -------------

DRUG (#50) Modified

EPHARMACY BILLABLE (#84) New

EPHARMACY BILLABLE (TRICARE) (#85) New

EPHARMACY BILLABLE (CHAMPVA) (#86) New

SENSITIVE DIAGNOSIS (#87) New

Forms Associated:

New/Modified/

Form Name File Name (Number) Deleted

--------- ------------------ -------------

N/A

Mail Groups Associated:

New/Modified/

Mail Group Name Deleted

--------------- -------------

N/A

Options Associated:

New/Modified/

Option Name Type Deleted

----------- ---- -------------

N/A

Protocols Associated:

New/Modified/

Protocol Name Deleted

------------- -------------

N/A

Security Keys Associated:

New/Modified/

Security Key Name Deleted

----------------- -------------

N/A

Templates Associated:

New/Modified/

Template Name Type File Name (Number) Deleted

------------- ---- ------------------ -------------

PSSCOMMON Input DRUG (#50) Modified

Additional Information:

N/A

New Service Requests (NSRs)

---------------------------

20140411 - Medical Care Collection Fund (MCCF) ePharmacy Compliance Phase 3

Patient Safety Issues (PSIs)

----------------------------

N/A

Defect Tracking System Ticket(s) & Overview:

--------------------------------------------

N/A

Test Sites:

-----------

<span class="mark">REDACTED</span>

Documentation Retrieval Instructions

------------------------------------

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to retrieve files from <span class="mark">REDACTED</span>.

This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the documentation directly using Secure File Transfer

Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI

Field Offices:

<span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl

Title File Name Transfer Mode

---------------------------------------------------------------------------

Release Notes/Installation Guide PSS_1_P192_RN.PDF Binary

User Manual PSS_1_UM.PDF Binary

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a post-install routine associated with this patch named PSS192PO.

The purpose of the post-install routine is to:

a\. Examine every drug in the Drug file (#50) to determine if it is billable

or not and if the drug is a Sensitive Diagnosis Drug or not.

b\. Set the new ePharmacy Billable field as appropriate.

c\. Set the new Sensitive Diagnosis Drug field as appropriate.

d\. Remove the "E" and "U" characters from the DEA, Special HDLG field.

e\. Identify and report all drugs with a blank DEA, Special HDLG field.

f\. Prepare and send an email message containing all of the Drug file changes

to users who hold the PSO EPHARMACY SITE MANAGER security key.

The post-install routine is automatically deleted by the system if allowed by

your Kernel site parameters configuration. You may delete this routine if the

installation was successful and it is not automatically deleted by KIDS.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please see the Installation Instructions associated with patch BPS\*1.0\*20.

Routine Information:

====================

The second line of each of these routines now looks like:

;;1.0;PHARMACY DATA MANAGEMENT;\*\*\[Patch List\]\*\*;9/30/97;Build 25

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: PSS192PO

Before: n/a After:B100977929 \*\*192\*\*

Routine Name: PSS50

Before: B20914479 After: B25607113 \*\*85,104,192\*\*

Routine Name: PSSDDUT2

Before:B103530932 After:B173773291 \*\*3,21,61,81,95,127,126,139,

131,143,188,189,192\*\*

Routine Name: PSSLOOK

Before: B85846814 After: B89759845 \*\*3,7,15,16,20,24,29,38,68,61,

87,90,127,147,170,189,192\*\*

Routine list of preceding patches: 104, 189

*(This page included for two-sided copying.)*

## Overview of Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not able to be a "one size fits all." The general strategy for VistA rollback is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch; otherwise, the site should contact the Enterprise Program Management Office (EPMO) directly for specific solutions to their unique problems.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA Installation Procedure of the KIDS build, the installer can back up the modified routines using the 'Backup a Transport Global' action. The installer can restore the routines using the MailMan message that were saved prior to installing the patch. The backout procedure for global, data dictionary and other VistA components is more complex and will require issuance of a follow-up patch to ensure all components are properly removed. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with restoration of the data.  This backout may need to include a database cleanup process.

Please contact the EPMO for assistance if the installed patch that needs to be backed out contains anything at all besides routines before trying to backout the patch. If the installed patch that needs to be backed out includes a pre or post install routine please contact the EPMO before attempting the backout.

From the Kernel Installation and Distribution System Menu, select

the Installation Menu.  From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch \#.

    a. Backup a Transport Global - This option will create a backup

       message of any routines exported with this patch. It will not

       backup any other changes such as DD's or templates.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure for VistA patches is complicated and may require a follow-up patch to fully roll back to the pre-patch state. This is due to the possibility of Data Dictionary updates, Data updates, cross references, and transmissions from VistA to offsite data stores.

Please contact the product development team for assistance if needed.

*(This page included for two-sided copying.)*

## System Feature: Drug File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Drug File (#50) contains fields for ePharmacy billable assessment which will be Yes/No fields: ePharmacy Billable, ePharmacy Billable (TRICARE), ePharmacy Billable (CHAMPVA), and Sensitive Diagnosis Drug.

## System Feature: Post Installation Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system generates one post installation report showing the value of the DEA Special HDLG field before the patch is installed and the value of the DEA Special HDLG field after the patch is installed and the "E" and "U" characters are removed. A drug will only be on the report if the value for the DEA Special HDLG field is changed for that drug.

### From: PSS*1*139 Release Notes

## DEA SPECIAL HANDLING CODE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once Outpatient Pharmacy patch PSO\*7\*303 and Integrated Billing patch IB\*2\*405 is installed, any drug defined with this new code will be treated in the same manner as supply items and investigational drugs. The "N" DEA Special Handling code must be defined manually.

VA Facilities should never charge veterans copayments for nutritional supplement prescriptions. Until this enhancement the only method to prevent copayment was to flag items as "S" Supply or "I" Investigational. Neither of these flags is appropriate for nutritional supplements. An additional entry of "N" Nutritional Supplement, in the DEA, SPECIAL HDLG field of the Drug File (#50), was added to address the nutritional supplement issue. The "N" will flag these products to ensure that the patient is not charged a VA copayment. In situations where the prescriptions for these products should still be billed to third parties, an "E" can be appended to the DEA, SPECIAL HDLG field for the drug file entry. Nutritional supplements however are usually <u>not</u> third party reimbursable.

Sites will need to determine all the nutritional supplements in their drug file and mark the DEA, SPECIAL HDLG field entry for all of their nutritional supplements drug file entries with an "N". They will also need to append any entries that may be third party reimbursable with an "E". Usually only Rx Only nutritional supplements are third party reimbursable.

Drug Enter/Edit option example:

Select OPTION NAME: DRUG ENTER/EDIT PSS DRUG ENTER/EDIT Drug Enter/Edit

Drug Enter/Edit

Select DRUG GENERIC NAME: TRAZO

Lookup: GENERIC NAME

1 TRAZODONE 100MG TAB N/F

2 TRAZODONE 50MG TAB

CHOOSE 1-2: 1 TRAZODONE 100MG TAB N/F

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This entry is marked for the following PHARMACY packages:

Outpatient

Non-VA Med

GENERIC NAME: TRAZODONE 100MG TAB//

VA CLASSIFICATION:

DEA, SPECIAL HDLG: 3// ?

ANSWER MUST BE 1-6 CHARACTERS IN LENGTH

THE SPECIAL HANDLING CODE IS A 2 TO 6 POSTION FIELD. IF APPLICABLE,

A SCHEDULE CODE MUST APPEAR IN THE FIRST POSITION. FOR EXAMPLE,

A SCHEDULE 3 NARCOTIC WILL BE CODED '3A', A SCHEDULE 3 NON-NARCOTIC WILL BE

CODED '3C' AND A SCHEDULE 2 DEPRESSANT WILL BE CODED '2L'.

THE CODES ARE:

0 MANUFACTURED IN PHARMACY

1 SCHEDULE 1 ITEM

2 SCHEDULE 2 ITEM

3 SCHEDULE 3 ITEM

4 SCHEDULE 4 ITEM

5 SCHEDULE 5 ITEM

6 LEGEND ITEM

9 OVER-THE-COUNTER

L DEPRESSANTS AND STIMULANTS

A NARCOTICS AND ALCOHOLS

P DATED DRUGS

I INVESTIGATIONAL DRUGS

M BULK COMPOUND ITEMS

C CONTROLLED SUBSTANCES - NON NARCOTIC

R RESTRICTED ITEMS

S SUPPLY ITEMS

B ALLOW REFILL (SCH. 3, 4, 5 ONLY)

W NOT RENEWABLE

F NON REFILLABLE

E ELECTRONICALLY BILLABLE

N NUTRITIONAL SUPPLEMENT

DEA, SPECIAL HDLG: 3//

### From: PSS*1*188 Release Notes

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Updated documentation describing the new functionality introduced by this patch is available.

> The preferred method is to FTP the files from ftp://download.vista.med.va.gov/. This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

> Albany ftp.fo-albany.med.va.gov \<ftp://ftp.fo-albany.med.va.gov\> Hines ftp.fo-hines.med.va.gov \<ftp://ftp.fo-hines.med.va.gov\> Salt Lake City ftp.fo-slc.med.va.gov \<ftp://ftp.fo-slc.med.va.gov\>

> Documentation can also be found on the VA Software Documentation Library at: <http://www4.va.gov/vdl/>

> Title File Name FTP Mode

> Release Notes/Installation Guide PSS_1_P188_RN.PDF Binary

#### (This page included for two-sided copying.)

## Routine Information:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The second line of each of these routines now looks like:

> ;;1.0;PHARMACY DATA MANAGEMENT;\*\*\[Patch List\]\*\*;9/30/97;Build 1

> The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

> Routine Name: PSSDDUT2

Before:B103506254 After:B103530932 \*\*3,21,61,81,95,127,126,139,

> 131,143,188\*\*

> Routine list of preceding patches: 143

## Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Quantity Multiplier field of the Drug File Decimal Increase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The number of decimal digits for the NCPDP QUANTITY MULTIPLIER (#83) field of the DRUG (#50) file was increased from three (3) to five (5) decimal digits.

## Issue Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### This patch addresses the following New Service Request (NSR):

#### - NCPDP Continuous Maintenance Standards (Phase 2, Iteration 2)

### Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### There are no Remedy Tickets associated with this patch.
