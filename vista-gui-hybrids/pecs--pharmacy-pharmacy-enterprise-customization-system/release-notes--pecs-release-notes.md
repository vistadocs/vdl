---
title: PECS Version 2.1 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: null
app_code: PECS
app_name: 'Pharmacy: Pharmacy Enterprise Customization System'
section: GUI
app_status: active
pkg_ns: PECS
patch_ver: 2.1
patch_id: PECS*2.1
group_key: PECS:PECS:2.1
file_numbers: []
security_keys: []
menu_options: 0
description: '> Department of Veterans Affairs Office of Information and Technology'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 608
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: July 2012
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Enterprise_Custom_Sys/pecs_v2_1_release_notes.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Enterprise_Custom_Sys/pecs_v2_1_release_notes.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=204
audit_applied: '2026-05-31'
master_source: PECS Version 2.1 Release Notes
master_pub_date: July 2012
consolidated_from: 4 versions
prior_versions:
- PECS Version 2.2 Release Notes
- PREC*6.2*1 PECS Release Notes
- PREC*7*1 PECS Release Notes
consolidated_title: pecs release notes
---

> Pharmacy Enterprise Customization System (PECS) v2.1

> Release Notes

![](pecs-version-2-1-release-notes/001.png)

> July 2012

> Department of Veterans Affairs Office of Information and Technology (OIT)

> Product Development (PD)

### (This page included for two-sided copying.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  
2.  1.  
    2.  

[Introduction 1](#introduction)[Enhancements 2](#enhancements)[Functional Enhancements 2](#functional-enhancements)[Architectural Enhancements 3](#architectural-enhancements)

### (This page included for two-sided copying.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ii Pharmacy Enterprise Customization System (PECS) July 2012

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
    - [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying-1)
- [Introduction](#introduction)
- [Enhancements](#enhancements)
  - [Functional Enhancements](#functional-enhancements)
  - [Architectural Enhancements](#architectural-enhancements)
> The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues. The first phase, PRE V.0.5, implements enhanced order checking functionality utilizing HealtheVet (HeV) compatible architecture and First DataBank (FDB) Drug Information Framework (DIF) Application Program Interfaces (APIs) and database. Pharmacy Enterprise Customization System (PECS), a Graphical User Interface (GUI) application has been developed for maintenance of FDB custom tables. A process to automatically update the standard and custom FDB data at the local Cache' database is also be provided.
> This release notes document provides a brief description of the new features and functions of PECS v2.1.
> July 2012 Pharmacy Enterprise Customization System (PECS) 1

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PECS v2.1 provides both functional and architectural enhancements.

## Functional Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Advanced Query/Customization:

- Combined selection of business concept and query builder on one page. In PECS 2.0, the user was required to select business concept and query type (VA, FDB, or Both) on the first screen before navigating to the next to build the query.
- Improved complex 'AND / OR' query builder to show additional criterion within the query builder that will allow the user to change the filter and/or criterion anytime while building query.
- Last executed query is displayed in query builder until the user either clears the query or click on Advanced Query/Customization. In PECS 2.0, query builder was initialized when a query was executed.
- New data grid (query results) utilizes dynamic paging, that is, as the user scroll down additional data is retrieved and displayed. The header row is static and does not scroll when the user scroll the data.
- Sort complete dataset by clicking on the column heading.
- User is not allowed to save the query without a name or with a duplicate name.
- Limit the query by action date to the appropriate operators:
  - Greater than or equal to
  - Greater than
  - Less than or equal to
  - Less than
- Require the user to search for FDB or VA records before allowing the user to create a customization record from a blank form.

#### Home Page:

- Individual links to display active records in each status (new, modified, reviewed, approved, rejected, and deleted records). In PECS 2.0, all statuses were combined in one link.

#### Navigation:

- Navigation links are added to the bottom of all pages, these are the same link as the page TABS at the top.
- Ability to navigate from the Drug-Drug Interface (DDI) detail page to Drug Pairs (DP) customization page (existing functionality), associated Professional Monograph (PM) and Corresponding FDB Interaction ID.
- Ability to navigate from DP customization page to parent VA customized Interaction and Corresponding FDB Interaction ID.

#### Messages:

- Added new and updated informational and error messages to provide accurate description.

> 2 Pharmacy Enterprise Customization System (PECS) July 2012

#### Reports:

- Updated to use aliases as column header instead of database field name.
- Updated to export reports in Excel format.

#### Easy Search:

- Drug-Drug Interaction - Ability for the user to view Drug-Drug Interaction data for up to 10 drugs at a time.
- Professional Monograph - Ability for user to view Professional Monographs data returned for one or more Routed Generic(s) selected by the user.
- Duplicate Therapy - Ability for the user to view Therapeutic Drug Class displayed for each drug returned by the PECS Easy Search query.
- Dose Range Check - Ability for the user to view if the amount being prescribed is an acceptable amount based on patient data and dose particulars entered by the user.

#### Dose Range:

- Added business rule requiring the user to enter units when a value in the dose numeric fields is entered.

## Architectural Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Refactoring of code into presentation, business and data layer
- Replaced unapproved tools
- Replaced unapproved libraries

> July 2012 Pharmacy Enterprise Customization System (PECS) 3

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PREC*7*1 PECS Release Notes

## ## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy Reengineering (PRE) Project provided innovative enhancements to Clinical Decision Support (CDS) within the Veterans Health Administration (VHA). Medication order checks are accomplished through the synergistic functionality of multiple applications, including Medication Order Check Healthcare Application (MOCHA), Pharmacy Enterprise Customization System (PECS), Pharmacy Product System-National (PPS-N), and Data Update (DATUP).

The PECS application, through a web-based Graphical User Interface (GUI), allows VHA pharmacists and clinicians to research and request custom changes to Drug-Drug Interaction, Drug Pairs, Dose Range, Duplicate Therapy, and Professional Monograph records, controlling access through a role-based authorization. VHA Pharmacy Benefits Management (PBM) periodically (as needed in support of VA procedures and priorities) prepare, review and approve the customizations, which result in VA Custom drug data, which will supersede or enhance the industry standard FDB-drug data.

The following patches are included in the FDB Fwk v4.5 Upgrade: DATUP (PRED\*4\*1, PRED\*4\*2, and PRED\*4\*3), MOCHA (PREM\*4\*1 and PREM\*4\*2), PPS-N (PREN\*4\*1), PECS (PREC\*7\*1), and VistA (PSS\*1\*254, PSJ\*5\*423, and PSO\*7\*779).

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to PECS version (v) First Databank (FDB) Framework (Fwk) Upgrade version 4.5 for this release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of PECS FDB Fwk Upgrade to version 4.5 and applies to the changes made between this release and any previous release for this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issue for FDB Fwk Upgrade v4.5 PECS 7.0.1 / PREC\*7\*1 release.

### New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable (N/A) to the FDB Fwk Upgrade v4.5 PECS 7.0.1 / PREC\*7\*1 release.

### Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHA, Patient Care Services, and Pharmacy Benefits Management has requested the FDB Fwk upgrade from version 3.3 to version 4.5 for VA Pharmacy applications. PECS will be upgrading

the Application Programming Interface (API) calls in support of the FDB Fwk version 4.5 upgrade.

The following are the enhancements and modifications to the FDB Fwk Upgrade v4.5 PECS 7.0.1 / PREC\*7\*1 release.

- All of the required APIs will be updated to ensure that the PECS application utilizes the FDB Fwk version 4.5.
- The goal of the FDB Fwk Upgrade from version 3.3 to version 4.5 is that the PECS application functionality performs the same under this new framework.
- FDB-925 - PECS: As a PECS User, I want the Success/Failure Email Notifications from DATUP that indicate either Successful or Failure processing of the Duplicate Therapy Comparison Report
- FDB-727 - PECS: Easy Search by Dose Range
- FDB-1102 - PECS: Reports - Convert Duplicate Therapy Report
- FDB-728 - PECS: Easy Search by Interactions for a Single Drug
- FDB-5226 - PECS: Upgrade Advanced Query / Customization DDI for v4.4
- FDB-5466 - PECS: Interaction Description blank
- FDB-5384 - PECS: As a user, I can export advanced query DDI customization results
- FDB-5388 - PECS: As a user, I can perform searches using other criteria beyond interaction description and interaction ID to find DDI customizations within the advanced query page
- FDB-5578 - PECS: Error message upon clicking the Open link on the FDB interaction search results
- FDB-5599 - PECS SQA: Very few matches on fdb44_dif queries
- FDB-5598 - PECS: Clinical effect code values seems switched on the UI
- FDB-5385 - PECS: As a user, I can display FDB table result DDI details for advanced query results
- FDB-5387 - PECS: As a user, I can toggle between VA and FDB DDIs on the DDI Details page
- FDB-5386 - PECS: As a user, I can display monographs for DDI customizations
- FDB-5077 - PECS: Upgrade to build with Maven instead of Ant
- FDB-5663 - PECS: Implement Jenkins build version hash and 4-digit versions
- FDB-5659 - PECS: As a user, I can display the drug pair customization screen
- FDB-5650 - PECS: As a user, I can display VA table result DDI details for advanced query results
- FDB-5541 - PECS: As a user, I can customize top-level DDI details
- FDB-5513 - PECS: As a user, I can see the date when the FDB DIF DB was last updated and its version in the home page
- FDB-5514 - PECS: As a user, I can see the date when the last customization update file was created in the home page
- FDB-5737 - PECS: As a user, I can customize drug pairs for a VA DDI
- FDB-5861 - PECS: As an approver, I can submit as reviewed and approve DDI customizations
- FDB-5786 - PECS: Upgrade build to FDB v4.5.10
- FDB-5872 - PECS: Compute drug pairs for FDB v4.4 DDI drug pair comparison report using algorithm supplied by FDB vendor
- FDB-5883 - PECS: As a release manager, I can generate a custom update file for FDB v4.x
- FDB-6093 - PECS: Comparison report has drug pair tabs that are five digit and have blank content
- FDB-6080 - PECS Compare Report: drug pairs not showing up (or showing blank tab) for standard upd files that have an "A" operation on them
- FDB-6194 - PECS: DDI / drug pairs comparison report - For drug pair tabs that have a lot of records, the top description row is missing and present in the end of when the records listing completes
- FDB-6095 - PECS: DDI / drug pairs comparison report drug pair tabs are showing too many drug pairs which do not match record count in DDIMLINK.UPD file
- FDB-6127- PECS: Verify in SQA env connectivity to the new lower-environment FTP Server
- FDB-6074 - PECS: Issue on DDI / drug pairs comparison report while parsing monograph id field
- FDB-6116 - DATUP/PECS: Verify VA custom incremental update files containing added DDIs, and drug pairs can be loaded into PECS by DATUP
- FDB-6100 - DATUP/PECS: Verify FDB v4.5 standard incremental update files can be loaded into PECS by DATUP
- FDB-5408 - PECS: As a user, I can view the DDI / drug pairs comparison report
- FDB-6001 - PECS: Add ixfdbcustomddimstrings1 index to v4.5 FDB_CUSTOM_DDIMSTRINGS table, to match indexing from PECS production
- FDB-6178 - PECS: DDI / DP comparison report has drug pair tabs that are blank
- FDB-6229 - DATUP: Did not run successfully in PECS SQA on 3/3/2023 -- unable to pick up standard report changes
- FDB-6107 - PECS: Generate VA custom update DDI customizations times out
- FDB-6380 - PECS: As a user, I want to modify/maintain an existing VA custom DDI
- FDB-6378 - PECS: Ensure Drug Pairs are Calculated Correctly for the DDI/Drug Pair Comparison Report
- FDB-5867 - PECS: As an approver, I can reject, submit for delete, and delete DDI customizations
- FDB-6507 - PECS: Add a New Drug to Reverse DDI Interaction (Case 16.3)
- FDB-6506 - PECS: Add Drug to Forward DDI Interaction (Case 16.1)
- FDB-6516 - PECS: Add Drug to Forward DDI Interaction (Case 2.1)
- FDB-6206 - PECS: In the DDI/DP comparison report, drug pair tabs will not display for reverse interaction ids (\>= 16000) received in FDB v4.5 standard incremental .UPD files
- FDB-6504 - PECS: Add Drug to Reverse DDI Interaction (Case 2.3)
- FDB-6576 - PECS: Add Drug to Forward Interaction (Case 3.1)
- FDB-6577 - PECS: Add Drug to Reverse Interaction (Case 3.3)
- FDB-6597 - PECS: DDI / Drug Pair comparison report - Interaction id details showing up on the first tab of compare report even though there are no actual changes in the fields for these interactions
- FDB-6578 - PECS: Add Drug to Forward Interaction (Case 4.1)
- FDB-6579 - PECS: Add Drug to Reverse Interaction (Case 4.3)
- FDB-6228 - PECS: In DDI / DP comparison report the order of interactions displayed on the first report tab is not following a specific order
- FDB-6346 - PECS: DDI / drug pairs comparison report - Delete/Add Records dropped in SQA-Prod standard update load from 12-08 has 64 less records in SQA as compared to production same run
- FDB-5971 - PECS: Upgrade build to use FDB v4.5.10.4 and latest version of MOCHA common jar following MOCHA upgrade to FDB v4.5.10.4
- FDB-6689 - PECS: Easy Search - Reverse ID's being displayed and Generic drug order switched on interactions
- FDB-6308 - DATUP run failing: Custom update feature is not setting the correct value of the "previous issue date" and "Inc update File creation date" in the FDBUPDCONTROL.DAT, CT_Version table Issue date mismatch
- FDB-6632 - PECS: Easy Search - Interactions for a Single Drug
- FDB-6668 - PECS: Upgrade build to use FDB v4.5.11.1 and latest version of MOCHA common jar following MOCHA upgrade to FDB v4.5.11.1
- FDB-6700 - PECS: Easy Search Interactions for a Single Drug search results on PECS SQA returns less records than PECS PROD
- FDB-6815 - VistA MOCHA CPRS - From PECS - New and Existing DDI Customizations Regression Testing
- FDB-6902 - PECS: Spike the "Advanced Query / Customization \> Dose Range" Feature
- FDB-6903 - PECS: Spike the "Easy Search \> Dose Range" Feature
- FDB-6999 - PECS: Update Ear Config so WebLogic Prefers Spring Classes Packaged in Ear File<span id="_Toc61274730" class="anchor"></span>FDB-6971 - PECS: Update fdb-fwk-upgrade branch to use v7.0.2
- FDB-6971 - PECS: Update fdb-fwk-upgrade branch to use v7.0.2
- FDB-6845 - PECS: \[Issue Tracker \#5\] Easy Search - Interactions for a Single Drug - HTTP 500 Internal Server Error on certain searches: tablet, oral, sodium
- FDB-7002 - PECS: \[Issue Tracker \#5\] Display list for Easy Search Interactions for a Single Drug does not display the route of the drug in SQA but does in Production
- FDB-7078 - PECS: (Spike) Use a Database View to Associate VA Custom Dose Records with v4.5 Standard Records
- FDB-7057 - PECS: (Spike) Adv. Query / Customization \> Dose Range - Simple Queries to Populate FDB Table Results
- FDB-7224 - PECS: Merge fdb-fwk-upgrade into release/fdb-7.0 following conclusion of interim UAT
- FDB-7186 - PECS: Easy Search \> Dose Range - certain drugs giving error upon selection in search results
- FDB-7059 - PECS: Upgrade Advanced Query/Customization \> Duplicate Therapy to FDB v4.5
- FDB-6882 - PECS: As a user, I can export Advanced Query / Customization for Dose Range search results
- FDB-7058 - PECS: Upgrade Easy Search \> Dose Range to v4.5
- FDB-7167 - PECS: Adv. Query / Customization \> Dose Range - Add High Priority Search Fields to Populate FDB Table Results
- FDB-7316 - PECS: As an approver, I can submit as reviewed and approve DRC customizations
- FDB-7305 - PECS: Publish Custom Dose Range Record to VA Custom Update File
- FDB-7236 - PECS: Advanced Query/Customization for Duplicate Therapy - As a user I can click "Active/Open" links in VA Tables and FDB Tables Results sections to view the details page
- FDB-7304 - PECS: Create New Custom Dose Range Record
- FDB-7307 - PECS: Create new Custom Duplicate Therapy Record
- FDB-7037 - PECS: Easy Search for Dose Range - lack of data on dose range for certain drugs on SQA env
- FDB-7438 - PECS: (Step 2) Publish Duplicate Therapy customization to VA custom update file
- FDB-7296 - PECS: (Step 1) As an approver, I can submit as reviewed and approve Duplicate Therapy customizations
- FDB-7040 - PECS: Easy Search for Dose Range: Link to record in PECS is not available in SQA env
- FDB-7298 - PECS: Easy search for Dose Range - Different dose range related values in details screen results comparing SQA to PROD
- FDB-7439 - DATUP/PECS/MOCHA: (Step 3) Load VA custom update file with New Duplicate Therapy Record
- FDB-6195 - DATUP/PECS: Verify VA custom incremental update files containing DDI and drug pair deletions can be loaded into PECS by DATUP
- FDB-7567 - PECS: (Step 2b) Publish Duplicate Therapy customization to VA custom update file and confirm header row in UPD file contains FDB_CUSTOM_DPT_ALLOWANCE
- FDB-7565 - PECS: Easy Search for Dose Range - sort Dose Type dropdown options alphabetically
- FDB-7547 - PECS: Easy Search for Dose Range - Incorrect message-related field values
- FDB-7548 - PECS: Dose range comparison report displaying add "A" records / displaying conceptID with dose type code 00
- FDB-7235 - PECS: Advanced Query/Customization for Duplicate Therapy - As a user I can search for historical VA customization and FDB standard records
- FDB-7435 - PECS: Reconcile Dose Route values
- FDB-7563 - PECS: Duplicate Therapy Comparison Report
- FDB-7295 - PECS: Dose Range Comparison Report excluding Unit-related and Rate-related fields
- FDB-7501 - PECS: Dose Range Comparison Report for Unit-related and Rate-related fields
- FDB-7533 - PECS: Remove Dose Type Code 99 from Dose Type Dropdown in DRC Edit Screen
- FDB-7383 - PECS: Re-enable generation of full custom update file
- FDB-7668 - PECS/DATUP/MOCHA: (Step 1) Validate modification and deletion of DRC customizations
- FDB-7671 - PECS/DATUP/MOCHA: (Step 1) Validate modification and deletion of DPT customizations
- FDB-7753 - PECS Easy Search : No dose range results on Easy Search for some drugs(related to low/high half-life unit error from FDB dose screen API call)
- FDB-7486 - PECS: Upgrade build to use FDB v4.5.11.2 and latest version of MOCHA common jar following MOCHA upgrade to FDB v4.5.11.2
- FDB-7234 - PECS: Advanced Query/Customization for Duplicate Therapy - As a user I can export VA Table and FDB Table Results
- FDB-7656 - PECS: Null pointer exception @ "DDI clinical effect code" during DDI / drug pair comparison report generation for 9/22/2023 file (MKF45_UPD20230922.zip)
- FDB-7729 - PECS: Easy Search for Dose Range: Invalid order message on some drugs not matching production
- FDB-7801 - PECS/DATUP/MOCHA: (Step 1) As a user, I can see VA DRC customizations for dose routes newly introduced in FDB v4.5
- FDB-7582 - PECS/DATUP/MOCHA: Verify custom half-life unit values can be published to VA custom update file and loaded into FDB_CUSTOM_DOSING_3X DB table
- FDB-7893 - PECS: DRC Dose Unit dropdown is empty in Easy Search after FDB-7444 DB update
- FDB-7912 - PECS/DATUP/MOCHA: (Step 1) Validate DRC dose unit customizations
- FDB-7834 - PECS: In Easy Search, handle null responses from FDB v4.5 DispensableGeneric.getGenericDispensableDrug() API
- FDB-7906 - PECS: Easy Search for Dose Range - "No results for drugs checked" unexpected error for continuous route drugs when dose rate units is not empty
- FDB-7444 - PECS: Display Updated v4.5 Dose Unit Values on DRC Edit Screen
- FDB-7027 - PECS/MOCHA/VistA: UAT Issue Tracker \# 6 - Creating a VA Custom DDI using open blank form is giving an unexpected error message on VistA
- FDB-8118 - PECS/VistA: Validate that PSS Drug Dosing Lookup returns FDB routes for drug records having null high half-life values
- FDB-7651 - PECS/DATUP/MOCHA: (Step 1) Validate DRC rate field customizations
- FDB-8212 - PECS: Implement solution for Easy Search for Dose Range: when using milligrams for GCN 390, messages return with units eaches instead of in milligrams
- FDB-7997 - PECS: Easy Search for Duplicate Therapy - Duplicate allowance value returned is always FDB standard value even when VA customized value exists
- FDB-7003 - PECS: Ensure null values for Fdb4Ddiminteraction are handled properly within DrugDrugInteractionServiceImpl::createDTO()
- FDB-8020 - PECS: As a user, I can perform an Easy Search for drug-drug interaction with professional monograph and/or duplicate therapy
- FDB-8177 - PECS: As a user, I can see FDB custom DDI active customization reports
- FDB-8316 - PECS: Easy Search for Dose Range - handling of metric and form-based frequency values
- FDB-8247 - PECS/DATUP/MOCHA: Update Jenkinsfile to refer to targetBranch following upgrade of GitForensics plugin and removal of defaultBranch naming
- FDB-7800 - DATUP/PECS: Load FDB v4.5 standard update files into SQA environment to correct misspelling of capusles/kilogram/day dose unit
- FDB-8293 - PECS: Validate changed and deleted DPT customizations are written to VA custom update file and can be loaded successfully
- FDB-8253 - PECS: As a user, I can see Null Drug Pairs active customization reports
- FDB-6756 - PECS/DATUP/MOCHA: (Step 1) Low and high frequency customizations
- FDB-8347 - PECS: As a user, I can search for professional monographs via the Advanced Query/Customization tab
- FDB-8251 - PECS: As a user, I can see FDB Custom Professional Monograph active customization reports
- FDB-8250 - PECS: As a user, I can see FDB Custom Duplicate Therapy active customization reports
- FDB-6060 - PECS: As a user, I can search for drug pairs via the Advanced Query/Customization tab
- FDB-8249 - PECS: As a user, I can see FDB Custom Dose Range active customization reports
- FDB-8252 - PECS: As a user, I can see Deleted Monograph active customization reports
- FDB-8687 - PECS SQA : Custom update fails with error for Delete and update on VA Custom professional monograph
- FDB-8021 - MOCHA/DATUP/PECS: Integrate and validate sustainment build PREM\*3\*6 for MOCHA and then rebuild DATUP and PECS with updated MOCHA common jar
- FDB-8348 - PECS/DATUP/MOCHA: (Step 1) Upgrade and validate Professional Monograph customizations
- FDB-8155 - PECS: Upgrade build to use FDB v4.5.14.1 - MISC
- FDB-5456 - PECS: Clean up code references to specific FDB versions
- FDB-8871 - PECS/VistA/CPRS: Two monographs associated with the same VA custom DDI
- FDB-8822 - PECS: Complete required vulnerability remediation
- FDB-8632 - PECS: As an administrator, I can remove null drug pairs
- FDB-8336 - PECS: Improve handling of DB connections to mitigate connection pool exceptions
- FDB-8882 - PECS: Easy Search for Dose Range -- Link to record does not work in dev and sqa, freq low high other fields not matching prod
- FDB-7268 - PECS: Easy Search for Dose Range - Issue with Search strings with a concentration having '.' in the numeric value
- FDB-8920 - PECS: Improve handling of DB IO connection objects to mitigate leaks
- FDB-8892 - PECS: As a user I can perform drug pair lookups
- FDB-8298 - PECS: Update log4j2.xml application logging configuration to retain only last 10 files and ensure appropriate log levels are used when writing to logs to omit extraneous information
- FDB-8972 - PECS: Administration - Customize Settings
- FDB-8985 - PECS: After migration of VA Custom data in FDB-8285 - the dose units are missing for some of the records with the new dose units
- FDB-7026 - PECS: Easy Search - Interactions for a Single Drug: Searching by some search strings returns significantly fewer records in PECS SQA as compared to PECS PROD
- FDB-7011 - PECS: Remove duplicate weblogic-application.xml files
- FDB-8285 - PECS: Create and validate DB scripts to migrate customization data for DDI, DRC, Monograph, and DPT customizations from PECS PROD FDB_DIF.\* DB tables to PECS SQA FDB45_DIF.\* DB tables
- FDB-7282 - PECS: Advanced Query/Customization for Dose Range - Search by Concept ID Description - slowness and timeout error on more general search strings
- FDB-7632 – PECS: Ensure post-deployment instruction to end users to clear browser cache
  - Note: After executing the RFCs and deploying changes to an environment, end users are to clear their browser cache to ensure their browser will obtain the new version of the cached files.
- FDB-5646 - PECS: Modify maven build to create online help ear file
- FDB-7915 - VistA/CPRS: (Step 3) As a user, I can see VA DRC customizations 'DOSE UNITS' newly introduced in FDB v4.5
- FDB-9064 - PECS: Remove tspn/day and tablespoonful/day from VA customization dose unit values
- FDB-9101 - PECS: Remove dose routes inappropriate for DRC Screening
- FDB-9100 - PECS: Adjust query to fetch FDBDX from FDB_MEDCOND DB table for display in DRC Advanced Query/Customization and in Details views
- FDB-6883 - PECS: As a user, I can save queries for Advanced Query / Customization for Dose Range
- FDB-6884 - PECS: As a user, I can use a saved query for Advanced Query / Customization for Dose Range
- FDB-5993 - PECS: User unable to click on Save on the Add comment dialog box on the DDI FDB interaction screen as well as monograph ID details Add comments
- FDB-7813 - PECS: Download Export of Adv query customization -\> Duplicate Therapy, downloaded file defaults to Criteria tab in 4.5
- FDB-7281 - PECS: Advanced Query/Customization for Dose Range - Export to excel - Excel is defaulting to criteria tab when the sheet opens
- FDB-6681 - PECS: As a user, I can perform searches for Advanced Query / Customization for Dose Range
- FDB-9182 - PECS: Easy Search for Dose Range - Duplicate umbrella dose route value incorrectly returned in dose route dropdown
- FDB-9183 - PECS: Reintroduce perineural injection dose route because FDB vendor confirmed it is appropriate for DRC Screening beyond its umbrella route of Infiltration
- FDB-9103 - PECS: Online Help pages show PECS 6.0 when should show 7.0
- FDB-9052 - PECS: Upgrade to new FDB v4.5.15.1 API that fixes UOM conversion issue due to mixed case
- FDB-9050 - PECS: Administration - User Roles - Update User Roles
- FDB-6267 - PECS: Drug pairs screen: special characters (on the Info text) are showing up on the drug pairs selected table section
- FDB-6072 - PECS: VA custom update files need download as zip option
- FDB-9084 - PECS: Add "Medical Condition Description" field as column in Advanced Query/Customization and in Details view
- FDB-9208 - PECS: User unable to click on Save/Save on the Add pre customization comments : professional monograph scenarios
- FDB-9197 - PECS: User unable to click on Save/Save on the Add pre customization comments : duplicate therapy scenarios
- FDB-9051 - PECS: Home - Request Table Widgets
- FDB-9247 - PECS: Clicking the link for DDI open active link gives error
- FDB-8877 - PECS: Upgrade JSCH library to v0.2.23 to support upgrade of Centrify from v5.8.x to v6.0.x
- FDB-8022 - PECS: Integrate and validate sustainment build PREC\*6.2\*5
  - PECS-420: PECS application contains Java components which are subject to compliance with Technical Reference Model (TRM) to maintain authority to operate (ATO).

### Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FDB-6073 - PECS: VA custom update files need download as zip option

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation describing the new functionality introduced by this patch is available. Upon National Release, the documentation will be in the form of Adobe Acrobat files. Documentation will be found on the VA Software Documentation Library at:

<https://www.va.gov/vdl/application.asp?appid=204>

<table>
<caption>Table of PSO*7*467 Release DocumentationTable includes file description, file name, and FTP mode</caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 44%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Title</strong></th>
<th><strong>FTP Mode</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PREC_7_0_P1_RN.DOCX</p>
<p>PREC_7_0_P1_RN.PDF</p></td>
<td>PECS 7.0.1 PREC*7*1 Release Notes</td>
<td>Binary</td>
</tr>
<tr class="even">
<td><p>PREC_7_0_P1_IG.DOCX</p>
<p>PREC_7_0_P1_IG.DOCX</p></td>
<td>PECS 7.0.1 PREC*7*1 Installation Guide</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td><p>PREC_7_0_P1_DIBR.DOCX</p>
<p>PREC_7_0_P1_DIBR.PDF</p></td>
<td>PECS 7.0.1 PREC*7*1 Deployment, Installation, Back-Out, Rollback Guide</td>
<td>Binary</td>
</tr>
</tbody>
</table>

Table of PSO\*7\*467 Release DocumentationTable includes file description, file name, and FTP mode

### From: PREC*6.2*1 PECS Release Notes

## Initial Security Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS v6.2 builds on the functionality provided by PECS v.6.1 with a few new additions.

- Application code has been updated to comply with VA Security Standards.
- Using the Fortify Scan report as guidance, the false positive findings have been identified and documented in the .fpr file.
- Fortify scan defects and all defects discovered during compliance updates are fixed.
- The mitigation of Fortify scan defects that could not be remediated are documented in the .fpr file.
- The following technologies have been upgraded to the Technical Reference Model (TRM) standards for this Informational Patch release: WebLogic 12.1.3, Spring 4.2.9, Hibernate 5.1.1, and Log4j-api 2.10.0.

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No changes were made to the existing functionality of the application.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None.
