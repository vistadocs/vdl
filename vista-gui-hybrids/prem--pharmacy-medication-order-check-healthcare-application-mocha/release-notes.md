---
consolidated_title: "mocha server release notes"
app_code: PREM
doc_type: RN
master_source: "PREM*4*1 MOCHA Server Version 4 Release Notes"
master_pub_date: June 2024
consolidated_from: 2 versions
prior_versions:
  - "PREM*3*3 MOCHA Server Version 3.2 Release Notes"
---

## Table of Contents

  - [## Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [This Release](#this-release)
    - [New Features and Functions Added](#new-features-and-functions-added)
    - [Enhancements and Modifications to Existing](#enhancements-and-modifications-to-existing)
  - [Known Issues](#known-issues)
  - [Product Documentation](#product-documentation)
---
title: |
  <span id="_Toc205632711" class="anchor"></span>Medication Order Check Healthcare Application (MOCHA) 4.0
  PREM\*4\*1
  Release Notes
---
![](prem-4-1-mocha-server-version-4-release-notes/001.png)
June 2024
Office of Information and Technology (OIT)
Table of Contents

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The First Databank (FDB) Framework (Fwk) Upgrade Project provided innovative enhancements to Clinical Decision Support (CDS) within the Veterans Health Administration (VHA). Medication order checks are accomplished through the synergistic functionality of multiple applications, including Medication Order Check Healthcare Application (MOCHA), Pharmacy Product System-National (PPS-N), and Data Update (DATUP).

MOCHA Server is a Java Enterprise Edition (JEE) application, used by the MOCHA Veterans Health Information Systems and Technology Architecture (VistA) Pharmacy Application to perform enhanced order checks using the FDB MedKnowledge Framework. MOCHA Server is a VA-built custom web application; it is not a legacy or commercial off the shelf (COTS) application or an Enterprise Shared Service (ESS). FDB MedKnowledge Framework is a drug data product that provides the latest identification and safety information on medications, along with the latest algorithms used to perform order checks.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to MOCHA version (v) 4.0 First Databank (FDB) Framework (Fwk) Upgrade v4.5 for this release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of MOCHA FDB Fwk Upgrade v4.5 and applies to the changes made between this release and any previous release for this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issue for MOCHA 4.0 / FDB Fwk Upgrade v4.5 PREM\*4\*1.

### New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable (N/A) to the FDB Fwk Upgrade v4.5 MOCHA 4.0 / PREM\*4\*1 release.

### Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHA, Patient Care Services, and Pharmacy Benefits Management (PBM) has requested the FDB Fwk upgrade from version 3.3 to version 4.5 for VA Pharmacy applications. MOCHA Server will be upgrading the Application Programming Interface calls in support of the FDB Fwk version 4.5 upgrade.

The following are the enhancements and modifications to the FDB Fwk Upgrade version 4.5 MOCHA 4.0 / PREM\*4\*1 release.

- FDB Fwk v4.5 Application Programming Interfaces (APIs) to be integrated into the MOCHA application. The vendor documentation has the behavioral and content differences between version 3.3 and 4.5
  - FDB-1034 - Upgraded Drug Information Service
  - FDB-781 - Upgraded Order Check Service which affects the following:
    - Drug-Drug Interaction Check
    - Dosing Order Check
    - Drug Allergy Check
    - Duplicate Therapy Check
  - FDB-780 - Upgraded Dosing Info Service
    - Neonatal dosing records are now contained in the same FDB results with the normal DRC search results. See vendor documentation for more detail.
- FDB-2663 - Custom data fields for database version have been removed in version 4.5, we set values in MOCHA XML response to display for DrugVendorDataVo CT_Version fields: CustomBuildVersion, CustomDataVersion, and CustomIssueDate to same values as corresponding FDB published fields
- Dose units are related to VistA file #50 and hard coded in VistA files \#51.24 and #51.25. Some of these values have changed between FDB v3.3 and v4.5
- New Element in FDB v4.5 Response Structure Messages
  - Drug-Drug and Duplicate Therapy checks now have messages being sent in the response from MOCHA to VistA with the 4.5 upgrade. This is a new element in the response structure that wasn’t being sent in 3.3. VistA did not accept the messages in the Drug-Drug and Duplicate Therapy responses and treated them as an exception and therefore would not process and display the order check messages appropriately.
  - Current Workaround: Modified MOCHA code to suppress the message information in the response XML so that VistA continues to process. This allows MOCHA to return responses in the same format as v3.3
- FDB-2727 - Medication Route Mappings for standard and continuous med routes have changes from 3.3 to 4.5
  - Standard Med Route / First Databank Med Route
    - OTIC / OTIC (EAR)
    - OPTHALMIC / OPTHALMIC (EYE)
    - IONTOPHORESIS / IONTOPHORETIC
    - SUBMUCOSAL / SUBMUCOSAL INJECTION
- Additional FDB v4.5 Severity Types Not in Use by VistA
  - FDB v4.4 allows the following severity types:
    - Contraindicated Drug Combination
    - Severe Interaction
    - Moderate Interaction
    - Undetermined Severity – Alternative Therapy Interaction
  - VistA is only concerned with the first two severity types and has the following hard-coded mappings:
    - Contraindicated Drug Combination à Critical (in VistA)
    - Severe Interaction à Significant (in VistA)
- PEPS Services “Check Vendor Database Link” option being handled by VistA to display the Dif DbVersion, difBuildVersion, customDbVersion, and CustomBuildVersion fields for FDB 4.5
- PEPS Services “Check PEPS Services Setup” option displays Critical or Significant for drug-drug interaction check with existing drugs
- Updating the dose units in the inbound drugCheck schema to include the full 4.5 list for request validation. Adding 4.5 Dose Units plurals to the validation list
- FDB-3288 - Option Lookup Dosing Check Information for Drug
- Sustainment releases for PREM\*3\*3 and PREM\*3\*4 have been included in this release
- FDB-3304 - Max Daily Dose ‘below the dosing range’ warning currently displaying when the prescribed dose is below recommended dosing levels for the medication route
  - Below dosing range was turned off
- FDB-4158 - Transformations to accommodate for frequency abbreviations not supported in FDB v4.4 (e.g., X#D)
- FDB-4111 - Lookup Dosing Check Information for a Drug was not displaying for IVs
- FDB-4027 - No reason was provided for continuous epidural route when dose checks could not be performed warning was returned
- FDB-3914 - Alert message was using what appeared to be a different “drug” source
- FDB-3834 - Add route to CPRS alert message when a contraindicated route was chosen (CPRS / VistA)
- FDB-3550 - Incorrect Dose Check Calculation for Short Duration Order
- FDB-3521 - Admixtures were providing message in an improper format
- FDB-3810 - Lower than normal frequency “max daily dose could not be done” in CPRS
- FDB-3532 - Weight Required and BSA Required displayed twice for both Max Single and Max Daily (FDB-3532)
- FDB-3797 - Continuous infusion not able to do dose range check
- FDB-3368 - PSJ OE (Inpatient OE) – Invalid next dosing ID for this dosing set error warning (FDB-3368)
- FDB-3521 - VistA drug interaction message format different
- FDB-3667 - IVPB not showing max daily dose message
- Dosing checks for weight required and general dosing range message not displaying (IV Order Solution premix)
- Drug Allergy Checks and Warning Message displayed for Drug or Drug Class Allergy Reactions
- FDB-2470 - Monograph information is displayed in VistA
- FDB-2471 - Order Check for duplicate therapy check between two drugs in VistA
- FDB-2407 - PEPS Services, Check PEPS Services Setup and Outpatient pharmacy functions
- FDB-2411 - Warning Message when Dosage Exceeds Maximum Single Dose
- FDB-2409 - Validate Maximum Single Dose Order Check for Simple Medication Orders
- FDB-2615 - Order Check Request from VistA for Drug-Drug Interaction Check between one drug and list of drugs
- FDB-2616 - Error Response in VistA when Order Check for Complex Medication Orders
- FDB-2663 - Set values in MOCHA XML response for DrugVendorDataVo CT_Version fields CustomBuildVersion, CustomDataVersion, and CustomIssueDate to same values as corresponding FDB published fields
- FDB-2614 - Maximum Single Dose Order Check with a New IV or Unit Dose Medication Order
- FDB-2890 - VistA: Update M routines to correct PEPS Services “Check Vendor Database Link” option dB version field
- FDB-2960 - VistA: Update M routines to update standard medication route mappings to FDB v4.4
- FDB-2981 - VistA: Update PEPS Services Check PEPS Services Setup “Q4H” dosing check frequency value for FDB v4.4
- FDB-2982 - VistA: Update PEPS Services Check PEPS Services Setup Drug-Drug Interaction Check to allow Critical or Significant result for hard-coded drugs
- FDB-3273 - Validate PSS post init routine to handle dose unit changes for FDB v4.4
- FDB-3726 - Dup drug screens not working (Issue tracker 21)
- FDB-3532 - Weight Required and BSA Required displays twice for both Max Single and Max Daily
- FDB-4609 - Max daily dose not showing in General Dosing Guidelines for Timolol
- FDB-4597 - Nose Drops ordered with SPRAYS dose unit returning: Dosing Checks could not be performed. Reason(s): An unexpected error has occurred.
- FDB-4711 - VistA: UNITS/DAY results in unexpected error
- FDB-4620 - VistA: Invalid dose warning when entering invalid unit of INHALATIONS
- FDB-4605 - VistA: Weight Based Drip – Free Text Dosing in IV package is providing an incorrect error message in both CPRS and pharmacy
- FDB-4623 - VistA: Message for invalid routes is not clear to general end users
- FDB-4655 - VistA: Getting 0 allowances for ACE Inhibitors for Duplicate Therapy
- FDB-4576 - MOCHA: Merge release/fdb-4.0 branch changes into fdb-fwk-upgrade branch to integrate release changes and application security (Fortify, OWASP) remediation
- FDB-3914 - Alert message using what appears to be a different "drug" source
- FDB-4611 - VistA: Unnecessary 'Invalid or Undefined Frequency' message is returned when an invalid route is entered
- FDB-3520 - VistA: Above Range / Within Max
- FDB-3927 - CPRS: Display new contraindicated warning message that was introduced in FDB v4.4
- FDB-4765 - VistA: General dosing guidelines are displayed when frequency is out of range for combo drugs
- FDB-3977 - MOCHA/VistA: Prototype to implement filtering out top-level messages beyond the first whenever subsequent message content is completely contained in the first
- FDB-4540 - CPRS: Update Dose Range Check in CPRS to Display Max Single Dose Messages for Complex Orders
- FDB-4923 - [VistA: Dose Range Check messaging for Complex Orders](https://vajira.max.gov/browse/FDB-4923)
- FDB-3725 - Unable to convert units (Issue tracker \#18)
- FDB-4590 - VistA: (May 2022 UAT Issue tracker \#1) FDB Dosing information is not available for this Drug (CABENUVA)
- FDB-4623 - VistA: (May 2022 UAT Issue Tracker \#11) Message for invalid routes is not clear to general end users
- FDB-5281 - VistA: Rollback of FDB v4.4 frequency format to allow for edit of dosing check frequency in VistA files 51 and 51.1
- FDB-5227 - SQA - (FDB v4.5): Perform timeboxed regression testing of critical features VistA and PPS-N
- FDB-5324 - Create and Execute Test Cases for missing or invalid GCNSEQNO scenarios (FDB-4271) in JIRA
- FDB-5282 - VistA: Apply FDB v4.4 frequency format and convert unsupported frequencies
- FDB-5394 - VistA/CPRS: Remove v3.3 frequency message; allow v4.x frequency messages through
- FDB-5446 - MOCHA: Clean up code references to FDB v4.4.
- FDB-5179 - VistA/CPRS: Perform developer validation of remote order checks
- FDB-5535 - VistA/CPRS/MOCHA: v4.5 Regression Test in SQC
- FDB-5814 - VistA/MOCHA: Unexpected error returned when performing order check for fish oil with GCNSEQNO 73367
- FDB-5611 - VistA MOCHA GCN SEQ: FR 23 Inpatient with drug that has a bad GCNSEQNO and Exclude DDI check is 'NO', Drug level error should display
- FDB-5609 - VistA/MOCHA GCN SEQ: FR 13 Inpatient with drug that has a bad GCNSEQNO and Exclude DDI check is ‘NO’, Exclude from dose ck is 'NO', Override DF dose ck is 'NO' - A drug level error should display.
- FDB-5610 - VistA/MOCHA GCN SEQ: FR 8 Inpatient with drug that has a bad GCNSEQNO and Exclude DDI check is ‘YES’, no message shall be displayed to the user
- FDB-5730 - VistA/MOCHA GCN SEQ: FR 21- Inpatient- when an edit is performed on a unit dose or an IV order through pharmacy backdoor options for a dosing check is performed
- FDB-5731 - VistA/MOCHA GCN SEQ: FR 14- Inpatient The drug level error message will be displayed to a user if an inpatient (IV & UD) order is entered through backdoor options for a drug
- FDB-5732 - VistA/MOCHA: GCN SEQ: FR 6 Outpatient-If an OP order is written for a drug that has a bad GCNSEQNO and EXCLUDE DRG-DRG INTERACTION CK in the VA PRODUCT File is ‘Yes’, no message shall be displayed.
- FDB-5611 - VistA MOCHA GCN SEQ -FR 23 Inpatient with drug that has a bad GCNSEQNO and Exclude DDI check is 'NO', Drug level error should display
- FDB-5604 - VistA: Installing PSS 254 - Orderable Items report that is easy to import into Excel
- FDB-5603 - VistA: Installing PSS 254 - Quick Order report that is easy to import into Excel
- FDB-5907 - MOCHA: Upgrade build to FDB v4.5.10.1
- FDB-5611 - VistA MOCHA GCN SEQ -FR 23 Inpatient with drug that has a bad GCNSEQNO and Exclude DDI check is 'NO', Drug level error should display
- FDB-5833 - VistA/CPRS: If the frequency check status is ‘ExceedsHigh’ Inpatient or outpatient Medications shall display the FDB frequency message
- FDB-6204 - VistA: Update to the Rollback Messaging and PEPS Dev Port
- FDB-6202 - VistA: Update Rollback/Back-out Process Data Handling
- FDB-6114 - MOCHA: Upgrade build to FDB v4.5.10.3 and pass UNKNOWN severityFilter value to Screening.drugDrugScreen()
- FDB-6301 - MOCHA: Update Java codes on the workarounds for drug profile changed by FDB v4.5.10.3
- FDB-6247 - Execute initial remote order check test using DAYTSHR & CHYSHR VistA
- FDB-6009 - VistA: Validate PSS and PSJ rollback using BTN account following re-mirror
- FDB-4600 - VistA/MOCHA: PSS Check PEPS Services Setup - Custom DDI
- FDB-4612 - VistA/CPRS: (May 2022 UAT Issue tracker \#8) Lowercase display of route in general dosing information message CPRS & backdoor
- FDB-6165 - VistA/CPRS/MOCHA: Add drug name prefixed to frequency message
- FDB-6356 - MOCHA: Upgrade build to use FDB v4.5.10.4
- FDB-6367 - MOCHA/VistA: Two Drug-Drug Interaction alerts displayed for VA customized DDI’s
- FDB-4652 - CPRS (May 2022 UAT Issue tracker \#15): Continuous infusion – Free text dosing rate - No weight messaging
- FDB-6011 - VistA / CPRS: As a user, I can see existing VA DDI customizations are available when performing order checks
- FDB-6382 - VistA: Retest PSS Check PEPS Services Setup for VA Custom DDI following upgrade of MOCHA to use FDB v4.5.11.1
- FDB-6688 - VistA/MOCHA: Double equal sign (===) lines above Drug-Drug Interaction alert message
- FDB-4652 - CPRS (May 2022 UAT Issue tracker \#15) Continuous infusion – Free text dosing rate – No weight messaging
- FDB-6382 - VistA: Retest PSS Check PEPS Services Setup for VA Custom DDI following upgrade of MOCHA to use FDB v4.5.11.1
- FDB-5661 - Bug: VistA - Leuprolide and Degarelix drugs-The frequency schedule is for “week” the chemo message is displayed
- FDB-6815 - VistA MOCHA CPRS\_ From PECS - New and Existing DDI Customizations Regression Testing
- FDB-4717 - MOCHA: Upgrade FDB Fwk library to v4.4.16 alpha release to introduce support for dosing frequencies that require greater precision (e.g., greater than every 90 days)
- FDB-6701 - VistA: Validate the extended dosing intervals for LEUPROLIDE ACETATE GCN# 44968 in FDB v4.5 using VistA SQC account
- FDB-5661 - VistA: Leuprolide and Degarelix drugs -The frequency schedule is for “week” the chemo message is displayed
- FDB-5034 - VistA/CPRS: Inconsistent Display of Frequency Messages
- FDB-6069 - VistA/CPRS: As a user, I can see new VA DDI customizations are available when performing order checks
- FDB-6905 - VistA/CPRS: Validate extended dosing intervals for ID 6 (LEUPROLIDE ACETATE 30MG/KIT INJ,SUSP,SA) and ID 18 (PALIPERIDONE PALMITATE 273MG/KIT (3 MONTH) INJ,SUSP,SA )
- FDB-7306 - DATUP/MOCHA: Load Custom File with New Dose Range Record
- FDB-6591 - MOCHA: Update DRC and DPT FDB v4.5 Screening API calls based on guidance from FDB
- FDB-6623 - VistA/MOCHA/CPRS: Create and execute next remote order check tests using DAYTSHR & CHYSHR
- FDB-7439 - DATUP/PECS/MOCHA: (Step 3) Load VA custom update file with New Duplicate Therapy Record
- FDB-6069 - VistA/CPRS: As a user, I can see new VA DDI customizations are available when performing order checks
- FDB-6701 - VistA: Validate the extended dosing intervals for LEUPROLIDE ACETATE GCN# 44968 in FDB v4.5 using VistA SQC account
- FDB-5661 - VistA - Leuprolide and Degarelix drugs-The frequency schedule is for “week” the chemo message is displayed
- FDB-5034 - VistA/CPRS: Inconsistent Display of Frequency Messages
- FDB-6751 - VistA/CPRS: Annual dosing intervals - once a year
- FDB-6795 - VistA/CPRS: Display max daily dose messaging returned by FDB API response for invalid frequencies
- FDB-7009 - MOCHA: Update EAR Config so WebLogic Prefers Spring Classes Packaged in EAR file
- FDB-7030 - VistA/MOCHA- PECS FDB Fwk v4.5_Interim UAT 2023: Issue tracker \#8- Reinstated is a trigger for doing Enhanced Order Checks and it is not acting reliably in outpatient
- FDB-6996 - VistA/MOCHA- PECS FDB Fwk v4.5_Interim UAT 2023: Issue tracker \#4 VistA/MOCHA Existing DDI Scenario#10- Isoniazid and Acetaminophen drugs, not showing Significant drug interaction message twice
- FDB-7552 - VistA/MOCHA/CPRS: Create and execute next remote order check tests concerning discontinued orders using DAYTSHR & CHYSHR
- FDB-7739 - VistA/MOCHA/CPRS: Create and execute remote order tests concerning duplicate therapy checks for expired orders using DAYTSHR & CHYSHR

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- In version 3.3, the dose units are in all uppercase. Version 4.5 the dose units are lowercase. There is no current workaround for this issue.
- In version 3.3, the decimal precision is three decimal places. Version 4.5, the decimal precision is five decimal places. There is no current workaround for this issue.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation describing the new functionality introduced by this patch is available. Upon National Release, the documentation will be in the form of Adobe Acrobat files. Documentation will be found on the VA Software Documentation Library at:

<https://www.va.gov/vdl/application.asp?appid=201>

| File Name                        | Title                                                               | FTP Mode |
|--------------------------------------|-------------------------------------------------------------------------|--------------|
| PREM_4_1_RN.DOCX PREM_4_1_RN.PDF     | MOCHA 4.0 PREM\*4\*1 Release Notes                                      | Binary       |
| PREM_4_1_DIBR.DOCX PREM_4_1_DIBR.PDF | MOCHA 4.0 PREM\*4\*1 Deployment, Installation, Back-Out, Rollback Guide | Binary       |
| PREM_4_1_VDD.DOCX PREM_4_1_VDD.PDF   | MOCHA 4.0 PREM\*4\*1 Version Description Document                       | Binary       |

Table of PSO\*7\*467 Release DocumentationTable includes file description, file name, and FTP mode

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PREM*3*3 MOCHA Server Version 3.2 Release Notes

## Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Server 3.2 updates the code base to comply with software assurance policies to mitigate security vulnerabilities.

## Menu Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No menu changes have been made.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new options have been made.

## Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No options have been changed.

## Deleted Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No options have been deleted.

## New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new files were added to the build for this release. In the case of library files, older versions of these libraries were deleted from the build.

- javax.servlet.javax.servlet-api.jar
- log4j-api-2.14.0.jar
- log4j-core-2.14.0.jar
- commons-collections4-4.4.jar
- esapi-2.2.0.0.jar

## Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for Java Web Service.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for Java Web Service.

## Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new security keys have been created.

## Modified Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Templates have not been modified.
